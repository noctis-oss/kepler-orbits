# Keplerian orbits

A short paper comparing the analytical Keplerian orbit with a numerical
integration. `main.tex` is the source of the paper.

## Reproduce

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements-lock.txt
    python generate_kepler_data.py
    python check_data.py
    python build_figures.py
    latexmk main.tex

`generate_kepler_data.py` uses only the standard library and writes the
three CSV files. Each script in `figures/` draws one figure from a
formula or from those files. The paper is `build/main.pdf`.
