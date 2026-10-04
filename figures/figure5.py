"""Figure 5: Kepler's third law, T^2 against a^3, from kepler_third_law.csv."""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write a file; never open a window
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent

MU = 1.0
with (ROOT/"kepler_third_law.csv").open(newline="") as source:
    rows = list(csv.DictReader(source))
a_cubed = np.linspace(0.0, 8.5, 2)

fig, ax = plt.subplots(figsize=(4.8, 3.4))
ax.plot(a_cubed, 4.0*np.pi**2*a_cubed/MU, color="tab:blue",
        label=r"$T^2=4\pi^2a^3/\mu$")
ax.plot([float(row["a_cubed"]) for row in rows],
        [float(row["T_squared"]) for row in rows], "o", color="tab:orange",
        label="kepler_third_law.csv")
ax.set_xlabel("$a^3$")
ax.set_ylabel("$T^2$")
ax.legend(loc="upper left", fontsize="small")
fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight",
            metadata={"CreationDate": None})  # same bytes on every run
