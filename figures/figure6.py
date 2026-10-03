"""Figure 6: reference, perturbed and first-order (linearized) orbits."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write a file; never open a window
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent

with (ROOT/"kepler_variation.csv").open(newline="") as source:
    rows = list(csv.DictReader(source))

def column(name):
    return [float(row[name]) for row in rows]

fig, ax = plt.subplots(figsize=(4.8, 3.4))
ax.plot(column("x_reference"), column("y_reference"), color="tab:blue",
        label="Reference")
ax.plot(column("x_perturbed"), column("y_perturbed"), color="tab:red",
        label="Perturbed")
ax.plot(column("x_linearized"), column("y_linearized"), color="tab:green",
        linestyle="--", label="First-order prediction")
ax.set_aspect("equal")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(loc="upper right", fontsize="small")
fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight",
            metadata={"CreationDate": None})  # same bytes on every run
