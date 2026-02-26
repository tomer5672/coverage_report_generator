"""Parsing utilities for diff-cover outputs.

`diff-cover` can emit a Markdown report. This module extracts a small summary
from that markdown so it can be posted as a PR comment or printed in CI logs.

The parser is intentionally tolerant: it uses a couple of regex heuristics rather
than depending on a strict markdown schema.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable, Optional


@dataclass(frozen=True)
class DiffCoverageSummary:
    """A compact summary of diff coverage."""

    coverage_percent: Optional[float]
    missing_lines: Optional[int]
    measured_lines: Optional[int]
    raw: str


_PERCENT_RE = re.compile(r"(?P<pct>\d+(?:\.\d+)?)\s*%")
_LINES_RE = re.compile(
    r"(?P<missing>\d+)\s*(?:missing|uncovered)\s*.*?out\s+of\s+(?P<measured>\d+)",
    re.IGNORECASE,
)


def _first_match(pattern: re.Pattern, lines: Iterable[str]) -> Optional[re.Match]:
    for line in lines:
        m = pattern.search(line)
        if m:
            return m
    return None


def parse_diff_cover_markdown(markdown_text: str) -> DiffCoverageSummary:
    """Parse a `diff-cover` markdown report and return a summary.

    Args:
        markdown_text: The content of the markdown report.

    Returns:
        DiffCoverageSummary with best-effort extracted fields.
    """

    lines = markdown_text.splitlines()

    pct_match = _first_match(_PERCENT_RE, lines)
    lines_match = _first_match(_LINES_RE, lines)

    coverage_percent: Optional[float] = None
    if pct_match:
        try:
            coverage_percent = float(pct_match.group("pct"))
        except ValueError:
            coverage_percent = None

    missing_lines: Optional[int] = None
    measured_lines: Optional[int] = None
    if lines_match:
        try:
            missing_lines = int(lines_match.group("missing"))
            measured_lines = int(lines_match.group("measured"))
        except ValueError:
            missing_lines = None
            measured_lines = None

    return DiffCoverageSummary(
        coverage_percent=coverage_percent,
        missing_lines=missing_lines,
        measured_lines=measured_lines,
        raw=markdown_text,
    )

