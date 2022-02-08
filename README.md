# Python template.

Python boilerplate project


# Project structure.
```
├── CHANGELOG.md                            # Changelogs
├── README.md                               # Current file
├── deploy                                  # Deploy configurations
├── docs                                    # Documentation
├── pyproject.toml                          # Project configuration
├── setup.cfg                               # Libraries configuration
└── src                                     # Source files
    ├── app                                 # Main application
    │   ├── constants.py                    # App constants
    │   ├── main.py                         # App entrypoint
    │   ├── manage.py                       # CLI-utility
    │   ├── routes                          # API routes
    │   │   ├── dependencies                # API dependencies
    │   │   └── base.py                     # Base endpoints
    │   ├── schemas                         # App schemas
    │   │   └── base.py                     # Base schemas
    │   └── settings                        # App settings
    │       └── base.py                     # Base settings
    ├── conftest.py                         # Pytest entrypoint
    ├── tasks                               # Periodical tasks
    └── tests                               # Tests
        └── test_api.py                     # API tests
```


# Installation.
```
poetry install
poetry run pre-commit install
```


# Run tests.
```
poetry run pytest
```


# Run code analysis.
```
poetry run pre-commit run --all-files
```
