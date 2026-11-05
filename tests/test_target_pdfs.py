import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import fitz

SPEC = importlib.util.spec_from_file_location(
    "target_pdfs", Path(__file__).resolve().parents[1] / "scripts/check_target_pdfs.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TargetPdfTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        for name in ["tex", "figures/00-shared", "fonts", "target", "scripts"]:
            (self.root / name).mkdir(parents=True)
        for name in ["build.sh", ".latexmkrc", ".gitattributes",
                     "scripts/check_target_pdfs.py", "scripts/book_catalog.py", "scripts/publish_volume.py"]:
            (self.root / name).write_text("initial")
        (self.root / "fonts/font.otf").write_bytes(b"fixed font")
        (self.root / "tex/references.bib").write_text(
            "@book{used,title={Used}}\n@book{unused,title={Unused}}\n")
        (self.root / "tex/index-terms").mkdir()
        (self.root / "tex/index-terms/01-first.tex").write_text(
            "\\DeclareBookIndexTerm{使用}{used}\n\\DeclareBookIndexTerm{闲置}{unused}\n")
        catalog = {"volumes": []}
        for number, slug in [(1, "01-first"), (2, "02-second")]:
            catalog["volumes"].append({"number": number, "slug": slug, "title": slug})
            path = self.root / "tex" / slug
            path.mkdir()
            (path / "main.tex").write_text(f"\\input{{tex/{slug}/volume}}")
            (path / "volume.tex").write_text(
                "\\chapter{Source}\\label{chap:%s}\\term{使用}\\cite{used}" % slug)
            document = fitz.open()
            document.new_page()
            document.save(self.root / "target" / f"vol{number}-{slug[3:]}.pdf")
            document.close()
        (self.root / "tex/volumes.json").write_text(json.dumps(catalog))
        self.addCleanup(patch.stopall)
        patch.object(MODULE, "ROOT", self.root).start()
        self.snapshot = self.root / "snapshot.json"
        self.snapshot.write_text(json.dumps(MODULE.inputs()))
        self.run_command("record", "--snapshot", str(self.snapshot))

    def run_command(self, *args):
        with patch("sys.argv", ["check_target_pdfs.py", *args]):
            MODULE.main()

    def changed(self):
        return MODULE.affected(MODULE.inputs(), MODULE.manifest())

    def test_accepts_current_pdfs(self):
        self.run_command("check")

    def test_local_change_only_rebuilds_its_volume(self):
        with (self.root / "tex/01-first/volume.tex").open("a") as stream:
            stream.write(" revised prose")
        self.assertEqual(self.changed(), ["01-first"])
        self.snapshot.write_text(json.dumps(MODULE.inputs()))
        self.run_command("record", "--volume", "01-first", "--snapshot", str(self.snapshot))
        self.run_command("check")

    def test_unused_bibliography_does_not_rebuild_volumes(self):
        source = self.root / "tex/references.bib"
        source.write_text(source.read_text().replace("Unused", "Revised unused"))
        self.assertEqual(self.changed(), [])

    def test_used_bibliography_rebuilds_users(self):
        source = self.root / "tex/references.bib"
        source.write_text(source.read_text().replace("Used", "Revised used"))
        self.assertEqual(self.changed(), ["01-first", "02-second"])

    def test_unused_index_record_does_not_rebuild(self):
        source = self.root / "tex/index-terms/01-first.tex"
        source.write_text(source.read_text().replace("{unused}", "{other unused}"))
        self.assertEqual(self.changed(), [])

    def test_shared_font_rebuilds_all(self):
        (self.root / "fonts/font.otf").write_bytes(b"revised font")
        self.assertEqual(self.changed(), ["01-first", "02-second"])

    def test_moved_reference_changes_referencing_volume(self):
        source = self.root / "tex/02-second/volume.tex"
        source.write_text(source.read_text() + "\\BookChapterRef{chap:01-first}{source}")
        self.snapshot.write_text(json.dumps(MODULE.inputs()))
        self.run_command("record", "--snapshot", str(self.snapshot))
        first = self.root / "tex/01-first/volume.tex"
        first.write_text("\\chapter{Inserted}" + first.read_text())
        self.assertEqual(self.changed(), ["01-first", "02-second"])

    def test_changes_during_build_are_rejected(self):
        (self.root / "tex/01-first/volume.tex").write_text("\\chapter{changed}")
        with self.assertRaisesRegex(ValueError, "构建过程中"):
            self.run_command("record", "--volume", "01-first", "--snapshot", str(self.snapshot))

    def test_extra_or_missing_pdfs_are_rejected(self):
        (self.root / "target/old.pdf").write_bytes(b"%PDF-1.7\n%%EOF\n")
        with self.assertRaisesRegex(ValueError, "不完整"):
            self.run_command("check")

    def test_records_pdf_page_count_without_upper_limit(self):
        path = self.root / "target/vol1-first.pdf"
        document = fitz.open()
        for _ in range(1001):
            document.new_page()
        document.save(path)
        document.close()
        record = MODULE.pdf_record(MODULE.volumes(self.root)[0])
        self.assertEqual(record["pages"], 1001)

    def test_lfs_checks_hash_size_and_attribute(self):
        name = "target/vol1-first.pdf"
        data = (self.root / name).read_bytes()
        pointer = ("version https://git-lfs.github.com/spec/v1\n"
                   f"oid sha256:{MODULE.digest(data)}\nsize {len(data)}\n").encode()
        with patch.object(MODULE, "git", side_effect=[
                pointer, (name + ": filter: lfs\n").encode()]):
            self.assertTrue(MODULE.staged_matches(name, data))
        with patch.object(MODULE, "git", side_effect=[
                pointer, (name + ": filter: unspecified\n").encode()]):
            self.assertFalse(MODULE.staged_matches(name, data))
        with patch.object(MODULE, "git", side_effect=[
                pointer.replace(str(len(data)).encode(), b"1"), (name + ": filter: lfs\n").encode()]):
            self.assertFalse(MODULE.staged_matches(name, data))
