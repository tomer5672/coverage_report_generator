"""Tiny IO helpers.

These wrappers make it easier to mock IO in the future, but they're also handy
for keeping scripts small and readable.
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

PathLike = Union[str, Path]


def ensure_parent_dir(path: PathLike) -> Path:
    p = Path(path)
    if p.parent and not p.parent.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
    return p


def read_text(path: PathLike, encoding: str = "utf-8") -> str:
    return Path(path).read_text(encoding=encoding)


def write_text(path: PathLike, text: str, encoding: str = "utf-8") -> None:
    p = ensure_parent_dir(path)
    p.write_text(text, encoding=encoding)

