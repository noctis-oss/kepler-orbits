"""Figure 1: the analytical orbit r = a(1 - e^2) / (1 + e cos(theta))."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write a file; never open a window
import matplotlib.pyplot as plt
import numpy as np

A, E = 1.0, 0.6
theta = np.linspace(0.0, 2.0*np.pi, 721)
r = A*(1.0 - E**2) / (1.0 + E*np.cos(theta))

fig, ax = plt.subplots(figsize=(4.8, 3.4))
ax.plot(r*np.cos(theta), r*np.sin(theta), color="tab:blue")
ax.plot(0.0, 0.0, "k+")  # the central body, at a focus
ax.set_aspect("equal")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight",
            metadata={"CreationDate": None})  # same bytes on every run
