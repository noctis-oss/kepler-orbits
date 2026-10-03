"""Check the prepared orbit data without requiring Python editing."""
import csv
from pathlib import Path
import math

root = Path(__file__).resolve().parent
with (root / "kepler_orbit.csv").open() as source:
    rows = list(csv.DictReader(source))
assert len(rows) == 721, "Expected 721 orbit samples; regenerate the data."
radii = [math.hypot(float(r["x"]), float(r["y"])) for r in rows]
assert abs(min(radii) - 0.4) < 1e-5, "Unexpected minimum radius."
assert abs(max(radii) - 1.6) < 1e-5, "Unexpected maximum radius."
print("PASS: 721 samples; radius from 0.4 to 1.6.")
