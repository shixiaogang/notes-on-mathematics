#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_root="$(mktemp -d "${TMPDIR:-/tmp}/book-clean.XXXXXX")"
trap 'rm -rf "$fixture_root"' EXIT

cp "$project_root/build.sh" "$fixture_root/build.sh"
chmod +x "$fixture_root/build.sh"

mkdir -p \
  "$fixture_root/fake-bin" \
  "$fixture_root/target" \
  "$fixture_root/build/nested/test-cache" \
  "$fixture_root/build/.hidden-cache/deeper"
printf '#!/usr/bin/env bash\nexit 0\n' > "$fixture_root/fake-bin/latexmk"
chmod +x "$fixture_root/fake-bin/latexmk"

: > "$fixture_root/target/mathematics-notes.pdf"
: > "$fixture_root/build/main.bbl"
: > "$fixture_root/build/ordinary.cache"
: > "$fixture_root/build/.hidden-file"
: > "$fixture_root/build/nested/test-cache/result.aux"
: > "$fixture_root/build/.hidden-cache/deeper/result.idx"

PATH="$fixture_root/fake-bin:/usr/bin:/bin" \
  bash "$fixture_root/build.sh" clean

if [[ -e "$fixture_root/build" || -e "$fixture_root/target" ]]; then
  printf 'clean 回归测试失败：临时项目的 build/ 或 target/ 仍然存在。\n' >&2
  find "$fixture_root/build" -mindepth 1 -print >&2
  exit 1
fi

printf 'clean 回归测试通过：临时项目的 build/ 和 target/ 已完整删除。\n'
