#!/usr/bin/env python3
"""Publish a successfully compiled watched volume and its input snapshot."""
import shutil
import subprocess
import sys
from book_catalog import ROOT, volumes

slug = sys.argv[1]
volume = next(v for v in volumes() if v["slug"] == slug)
destination = ROOT / "target" / volume["pdf"]
destination.parent.mkdir(exist_ok=True)
temporary = destination.with_suffix(".pdf.tmp")
shutil.copyfile(ROOT / "build" / (slug + ".pdf"), temporary)
temporary.replace(destination)
subprocess.run([sys.executable, "scripts/check_target_pdfs.py", "record",
                "--volume", slug, "--snapshot", "build/" + slug + "-inputs.json"],
               cwd=ROOT, check=True)
