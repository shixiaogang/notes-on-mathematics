#!/usr/bin/env python3
"""Extract and audit bilingual index terms from the book's TeX sources."""

from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterator, NamedTuple, Sequence


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.book_catalog import volumes

VOLUMES = tuple(v["slug"] for v in volumes())
# Coverage is checked by actual calls and declarations, not a frozen word count.
EXPECTED_CALLS = None
EXPECTED_UNIQUE_TERMS = None
SHARED_TERM_FILES = (Path("tex/styles/environments.tex"),)
VERBATIM_ENVIRONMENTS = {"verbatim", "Verbatim", "lstlisting", "minted"}
CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
ABBREVIATION_RE = re.compile(
    r"^(?:\$[^$\n]+\$[- ]*)?[A-Z][A-Z0-9]*(?:[-/][A-Z0-9]+)*$"
)
# Capitalization only provides the default classification. These names follow
# the spelling used by their original publications.
VERIFIED_ABBREVIATIONS = frozenset(
    {"HyDE", "BERT-LeaQuR", "NeuQS", "ConvDR", "IRCoT"}
)
VERIFIED_PROPER_NAMES = frozenset(
    {"BM25", "BGE-M3", "DUET", "BRIGHT", "BEIR"}
)
RESERVED_INDEX_CHARACTERS = set('@!|"')


class TermOccurrence(NamedTuple):
    path: Path
    volume: str
    line: int
    column: int
    raw_call: str
    raw_display: str
    raw_sort: str | None
    key: str
    sort_key: str
    start: int = 0
    end: int = 0
    candidate: str | None = None
    abbreviation: str | None = None
    semantic_id: str | None = None


class TermMapping(NamedTuple):
    path: Path
    owner: str
    line: int
    column: int
    raw_source: str
    raw_translation: str
    key: str
    translation: str


class TermAlias(NamedTuple):
    path: Path
    owner: str
    line: int
    column: int
    raw_identity: str
    raw_display: str
    raw_translation: str
    identity: str
    display: str
    translation: str


class Diagnostic(NamedTuple):
    code: str
    path: Path
    line: int
    column: int
    message: str


class ScanError(ValueError):
    def __init__(self, path: Path, line: int, column: int, reason: str):
        self.path = Path(path)
        self.line = line
        self.column = column
        self.reason = reason
        super().__init__(f"{self.path.as_posix()}:{line}:{column}: {reason}")


class _InputEvent(NamedTuple):
    value: str


def _line_column(text: str, position: int) -> tuple[int, int]:
    line = text.count("\n", 0, position) + 1
    line_start = text.rfind("\n", 0, position) + 1
    return line, position - line_start + 1


