"""Rendering helpers for CI logs and PR comments."""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

from .diff_parser import DiffCoverageSummary


def render_text_table(rows: Sequence[Tuple[str, str]], title: Optional[str] = None) -> str:
    """Render a small, fixed-width table suitable for CI logs."""

    if not rows:
        return "" if title is None else f"{title}\n"

    left_width = max(len(k) for k, _ in rows)
    right_width = max(len(v) for _, v in rows)

    lines: List[str] = []
    if title:
        lines.append(title)

    border = f"+-{'-' * left_width}-+-{'-' * right_width}-+"
    lines.append(border)
    for k, v in rows:
        lines.append(f"| {k.ljust(left_width)} | {v.ljust(right_width)} |")
    lines.append(border)
    return "\n".join(lines) + "\n"


def render_markdown_comment(summary: DiffCoverageSummary, header: str = "Diff coverage") -> str:
    """Build a friendly markdown comment from a DiffCoverageSummary."""

    parts: List[str] = [f"## {header}"]

    if summary.coverage_percent is not None:
        parts.append(f"**Coverage:** {summary.coverage_percent:.2f}%")

    if summary.missing_lines is not None and summary.measured_lines is not None:
        parts.append(f"**Uncovered lines:** {summary.missing_lines} / {summary.measured_lines}")

    parts.append("\n<details><summary>Raw diff-cover output</summary>\n")
    parts.append("\n```\n" + summary.raw.strip() + "\n```\n")
    parts.append("</details>")

    return "\n\n".join(parts).strip() + "\n"

