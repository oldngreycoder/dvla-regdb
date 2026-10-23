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
registration and vehicle are frozen data classes
Register and vehicles registry are hsoted in separate classes , the vehicle registry being encapsulated into the register
demo.py provides a sample run through of how the code will should be used

## Testing approach
unit tests for each class method
unit tests for possible anomalies that could occur
BDD test cases to test features as specified in the requirements

## Assumptions and limitations
As specified in the requirements no persistance or user interface developed

## Next steps
Interview discussion

## GAI disclosure
Whereas I've written many python scripts before, these were adhoc. For this work I wanted to learn how to create
production ready python and to use python tooling such as pylance, ruff, mypy.
claude was used to create the VSCODE config and the project scaffolding such as CI/CD, .gitignore and pyrproject.toml
provided code reviews and knowledge regards pytest-bdd
soloution classes, features, unit tests, BDD feature file and steps, the demo and the test_demo - including sample data were created by myself.
