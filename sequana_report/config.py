"""Configuration for sequana_report package.

Manages asset paths (CSS, JS, templates) and report output settings.
"""

import os
from pathlib import Path

# Package directory
PACKAGE_DIR = Path(__file__).parent

# Resource directories
RESOURCES_DIR = PACKAGE_DIR / "resources"
CSS_DIR = RESOURCES_DIR / "css"
JS_DIR = RESOURCES_DIR / "js"
IMAGES_DIR = RESOURCES_DIR / "images"
TEMPLATES_DIR = RESOURCES_DIR / "templates"

# Build CSS/JS lists
css_list = sorted([str(f) for f in CSS_DIR.glob("*.css")])
js_list = sorted([str(f) for f in JS_DIR.glob("*.js")])

# Logo path (from sequana resources or default)
try:
    logo = str(IMAGES_DIR / "sequana_logo.png")
except Exception:
    logo = None

# Version (read from pyproject.toml or package metadata)
try:
    from importlib.metadata import version

    __version__ = version("sequana_report")
except Exception:
    __version__ = "0.1.0"

# Output directory and sample name (can be overridden per-report)
output_dir = "./"
sample_name = "sample"