def _is_escaped(text: str, position: int) -> bool:
    backslashes = 0
    cursor = position - 1
    while cursor >= 0 and text[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1


def _control_sequence(text: str, position: int) -> tuple[str, int]:
    if position >= len(text) or text[position] != "\\":
        return "", position
    cursor = position + 1
    if cursor >= len(text):
        return "", cursor
    if text[cursor].isalpha() or text[cursor] == "@":
        end = cursor + 1
        while end < len(text) and (
            text[end].isalpha() or text[end] == "@"
        ):
            end += 1
        return text[cursor:end], end
    return text[cursor], cursor + 1


def _skip_comment(text: str, position: int) -> int:
    newline = text.find("\n", position)
    return len(text) if newline < 0 else newline + 1


def _skip_space_and_comments(text: str, position: int) -> int:
    cursor = position
    while cursor < len(text):
        if text[cursor].isspace():
            cursor += 1
            continue
        if text[cursor] == "%" and not _is_escaped(text, cursor):
            cursor = _skip_comment(text, cursor)
            continue
        break
    return cursor


def _parse_group(
    text: str,
    position: int,
    opening: str,
    closing: str,
    path: Path,
    error_position: int,
    reason: str,
) -> tuple[str, int]:
    if position >= len(text) or text[position] != opening:
        line, column = _line_column(text, error_position)
        raise ScanError(path, line, column, f"missing {reason}")

    stack = [closing]
    cursor = position + 1
    while cursor < len(text):
        character = text[cursor]
        if character == "\\":
            _, cursor = _control_sequence(text, cursor)
            continue
        if character == "%" and not _is_escaped(text, cursor):
            cursor = _skip_comment(text, cursor)
            continue
        if character == "{":
            stack.append("}")
            cursor += 1
            continue
        if opening == "[" and character == "[":
            stack.append("]")
            cursor += 1
            continue
        if character == stack[-1]:
            stack.pop()
            cursor += 1
            if not stack:
                return text[position + 1 : cursor - 1], cursor
            continue
        cursor += 1

    line, column = _line_column(text, error_position)
    raise ScanError(path, line, column, f"unclosed {reason}")


def _canonicalize_tex(value: str) -> str:
    output: list[str] = []
    pending_space = False
    cursor = 0
    while cursor < len(value):
        character = value[cursor]
        if character == "\\":
            name, end = _control_sequence(value, cursor)
            output.append(value[cursor:end])
            cursor = end
            pending_space = False
            continue
        if character == "%" and not _is_escaped(value, cursor):
            cursor = _skip_comment(value, cursor)
            continue
        if character.isspace():
            pending_space = bool(output)
            cursor += 1
            continue
        if pending_space:
            output.append(" ")
            pending_space = False
        output.append(character)
        cursor += 1
    return "".join(output).strip()


def _split_parenthetical(value: str) -> list[str]:
    pieces: list[str] = []
    start = 0
    depth = 0
    cursor = 0
    while cursor < len(value):
        character = value[cursor]
        if character == "\\":
            _, cursor = _control_sequence(value, cursor)
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth = max(0, depth - 1)
        elif depth == 0 and character in {",", "，"}:
            pieces.append(value[start:cursor])
            start = cursor + 1
        cursor += 1
    pieces.append(value[start:])
    return pieces


def _parenthetical_candidate(
    text: str, position: int
) -> tuple[str | None, str | None]:
    cursor = _skip_space_and_comments(text, position)
    if cursor >= len(text) or text[cursor] not in {"(", "（"}:
        return None, None
    opening = text[cursor]
    closing = ")" if opening == "(" else "）"
    depth = 1
    end = cursor + 1
    while end < len(text):
        if text[end] == "\\":
            _, end = _control_sequence(text, end)
            continue
        if text[end] == opening:
            depth += 1
        elif text[end] == closing:
            depth -= 1
            if depth == 0:
                break
        end += 1
    if depth:
        return None, None

    content = _canonicalize_tex(text[cursor + 1 : end])
    pieces = [_canonicalize_tex(piece) for piece in _split_parenthetical(content)]
    if not pieces:
        return None, None
    candidate = re.split(r"\s*(?:也称|又称|亦称)\s*", pieces[0], maxsplit=1)[0]
    if not re.search(r"[A-Za-z]", candidate) or CJK_RE.search(candidate):
        return None, None
    abbreviation = None
    if len(pieces) > 1 and ABBREVIATION_RE.fullmatch(pieces[1]):
        abbreviation = pieces[1]
    return candidate, abbreviation


def _skip_verb(text: str, position: int) -> int:
    cursor = position
    if cursor < len(text) and text[cursor] == "*":
        cursor += 1
    if cursor >= len(text) or text[cursor] in "\r\n":
        return cursor
    delimiter = text[cursor]
    end = text.find(delimiter, cursor + 1)
    newline = text.find("\n", cursor + 1)
    if end < 0 or (newline >= 0 and newline < end):
        return len(text) if newline < 0 else newline + 1
    return end + 1


def _verbatim_end(text: str, position: int, environment: str) -> int:
    marker = f"\\end{{{environment}}}"
    end = text.find(marker, position)
    return len(text) if end < 0 else end + len(marker)


def _term_at(
    text: str, path: Path, volume: str, start: int, command_end: int
) -> tuple[TermOccurrence, int]:
    cursor = _skip_space_and_comments(text, command_end)
    raw_sort = None
    if cursor < len(text) and text[cursor] == "[":
        raw_sort, cursor = _parse_group(
            text,
            cursor,
            "[",
            "]",
            path,
            start,
            "optional argument",
        )
        cursor = _skip_space_and_comments(text, cursor)
    raw_display, end = _parse_group(
        text,
        cursor,
        "{",
        "}",
        path,
        start,
        "required argument",
    )
    line, column = _line_column(text, start)
    key = _canonicalize_tex(raw_display)
    sort_key = _canonicalize_tex(raw_sort) if raw_sort is not None else key
    candidate, abbreviation = _parenthetical_candidate(text, end)
    occurrence = TermOccurrence(
        path=path,
        volume=volume,
        line=line,
        column=column,
        raw_call=text[start:end],
        raw_display=raw_display,
        raw_sort=raw_sort,
        key=key,
        sort_key=sort_key,
        start=start,
        end=end,
        candidate=candidate,
        abbreviation=abbreviation,
    )
    return occurrence, end


def _term_alias_at(
    text: str, path: Path, volume: str, start: int, command_end: int
) -> tuple[TermOccurrence, int]:
    identity_start = _skip_space_and_comments(text, command_end)
    raw_identity, identity_end = _parse_group(
        text,
        identity_start,
        "{",
        "}",
        path,
        start,
        "semantic identity argument",
    )
    display_start = _skip_space_and_comments(text, identity_end)
    raw_display, end = _parse_group(
        text,
        display_start,
        "{",
        "}",
        path,
        start,
        "display argument",
    )
    line, column = _line_column(text, start)
    identity = _canonicalize_tex(raw_identity)
    key = _canonicalize_tex(raw_display)
    candidate, abbreviation = _parenthetical_candidate(text, end)
    return (
        TermOccurrence(
            path=path,
            volume=volume,
            line=line,
            column=column,
            raw_call=text[start:end],
            raw_display=raw_display,
            raw_sort=None,
            key=key,
            sort_key=f"{key}-{identity}",
            start=start,
            end=end,
            candidate=candidate,
            abbreviation=abbreviation,
            semantic_id=identity,
        ),
        end,
    )


def _events(
    text: str, path: Path, volume: str
) -> Iterator[TermOccurrence | _InputEvent]:
    cursor = 0
    while cursor < len(text):
        character = text[cursor]
        if character == "%" and not _is_escaped(text, cursor):
            cursor = _skip_comment(text, cursor)
            continue
        if character != "\\":
            cursor += 1
            continue

        start = cursor
        name, command_end = _control_sequence(text, cursor)
        if name == "verb":
            cursor = _skip_verb(text, command_end)
            continue
        if name == "begin":
            argument_start = _skip_space_and_comments(text, command_end)
            if argument_start < len(text) and text[argument_start] == "{":
                environment, argument_end = _parse_group(
                    text,
                    argument_start,
                    "{",
                    "}",
                    path,
                    start,
                    "environment argument",
                )
                environment = _canonicalize_tex(environment)
                if environment in VERBATIM_ENVIRONMENTS:
                    cursor = _verbatim_end(text, argument_end, environment)
                    continue
            cursor = command_end
            continue
        if name == "term":
            occurrence, cursor = _term_at(
                text, path, volume, start, command_end
            )
            yield occurrence
            continue
        if name == "termalias":
            occurrence, cursor = _term_alias_at(
                text, path, volume, start, command_end
            )
            yield occurrence
            continue
        if name == "input":
            argument_start = _skip_space_and_comments(text, command_end)
            if (
                argument_start >= len(text)
                or text[argument_start] != "{"
            ):
                cursor = command_end
                continue
            raw_input, cursor = _parse_group(
                text,
                argument_start,
                "{",
                "}",
                path,
                start,
                "input argument",
            )
            yield _InputEvent(_canonicalize_tex(raw_input))
            continue
        cursor = command_end


def scan_tex(text: str, path: Path | str, volume: str) -> list[TermOccurrence]:
    source_path = Path(path)
    return [
        event
        for event in _events(text, source_path, volume)
        if isinstance(event, TermOccurrence)
    ]


def _resolve_input(value: str) -> Path:
    candidate = Path(value)
    if not candidate.suffix:
        candidate = candidate.with_suffix(".tex")
    return candidate


def collect_terms(root: Path | str) -> list[TermOccurrence]:
    project_root = Path(root)
    occurrences: list[TermOccurrence] = []

    def walk(path: Path, volume: str, stack: tuple[Path, ...]) -> None:
        normalized = Path(path.as_posix())
        absolute = project_root / normalized
        if normalized in stack:
            chain = " -> ".join(item.as_posix() for item in (*stack, normalized))
            raise ValueError(f"recursive TeX input: {chain}")
        if not absolute.is_file():
            raise FileNotFoundError(f"missing TeX input: {normalized.as_posix()}")
        text = absolute.read_text(encoding="utf-8")
        for event in _events(text, normalized, volume):
            if isinstance(event, TermOccurrence):
                occurrences.append(event)
            else:
                child = _resolve_input(event.value)
                walk(child, volume, (*stack, normalized))

    for volume in VOLUMES:
        volume_path = Path("tex") / volume / "volume.tex"
        walk(volume_path, volume, ())

    traversed = {occurrence.path for occurrence in occurrences}
    for shared_path in SHARED_TERM_FILES:
        if shared_path in traversed:
            continue
        absolute = project_root / shared_path
        if absolute.is_file():
            occurrences.extend(
                scan_tex(
                    absolute.read_text(encoding="utf-8"),
                    shared_path,
                    VOLUMES[0],
                )
            )
    return occurrences


def _mapping_declarations(
    text: str, path: Path, owner: str
) -> Iterator[TermMapping]:
    cursor = 0
    while cursor < len(text):
        character = text[cursor]
        if character == "%" and not _is_escaped(text, cursor):
            cursor = _skip_comment(text, cursor)
            continue
        if character != "\\":
            cursor += 1
            continue
        start = cursor
        name, command_end = _control_sequence(text, cursor)
        if name == "verb":
            cursor = _skip_verb(text, command_end)
            continue
        if name == "begin":
            argument_start = _skip_space_and_comments(text, command_end)
            if argument_start < len(text) and text[argument_start] == "{":
                environment, argument_end = _parse_group(
                    text,
                    argument_start,
                    "{",
                    "}",
                    path,
                    start,
                    "environment argument",
                )
                environment = _canonicalize_tex(environment)
                if environment in VERBATIM_ENVIRONMENTS:
                    cursor = _verbatim_end(text, argument_end, environment)
                    continue
            cursor = command_end
            continue
        if name != "DeclareBookIndexTerm":
            cursor = command_end
            continue

        source_start = _skip_space_and_comments(text, command_end)
        raw_source, source_end = _parse_group(
            text,
            source_start,
            "{",
            "}",
            path,
            start,
            "mapping source argument",
        )
        translation_start = _skip_space_and_comments(text, source_end)
        raw_translation, cursor = _parse_group(
            text,
            translation_start,
            "{",
            "}",
            path,
            start,
            "mapping translation argument",
        )
        line, column = _line_column(text, start)
        yield TermMapping(
            path=path,
            owner=owner,
            line=line,
            column=column,
            raw_source=raw_source,
            raw_translation=raw_translation,
            key=_canonicalize_tex(raw_source),
            translation=_canonicalize_tex(raw_translation),
        )


def parse_mappings(root: Path | str) -> list[TermMapping]:
    project_root = Path(root)
    mappings: list[TermMapping] = []
    for owner in VOLUMES:
        path = Path("tex/index-terms") / f"{owner}.tex"
        absolute = project_root / path
        if not absolute.is_file():
            continue
        mappings.extend(
            _mapping_declarations(
                absolute.read_text(encoding="utf-8"), path, owner
            )
        )
    return mappings


def _alias_declarations(
    text: str, path: Path, owner: str
) -> Iterator[TermAlias]:
    cursor = 0
    while cursor < len(text):
        character = text[cursor]
        if character == "%" and not _is_escaped(text, cursor):
            cursor = _skip_comment(text, cursor)
            continue
        if character != "\\":
            cursor += 1
            continue
        start = cursor
        name, command_end = _control_sequence(text, cursor)
        if name == "verb":
            cursor = _skip_verb(text, command_end)
            continue
        if name == "begin":
            argument_start = _skip_space_and_comments(text, command_end)
            if argument_start < len(text) and text[argument_start] == "{":
                environment, argument_end = _parse_group(
                    text,
                    argument_start,
                    "{",
                    "}",
                    path,
                    start,
                    "environment argument",
                )
                environment = _canonicalize_tex(environment)
                if environment in VERBATIM_ENVIRONMENTS:
                    cursor = _verbatim_end(text, argument_end, environment)
                    continue
            cursor = command_end
            continue
        if name != "DeclareBookIndexTermAlias":
            cursor = command_end
            continue
        identity_start = _skip_space_and_comments(text, command_end)
        raw_identity, identity_end = _parse_group(
            text,
            identity_start,
            "{",
            "}",
            path,
            start,
            "alias identity argument",
        )
        display_start = _skip_space_and_comments(text, identity_end)
        raw_display, display_end = _parse_group(
            text,
            display_start,
            "{",
            "}",
            path,
            start,
            "alias display argument",
        )
        translation_start = _skip_space_and_comments(text, display_end)
        raw_translation, cursor = _parse_group(
            text,
            translation_start,
            "{",
            "}",
            path,
            start,
            "alias translation argument",
        )
        line, column = _line_column(text, start)
        yield TermAlias(
            path=path,
            owner=owner,
            line=line,
            column=column,
            raw_identity=raw_identity,
            raw_display=raw_display,
            raw_translation=raw_translation,
            identity=_canonicalize_tex(raw_identity),
            display=_canonicalize_tex(raw_display),
            translation=_canonicalize_tex(raw_translation),
        )


def parse_aliases(root: Path | str) -> list[TermAlias]:
    project_root = Path(root)
    aliases: list[TermAlias] = []
    for owner in VOLUMES:
        path = Path("tex/index-terms") / f"{owner}.tex"
        absolute = project_root / path
        if not absolute.is_file():
            continue
        aliases.extend(
            _alias_declarations(
                absolute.read_text(encoding="utf-8"), path, owner
            )
        )
    return aliases


def _diagnostic(
    code: str,
    item: TermOccurrence | TermMapping | TermAlias,
    message: str,
) -> Diagnostic:
    return Diagnostic(code, item.path, item.line, item.column, message)


def _contains_reserved_character(value: str) -> bool:
    return any(character in value for character in RESERVED_INDEX_CHARACTERS)


def _is_abbreviation(value: str) -> bool:
    if value in VERIFIED_PROPER_NAMES:
        return False
    if value in VERIFIED_ABBREVIATIONS:
        return True
    return bool(ABBREVIATION_RE.fullmatch(value))


def audit(
    occurrences: Sequence[TermOccurrence],
    mappings: Sequence[TermMapping],
    aliases: Sequence[TermAlias] = (),
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    first_occurrence: dict[str, TermOccurrence] = {}
    sort_keys: defaultdict[str, set[str]] = defaultdict(set)
    explicit_sort_displays: defaultdict[str, set[str]] = defaultdict(set)
    for occurrence in occurrences:
        first_occurrence.setdefault(occurrence.key, occurrence)
        if occurrence.semantic_id is not None:
            continue
        sort_keys[occurrence.key].add(occurrence.sort_key)
        if occurrence.raw_sort is not None:
            explicit_sort_displays[occurrence.sort_key].add(occurrence.key)

    for key, values in sort_keys.items():
        if len(values) > 1:
            item = first_occurrence[key]
            diagnostics.append(
                _diagnostic(
                    "SORT_KEY_CONFLICT",
                    item,
                    f"{key!r} uses multiple sort keys: {sorted(values)!r}",
                )
            )
    for sort_key, displays in explicit_sort_displays.items():
        if len(displays) > 1:
            item = first_occurrence[next(iter(displays))]
            diagnostics.append(
                _diagnostic(
                    "SORT_KEY_COLLISION",
                    item,
                    f"sort key {sort_key!r} is shared by {sorted(displays)!r}",
                )
            )

    mappings_by_key: defaultdict[str, list[TermMapping]] = defaultdict(list)
    for mapping in mappings:
        mappings_by_key[mapping.key].append(mapping)
        if not mapping.key:
            diagnostics.append(
                _diagnostic("EMPTY_MAPPING_KEY", mapping, "mapping key is empty")
            )
        if not mapping.translation:
            diagnostics.append(
                _diagnostic(
                    "EMPTY_TRANSLATION", mapping, "mapping translation is empty"
                )
            )
        if mapping.key and mapping.key == mapping.translation:
            diagnostics.append(
                _diagnostic(
                    "SELF_MAPPING", mapping, f"{mapping.key!r} maps to itself"
                )
            )
        if _contains_reserved_character(mapping.key) or _contains_reserved_character(
            mapping.translation
        ):
            diagnostics.append(
                _diagnostic(
                    "RESERVED_INDEX_CHARACTER",
                    mapping,
                    "mapping contains a reserved makeindex/xindy character",
                )
            )
        if mapping.translation and CJK_RE.search(mapping.translation):
            diagnostics.append(
                _diagnostic(
                    "NON_ENGLISH_TRANSLATION",
                    mapping,
                    f"{mapping.key!r} has a translation containing Chinese",
                )
            )

    for key, declarations in mappings_by_key.items():
        if len(declarations) > 1:
            for duplicate in declarations[1:]:
                diagnostics.append(
                    _diagnostic(
                        "DUPLICATE_MAPPING",
                        duplicate,
                        f"{key!r} is declared more than once",
                    )
                )
            translations = {
                declaration.translation for declaration in declarations
            }
            if len(translations) > 1:
                diagnostics.append(
                    _diagnostic(
                        "TRANSLATION_CONFLICT",
                        declarations[1],
                        f"{key!r} has conflicting translations: "
                        f"{sorted(translations)!r}",
                    )
                )

    abbreviation_graph = {
        key: declarations[0].translation
        for key, declarations in mappings_by_key.items()
        if _is_abbreviation(key)
        and _is_abbreviation(declarations[0].translation)
    }
    reported_cycles: set[frozenset[str]] = set()
    for start in abbreviation_graph:
        path: list[str] = []
        positions: dict[str, int] = {}
        current = start
        while current in abbreviation_graph and current not in positions:
            positions[current] = len(path)
            path.append(current)
            current = abbreviation_graph[current]
        if current not in positions:
            continue
        cycle = path[positions[current] :]
        cycle_key = frozenset(cycle)
        if len(cycle) < 2 or cycle_key in reported_cycles:
            continue
        reported_cycles.add(cycle_key)
        item = mappings_by_key[cycle[0]][0]
        diagnostics.append(
            _diagnostic(
                "ABBREVIATION_CYCLE",
                item,
                f"abbreviation mappings form a cycle: "
                f"{' -> '.join((*cycle, cycle[0]))}",
            )
        )

    for key, declarations in mappings_by_key.items():
        first_mapping = declarations[0]
        occurrence = first_occurrence.get(key)
        if occurrence is None:
            diagnostics.append(
                _diagnostic(
                    "ORPHAN_MAPPING",
                    first_mapping,
                    f"{key!r} has no matching index term",
                )
            )
            continue
        if first_mapping.owner != occurrence.volume:
            diagnostics.append(
                _diagnostic(
                    "WRONG_OWNER",
                    first_mapping,
                    f"{key!r} belongs to {occurrence.volume}, "
                    f"not {first_mapping.owner}",
                )
            )
        if not CJK_RE.search(key) and not _is_abbreviation(key):
            diagnostics.append(
                _diagnostic(
                    "UNEXPECTED_ENGLISH_MAPPING",
                    first_mapping,
                    f"complete English/proper/math term {key!r} "
                    "must remain unmapped",
                )
            )

    for key, occurrence in first_occurrence.items():
        declarations = mappings_by_key.get(key, [])
        has_translation = any(item.translation for item in declarations)
        if CJK_RE.search(key) and not has_translation:
            diagnostics.append(
                _diagnostic(
                    "MISSING_MAPPING",
                    occurrence,
                    f"Chinese term {key!r} has no English mapping",
                )
            )
        if _is_abbreviation(key) and not has_translation:
            diagnostics.append(
                _diagnostic(
                    "MISSING_ABBREVIATION_EXPANSION",
                    occurrence,
                    f"abbreviation {key!r} has no expansion",
                )
            )
    aliases_by_identity: defaultdict[str, list[TermAlias]] = defaultdict(list)
    for alias in aliases:
        aliases_by_identity[alias.identity].append(alias)
        if (
            not alias.identity
            or not alias.display
            or not alias.translation
        ):
            diagnostics.append(
                _diagnostic(
                    "EMPTY_TERM_ALIAS",
                    alias,
                    "semantic alias identity, display, and translation "
                    "must not be empty",
                )
            )
        if any(
            _contains_reserved_character(value)
            for value in (alias.identity, alias.display, alias.translation)
        ):
            diagnostics.append(
                _diagnostic(
                    "RESERVED_INDEX_CHARACTER",
                    alias,
                    "semantic alias contains a reserved makeindex/xindy "
                    "character",
                )
            )
        if alias.translation and CJK_RE.search(alias.translation):
            diagnostics.append(
                _diagnostic(
                    "NON_ENGLISH_TRANSLATION",
                    alias,
                    f"alias {alias.identity!r} has a translation "
                    "containing Chinese",
                )
            )

    for identity, declarations in aliases_by_identity.items():
        if len(declarations) > 1:
            for duplicate in declarations[1:]:
                diagnostics.append(
                    _diagnostic(
                        "DUPLICATE_TERM_ALIAS",
                        duplicate,
                        f"semantic alias {identity!r} is declared more than once",
                    )
                )

    first_semantic_occurrence: dict[str, TermOccurrence] = {}
    for occurrence in occurrences:
        if occurrence.semantic_id is not None:
            first_semantic_occurrence.setdefault(
                occurrence.semantic_id, occurrence
            )
    for identity, occurrence in first_semantic_occurrence.items():
        declarations = aliases_by_identity.get(identity, [])
        if not declarations:
            diagnostics.append(
                _diagnostic(
                    "MISSING_TERM_ALIAS",
                    occurrence,
                    f"semantic alias {identity!r} is not declared",
                )
            )
            continue
        declaration = declarations[0]
        if declaration.display != occurrence.key:
            diagnostics.append(
                _diagnostic(
                    "TERM_ALIAS_DISPLAY_MISMATCH",
                    occurrence,
                    f"semantic alias {identity!r} displays {occurrence.key!r}, "
                    f"expected {declaration.display!r}",
                )
            )
        if declaration.owner != occurrence.volume:
            diagnostics.append(
                _diagnostic(
                    "WRONG_ALIAS_OWNER",
                    declaration,
                    f"semantic alias {identity!r} belongs to "
                    f"{occurrence.volume}, not {declaration.owner}",
                )
            )
    for identity, declarations in aliases_by_identity.items():
        if identity not in first_semantic_occurrence:
            diagnostics.append(
                _diagnostic(
                    "ORPHAN_TERM_ALIAS",
                    declarations[0],
                    f"semantic alias {identity!r} has no matching index term",
                )
            )
    return diagnostics


def audit_statistics(
    occurrences: Sequence[TermOccurrence],
    expected_calls: int,
    expected_unique: int,
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    actual_calls = len(occurrences)
    actual_unique = len({occurrence.key for occurrence in occurrences})
    path = occurrences[0].path if occurrences else Path("tex")
    if expected_calls is not None and actual_calls != expected_calls:
        diagnostics.append(
            Diagnostic(
                "CALL_COUNT_MISMATCH",
                path,
                1,
                1,
                f"term call count is {actual_calls}, expected {expected_calls}",
            )
        )
    if expected_unique is not None and actual_unique != expected_unique:
        diagnostics.append(
            Diagnostic(
                "UNIQUE_COUNT_MISMATCH",
                path,
                1,
                1,
                f"unique term count is {actual_unique}, "
                f"expected {expected_unique}",
            )
        )
    return diagnostics


def _parse_idx_entries(text: str, path: Path) -> Iterator[tuple[str, str, int]]:
    cursor = 0
    while cursor < len(text):
        start = text.find("\\indexentry", cursor)
        if start < 0:
            return
        _, command_end = _control_sequence(text, start)
        entry_start = _skip_space_and_comments(text, command_end)
        entry, entry_end = _parse_group(
            text,
            entry_start,
            "{",
            "}",
            path,
            start,
            "index entry argument",
        )
        page_start = _skip_space_and_comments(text, entry_end)
        page, cursor = _parse_group(
            text,
            page_start,
            "{",
            "}",
            path,
            start,
            "index page argument",
        )
        line, _ = _line_column(text, start)
        yield entry, page, line


def _normalize_idx_tex(value: str) -> str:
    value = re.sub(
        r'\\mathaccent\s+"?[0-9A-Fa-f]+\s*\\relax\s+([A-Za-z])',
        r"\\widehat \1",
        value,
    )
    value = re.sub(r"(\$[^$\n]*?)\s+\$", r"\1$", value)
    return _canonicalize_tex(value)


def audit_index_artifacts(
    occurrences: Sequence[TermOccurrence],
    mappings: Sequence[TermMapping],
    idx_text: str,
    ind_text: str,
    base_path: Path | str,
    aliases: Sequence[TermAlias] = (),
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    base = Path(base_path)
    translation_keys: defaultdict[str, set[str]] = defaultdict(set)
    mapping_translations: dict[str, str] = {}
    mapped_keys: set[str] = set()
    for mapping in mappings:
        if not mapping.translation:
            continue
        mapped_keys.add(mapping.key)
        translation_keys[mapping.translation].add(mapping.key)
        mapping_translations.setdefault(mapping.key, mapping.translation)
    aliases_by_identity = {
        alias.identity: alias for alias in aliases if alias.translation
    }
    for alias in aliases:
        if not alias.translation:
            continue
        mapped_keys.add(alias.display)
        translation_keys[alias.translation].add(alias.display)
    known_keys = {occurrence.key for occurrence in occurrences}
    expected_entries: set[tuple[str, str]] = set()
    expected_displays_by_sort: defaultdict[str, set[str]] = defaultdict(set)
    for occurrence in occurrences:
        translation = mapping_translations.get(occurrence.key)
        if occurrence.semantic_id is not None:
            alias = aliases_by_identity.get(occurrence.semantic_id)
            if alias is not None:
                translation = alias.translation
        display = occurrence.key
        if translation is not None:
            display = f"{display}，{translation}"
            expected_displays_by_sort[occurrence.sort_key].add(display)
        expected_entries.add((occurrence.sort_key, display))

    for entry, _, line in _parse_idx_entries(idx_text, base.with_suffix(".idx")):
        entry_body = entry.rsplit("|", 1)[0]
        if "@" in entry_body:
            sort_key, display = entry_body.split("@", 1)
        else:
            sort_key = display = entry_body
        sort_key = _normalize_idx_tex(sort_key)
        source, separator, english = display.partition("，")
        source = _normalize_idx_tex(source)
        english = _normalize_idx_tex(english)
        display = f"{source}{separator}{english}"
        if (sort_key, display) in expected_entries:
            continue
        if display in known_keys:
            if display in mapped_keys:
                diagnostics.append(
                    Diagnostic(
                        "MISSING_INDEX_TRANSLATION",
                        base.with_suffix(".idx"),
                        line,
                        1,
                        f"mapped term {display!r} is displayed without English",
                    )
                )
            continue
        if not separator:
            if display in translation_keys:
                diagnostics.append(
                    Diagnostic(
                        "ORPHAN_INDEX_ENGLISH",
                        base.with_suffix(".idx"),
                        line,
                        1,
                        f"English display {display!r} has no source term",
                    )
                )
            if source not in known_keys and display not in translation_keys:
                diagnostics.append(Diagnostic(
                    "ORPHAN_INDEX_TERM", base.with_suffix(".idx"), line, 1,
                    f"index display source {source!r} is not a term in this edition",
                ))
            continue
        if source not in known_keys:
            diagnostics.append(
                Diagnostic(
                    "ORPHAN_INDEX_TERM",
                    base.with_suffix(".idx"),
                    line,
                    1,
                    f"index display source {source!r} is not a term",
                )
            )
            continue
        expected_displays = expected_displays_by_sort.get(sort_key, set())
        diagnostics.append(
            Diagnostic(
                "INDEX_TRANSLATION_MISMATCH",
                base.with_suffix(".idx"),
                line,
                1,
                f"sort identity {sort_key!r} displays {display!r}, expected "
                f"{sorted(expected_displays)!r}",
            )
        )

    seen_items: dict[str, int] = {}
    for line_number, line in enumerate(ind_text.splitlines(), 1):
        stripped = line.strip()
        if not stripped.startswith("\\item "):
            continue
        item = stripped[len("\\item ") :]
        display = item.split("，\\hyperpage", 1)[0]
        source = _normalize_idx_tex(display.partition("，")[0])
        if source not in known_keys:
            diagnostics.append(Diagnostic(
                "ORPHAN_INDEX_TERM", base.with_suffix(".ind"), line_number, 1,
                f"index item source {source!r} is not a term in this edition",
            ))
        if display in seen_items:
            diagnostics.append(
                Diagnostic(
                    "DUPLICATE_INDEX_ITEM",
                    base.with_suffix(".ind"),
                    line_number,
                    1,
                    f"index item {display!r} is repeated",
                )
            )
        else:
            seen_items[display] = line_number
        pages = re.findall(r"\\hyperpage\{([^{}]+)\}", item)
        repeated_pages = sorted(
            page for page, count in Counter(pages).items() if count > 1
        )
        if repeated_pages:
            diagnostics.append(
                Diagnostic(
                    "DUPLICATE_INDEX_PAGE",
                    base.with_suffix(".ind"),
                    line_number,
                    1,
                    f"index item {display!r} repeats pages {repeated_pages!r}",
                )
            )
    return diagnostics


def _artifact_diagnostics(
    root: Path,
    occurrences: Sequence[TermOccurrence],
    mappings: Sequence[TermMapping],
    aliases: Sequence[TermAlias],
) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    build = root / "build"
    if not build.is_dir():
        return diagnostics
    for idx_path in sorted(build.glob("*.idx")):
        ind_path = idx_path.with_suffix(".ind")
        if not ind_path.is_file():
            continue
        scoped_occurrences = occurrences if idx_path.stem == "main" else [
            occurrence for occurrence in occurrences if occurrence.volume == idx_path.stem or occurrence.path in SHARED_TERM_FILES
        ]
        diagnostics.extend(
            audit_index_artifacts(
                scoped_occurrences,
                mappings,
                idx_path.read_text(encoding="utf-8", errors="replace"),
                ind_path.read_text(encoding="utf-8", errors="replace"),
                idx_path.with_suffix("").relative_to(root),
                aliases,
            )
        )
    return diagnostics


def _json_string(value: str | None) -> str:
    return json.dumps(value, ensure_ascii=False)


def _unique_occurrences(
    occurrences: Sequence[TermOccurrence],
) -> list[tuple[TermOccurrence, int]]:
    first: dict[str, TermOccurrence] = {}
    counts: Counter[str] = Counter()
    for occurrence in occurrences:
        first.setdefault(occurrence.key, occurrence)
        counts[occurrence.key] += 1
    return [(occurrence, counts[key]) for key, occurrence in first.items()]


def _print_extract(occurrences: Sequence[TermOccurrence]) -> None:
    for occurrence, calls in _unique_occurrences(occurrences):
        location = (
            f"{occurrence.path.as_posix()}:{occurrence.line}:{occurrence.column}"
        )
        print(
            "\t".join(
                (
                    "TERM",
                    f"owner={occurrence.volume}",
                    f"first={location}",
                    f"calls={calls}",
                    f"sort={_json_string(occurrence.sort_key)}",
                    f"display={_json_string(occurrence.key)}",
                    f"candidate={_json_string(occurrence.candidate)}",
                    f"abbreviation={_json_string(occurrence.abbreviation)}",
                )
            )
        )


def _print_diagnostic(diagnostic: Diagnostic) -> None:
    location = (
        f"{diagnostic.path.as_posix()}:"
        f"{diagnostic.line}:{diagnostic.column}"
    )
    print(
        "\t".join(
            (
                "ERROR",
                f"code={diagnostic.code}",
                f"first={location}",
                f"message={_json_string(diagnostic.message)}",
            )
        )
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="project root (default: script parent repository)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    extract_parser = subparsers.add_parser("extract")
    extract_parser.add_argument("--format", choices=("tsv",), default="tsv")
    subparsers.add_parser("check")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        occurrences = collect_terms(root)
        if args.command == "extract":
            _print_extract(occurrences)
            print(
                f"SUMMARY\tcalls={len(occurrences)}"
                f"\tunique={len(_unique_occurrences(occurrences))}"
            )
            return 0

        mappings = parse_mappings(root)
        aliases = parse_aliases(root)
        diagnostics = audit(occurrences, mappings, aliases)
        diagnostics.extend(
            audit_statistics(
                occurrences,
                expected_calls=EXPECTED_CALLS,
                expected_unique=EXPECTED_UNIQUE_TERMS,
            )
        )
        diagnostics.extend(
            _artifact_diagnostics(root, occurrences, mappings, aliases)
        )
        for diagnostic in diagnostics:
            _print_diagnostic(diagnostic)
        print(
            f"SUMMARY\tcalls={len(occurrences)}"
            f"\tunique={len(_unique_occurrences(occurrences))}"
            f"\tmappings={len(mappings)}"
            f"\taliases={len(aliases)}"
            f"\terrors={len(diagnostics)}"
        )
        return 1 if diagnostics else 0
    except (FileNotFoundError, ScanError, UnicodeError, ValueError) as error:
        print(f"FATAL\tmessage={_json_string(str(error))}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
