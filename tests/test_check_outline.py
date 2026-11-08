from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_outline.py"
SPEC = importlib.util.spec_from_file_location("check_outline", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OutlineHierarchyTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.outline = self.root / "plans/ten-volume-migration"
        self.part_file = "01-example/01-outline.md"
        self.part = self.outline / self.part_file
        self.part.parent.mkdir(parents=True)
        (self.root / "scripts/outline").mkdir(parents=True)
        (self.root / "outlines").mkdir()

    def check(self, headings, chapters=(("1.1", "第一章"),)):
        """Exercise the public checker against a complete, isolated plan."""
        manifest = [{
            "volume": "示例卷",
            "chapter_count": len(chapters),
            "parts": [{
                "file": self.part_file,
                "chapters": [
                    {"number": number, "title": title}
                    for number, title in chapters
                ],
            }],
        }]
        (self.root / "scripts/outline/math-ten-part-files-manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
        )
        self.part.write_text(
            "\n\n".join(f"{heading}\n\n{body}" for heading, body in headings),
            encoding="utf-8",
        )
        (self.outline / "README.md").write_text(
            f"[示例部分]({self.part_file})\n\n"
            + "\n\n".join(f"#### {number} {title}" for number, title in chapters),
            encoding="utf-8",
        )
        return MODULE.check(root=self.root)

    def report(self, *headings, chapters=(("1.1", "第一章"),)):
        return self.check(
            [(heading, "说明这一项的具体内容。") for heading in headings], chapters
        )

    def assert_valid(self, report):
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["warnings"], [])

    def test_accepts_legacy_structure_without_subsubsections(self):
        report = self.report(
            "## 1.1 第一章",
            "### 1.1.1 第一节",
            "#### 1.1.1.1 第一小节",
            "### 1.1.2 本章小结",
        )
        self.assert_valid(report)
        self.assertEqual(report["counts"], {
            "volumes": 1, "parts": 1, "chapters": 1,
            "sections": 2, "subsections": 1, "subsubsections": 0,
        })
        self.assertEqual(report["local_links_checked"], 1)

    def test_accepts_and_counts_subsubsections(self):
        report = self.report(
            "## 1.1 第一章",
            "### 1.1.1 第一节",
            "#### 1.1.1.1 第一小节",
            "##### 1.1.1.1.1 第一子项",
            "##### 1.1.1.1.2 第二子项",
            "### 1.1.2 本章小结",
        )
        self.assert_valid(report)
        self.assertEqual(report["counts"]["subsubsections"], 2)

    def test_resets_descendant_counts_for_each_parent(self):
        report = self.report(
            "## 1.1 第一章",
            "### 1.1.1 第一节",
            "#### 1.1.1.1 第一小节",
            "##### 1.1.1.1.1 第一子项",
            "##### 1.1.1.1.2 第二子项",
            "#### 1.1.1.2 第二小节",
            "##### 1.1.1.2.1 重新计数",
            "### 1.1.2 第二节",
            "#### 1.1.2.1 重新计数",
            "##### 1.1.2.1.1 重新计数",
            "### 1.1.3 本章小结",
            "## 1.2 第二章",
            "### 1.2.1 第一节",
            "#### 1.2.1.1 重新计数",
            "##### 1.2.1.1.1 重新计数",
            "### 1.2.2 本章小结",
            chapters=(("1.1", "第一章"), ("1.2", "第二章")),
        )
        self.assert_valid(report)
        self.assertEqual(report["counts"], {
            "volumes": 1, "parts": 1, "chapters": 2,
            "sections": 5, "subsections": 4, "subsubsections": 5,
        })

    def test_rejects_wrong_skipped_or_duplicate_subsubsection_numbers(self):
        cases = {
            "first number skipped": ("1.1.1.1.2",),
            "wrong chapter": ("1.2.1.1.1",),
            "wrong section": ("1.1.2.1.1",),
            "wrong subsection": ("1.1.1.2.1",),
            "skipped number": ("1.1.1.1.1", "1.1.1.1.3"),
            "duplicate number": ("1.1.1.1.1", "1.1.1.1.1"),
        }
        for name, numbers in cases.items():
            with self.subTest(name=name):
                report = self.report(
                    "## 1.1 第一章",
                    "### 1.1.1 第一节",
                    "#### 1.1.1.1 第一小节",
                    *(f"##### {number} 子项" for number in numbers),
                    "### 1.1.2 本章小结",
                )
                self.assertTrue(any(
                    error.startswith("Subsubsection numbering:")
                    for error in report["errors"]
                ), report)

    def test_rejects_subsubsection_without_parent_subsection(self):
        cases = {
            "no section": (
                "## 1.1 第一章",
                "##### 1.1.0.0.1 孤立子项",
                "### 1.1.1 本章小结",
            ),
            "no subsection": (
                "## 1.1 第一章",
                "### 1.1.1 第一节",
                "##### 1.1.1.0.1 孤立子项",
                "### 1.1.2 本章小结",
            ),
            "parent belongs to previous section": (
                "## 1.1 第一章",
                "### 1.1.1 第一节",
                "#### 1.1.1.1 第一小节",
                "##### 1.1.1.1.1 合法子项",
                "### 1.1.2 第二节",
                "##### 1.1.2.0.1 孤立子项",
                "### 1.1.3 本章小结",
            ),
        }
        for name, headings in cases.items():
            with self.subTest(name=name):
                report = self.report(*headings)
                self.assertTrue(any(
                    error.startswith("Subsubsection missing parent subsection:")
                    for error in report["errors"]
                ), report)

    def test_rejects_subsection_without_parent_section(self):
        report = self.report(
            "## 1.1 第一章",
            "#### 1.1.0.1 孤立小节",
            "### 1.1.1 本章小结",
        )
        self.assertTrue(any(
            error.startswith("Subsection missing parent section:")
            for error in report["errors"]
        ), report)

    def test_rejects_depth_six(self):
        report = self.report(
            "## 1.1 第一章",
            "### 1.1.1 第一节",
            "#### 1.1.1.1 第一小节",
            "##### 1.1.1.1.1 合法子项",
            "###### 1.1.1.1.1.1 过深子项",
            "### 1.1.2 本章小结",
        )
        self.assertTrue(any(
            error.startswith("Unexpected heading depth:")
            for error in report["errors"]
        ), report)

    def test_checks_subsubsection_overview(self):
        for body in ("", "第一句。第二句。第三句。"):
            with self.subTest(body=body):
                report = self.check([
                    ("## 1.1 第一章", "说明本章内容。"),
                    ("### 1.1.1 第一节", "说明本节内容。"),
                    ("#### 1.1.1.1 第一小节", "说明小节内容。"),
                    ("##### 1.1.1.1.1 子项", body),
                    ("### 1.1.2 本章小结", "总结本章内容。"),
                ])
                self.assertTrue(any(
                    "Overview requires 1–2 sentences" in error
                    and "1.1.1.1.1" in error
                    for error in report["errors"]
                ), report)
                if not body:
                    self.assertTrue(any(
                        "Empty outline item" in error for error in report["errors"]
                    ), report)


if __name__ == "__main__":
    unittest.main()
