"""Base application constants."""

from pathlib import Path


# Directories
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent.parent
DOCS_DIR = ROOT_DIR / "docs"
TEST_DIR = ROOT_DIR / "tests"
