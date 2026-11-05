from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from render_labels import render
render(Path(__file__).resolve().parent.name)
