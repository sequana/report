"""sequana_report: Shared HTML report generation infrastructure for Sequana.

Provides base classes, templates, and utilities for generating HTML reports
across the Sequana ecosystem (sequana core + pipelines).
"""

from . import config
from .base_module import SequanaBaseModule

__version__ = config.__version__

__all__ = [
    "SequanaBaseModule",
    "config",
]
