# 📚 Project Structure Overview

> 🦰 `verticalnn` is a Python-based project for **reconstructing ocean profiles from sparse measurements** using neural networks.

This project is structured for clean development, testing, documentation, and future packaging.
If you're new to GitHub or Python packaging, here’s your orientation to the repository.


```text
verticalnn/
├── verticalnn/                # [core] Installable Python package
│   ├── __init__.py             # [core] Makes this a Python package
│   ├── config.py               # [core] Constants like pressure grids, hyperparameters
│   ├── data_utils.py           # [core] Data cleaning, NaN handling, normalization
│   ├── io.py                   # [core] Save/load profiles (.npz, .nc)
│   ├── network.py              # [core] Define neural network architectures
│   ├── tools.py                # [core] Pressure-depth conversions, other utilities
│   └── logger.py               # [core] Structured logging (optional)
├── notebooks/                  # [demo] Example Jupyter notebooks
│   ├── 00-prepare-data.ipynb
│   ├── 01-train-first-model.ipynb
│   └── 02-evaluate-results.ipynb
├── models/                     # [output] Trained models and scalers
│   └── v0/
│       ├── model.h5
│       ├── scaler_X.pkl
│       ├── scaler_Y.pkl
│       └── history.json
├── tests/                      # [test] Unit tests using pytest
│   ├── test_data_utils.py
│   ├── test_io.py
│   └── test_network.py
├── docs/                       # [docs] (optional) Documentation site sources (Sphinx)
│   ├── source/
│   └── Makefile
├── pyproject.toml              # [meta] Build system, packaging, linters, test config
├── requirements.txt            # [meta] Runtime requirements
├── requirements-dev.txt        # [meta] Development/testing requirements
├── README.md                    # [meta] Project overview (this file)
├── LICENSE                      # [meta] Open source license (MIT)
├── CITATION.cff                 # [meta] Citation file for GitHub 'Cite this repo'
├── .gitignore                   # [meta] Ignore logs, data, build artifacts
└── .pre-commit-config.yaml      # [style] Pre-commit hooks (optional)
```

---

## 🔰 Highlights

- **Core logic** lives inside the `verticalnn/` package — fully installable.
- **Training notebooks** in `notebooks/` for demos, experiments, and quick testing.
- **Model outputs** saved separately in `models/`.
- **Unit tests** with `pytest` live in `tests/`.
- **Modern packaging** with `pyproject.toml` — ready for PyPI if you wish.
- **Optional documentation** under `docs/`, if you build a Sphinx website later.
- **Pre-commit config** available for linting, formatting, and checking before commits.

---

## 🧰 Development & Testing

- Use `pytest` to run tests:

```bash
pytest
```

- Use `black` and `ruff` for formatting and linting:

```bash
black verticalnn/
ruff verticalnn/
```

- Optionally activate your pre-commit hooks manually:

```bash
pre-commit run --all-files
```

---

## 📝 Documentation

If you build documentation with Sphinx later:

```bash
cd docs
make html
```

or use GitHub Actions to automatically build and deploy.

---

## 🛆 Python Packaging

- Install verticalnn locally (for editable development):

```bash
pip install -e .
```

- Or install runtime dependencies only:

```bash
pip install -r requirements.txt
```

- Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

---

## 📟 Metadata and Citation

- **CITATION.cff** allows automatic "Cite this repository" button on GitHub.
- **LICENSE** is MIT — permissive, allowing reuse with attribution.

