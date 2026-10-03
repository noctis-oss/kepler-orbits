"""Figure 4: the analytical orbit and the RK4 trajectory, one on the other."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write a file; never open a window
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent

A, E = 1.0, 0.6
theta = np.linspace(0.0, 2.0*np.pi, 721)
r = A*(1.0 - E**2) / (1.0 + E*np.cos(theta))
with (ROOT/"kepler_orbit.csv").open(newline="") as source:
    rows = list(csv.DictReader(source))

fig, ax = plt.subplots(figsize=(5.6, 3.6))
ax.plot(r*np.cos(theta), r*np.sin(theta), color="tab:blue", linewidth=1.8,
        label="Analytical")
ax.plot([float(row["x"]) for row in rows], [float(row["y"]) for row in rows],
        color="tab:orange", linewidth=1.3, linestyle="--", label="Numerical RK4")
ax.set_aspect("equal")
ax.grid(True)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(loc="upper right")
fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight",
            metadata={"CreationDate": None})  # same bytes on every run
