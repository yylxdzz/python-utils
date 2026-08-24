"""File system helpers."""

import os
import tempfile
from pathlib import Path
from typing import Union

PathLike = Union[str, os.PathLike]


def ensure_dir(path: PathLike) -> Path:
    """Create directory (and parents) if missing. Returns the Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def read_text(path: PathLike, encoding: str = "utf-8") -> str:
    """Read a text file with a clear error on failure."""
    return Path(path).read_text(encoding=encoding)


def atomic_write(path: PathLike, content: str, encoding: str = "utf-8") -> None:
    """Write text atomically: write to temp file then rename, avoiding partial writes."""
    p = Path(path)
    ensure_dir(p.parent)
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), prefix=p.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(content)
        os.replace(tmp, p)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
