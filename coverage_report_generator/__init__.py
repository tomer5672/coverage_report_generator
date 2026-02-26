"""Coverage report helper package.

This package intentionally contains a few small, decoupled utilities to make it easy
to import and reuse pieces from scripts or CI jobs.
"""

from .diff_parser import DiffCoverageSummary, parse_diff_cover_markdown
from .reporting import render_markdown_comment, render_text_table
from .io_utils import read_text, write_text, ensure_parent_dir

__all__ = [
    "DiffCoverageSummary",
    "parse_diff_cover_markdown",
    "render_markdown_comment",
    "render_text_table",
    "read_text",
    "write_text",
    "ensure_parent_dir",
]

