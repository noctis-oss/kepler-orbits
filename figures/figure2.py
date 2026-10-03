"""Figure 2: the orbit for a = 1 and four eccentricities."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # write a file; never open a window
import matplotlib.pyplot as plt
import numpy as np

A = 1.0
theta = np.linspace(0.0, 2.0*np.pi, 721)

fig, ax = plt.subplots(figsize=(4.8, 3.4))
for e in (0.0, 0.3, 0.6, 0.8):
    r = A*(1.0 - e**2) / (1.0 + e*np.cos(theta))
    ax.plot(r*np.cos(theta), r*np.sin(theta), label=f"$e={e}$")
ax.plot(0.0, 0.0, "k+")
ax.set_aspect("equal")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(loc="upper right", fontsize="small")
fig.savefig(Path(__file__).with_suffix(".pdf"), bbox_inches="tight",
            metadata={"CreationDate": None})  # same bytes on every run
