# DVLA Vehicle Registration DB (mock)

A mock, in-memory vehicle registration database written in Python, with unit tests (pytest) and behaviour-driven tests (pytest-bdd).

## Requirements

- Python 3.12+

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running

```bash
pytest -v                                   # all tests (unit + BDD)
pytest -v --cov=dvla_regdb --cov-report=term-missing   # with coverage
ruff check .                                # lint
ruff format --check .                       # formatting
mypy src tests                              # static type checking (strict)
```

The same checks run in GitHub Actions on every push (`.github/workflows/ci.yml`).

## Project structure

```
src/dvla_regdb/
    vehicle.py        # Vehicle record (frozen dataclass)
    registration.py   # Registration record (frozen dataclass)
    vregistry.py      # VRegistry: store of vehicles, keyed by vehicle ID
    register.py       # VRegister: registration store; owns a VRegistry
    regexcept.py      # Exception hierarchy (VehicleRegisterError base)
tests/                # pytest unit tests
features/             # Gherkin feature files for BDD scenarios
```

## Design decisions

<!-- TODO: explain in your own words, e.g.
- Why frozen dataclasses for records
- Why dict-backed stores (O(1) lookup by ID)
- Why VRegister composes VRegistry
- Exception hierarchy and "lookup raises, search returns empty list"
- Optional vehicle on a registration (Vehicle | None)
-->

## Testing approach

<!-- TODO: unit vs BDD, fixtures, TDD workflow, edge cases covered -->

## Assumptions and limitations

<!-- TODO: e.g. in-memory only, no persistence, registration format validation, ... -->

## Next steps

<!-- TODO: what you would add with more time, e.g. persistence (SQLite), REST API, search -->
