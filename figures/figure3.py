"""Figure 3: the numerical orbit, read from kepler_orbit.csv."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write a file; never open a window
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent

with (ROOT/"kepler_orbit.csv").open(newline="") as source:
    rows = list(csv.DictReader(source))
x = [float(row["x"]) for row in rows]
y = [float(row["y"]) for row in rows]

fig, ax = plt.subplots(figsize=(4.8, 3.4))
ax.plot(x, y, color="tab:orange")
ax.plot(0.0, 0.0, "k+")
ax.set_aspect("equal")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight",
            metadata={"CreationDate": None})  # same bytes on every run
