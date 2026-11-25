"""Configuration Sphinx de my-arithmetic-nylphen."""

import os
import sys
from importlib.metadata import PackageNotFoundError, version as pkg_version

# Permet à autodoc d'importer le paquet même s'il n'est pas installé
sys.path.insert(0, os.path.abspath("../src"))

project = "my-arithmetic-nylphen"
author = "NylphenGoat"
copyright = "2026, NylphenGoat"

try:
    release = pkg_version("my-arithmetic-nylphen")
except PackageNotFoundError:
    release = "0.0"
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
]

# Napoleon : docstrings au format numpy uniquement
napoleon_google_docstring = False
napoleon_numpy_docstring = True

autodoc_typehints = "description"
autodoc_member_order = "bysource"

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

language = "fr"
templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "sphinx_rtd_theme"

# Rend pgcd disponible dans les exemples des docstrings testés par doctest
doctest_global_setup = "from my_arithmetic_nylphen import pgcd"
