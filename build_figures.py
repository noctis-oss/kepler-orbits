"""Run the figure scripts present in this revision. No Git operations."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
scripts = sorted((root / "figures").glob("figure[1-6].py"))
if not scripts:
    sys.exit("No figure scripts yet. Add the files for the current stage first.")
for script in scripts:
    print(f"Building {script.name}", flush=True)
    subprocess.run([sys.executable, str(script)], cwd=root, check=True)
print(f"Built {len(scripts)} figures.")
