# Python FastAPI template.

FastAPI boilerplate project


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
    │   ├── db                              # Database module
    │   │   ├── models                      # Database models
    │   │   ├── repositories                # Database repositoiries
    │   │   ├── connections.py              # App database connectors
    │   │   └── postgres.py                 # Postgres connections
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
        ├── utils                           # Utils for testing
        │   └── db.py                       # Database utils
        ├── conftest.py                     # Pytest configuration
        └── test_api.py                     # API tests
```


# Initialization.
At first you should to initialize a project.
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
