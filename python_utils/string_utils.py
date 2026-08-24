"""String manipulation helpers."""

import re

_CAMEL_BOUNDARY = re.compile(r"[_-]|(?<=[a-z0-9])(?=[A-Z])")


def slugify(text: str, sep: str = "-") -> str:
    """Convert arbitrary text to a URL-friendly slug."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", sep, text)
    return text.strip(sep)


def truncate(text: str, max_len: int = 80, suffix: str = "...") -> str:
    """Truncate text to max_len, adding a suffix when cut."""
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)].rstrip() + suffix


def to_snake_case(text: str) -> str:
    """Convert CamelCase / kebab-case to snake_case."""
    parts = [p for p in _CAMEL_BOUNDARY.split(text) if p]
    return "_".join(p.lower() for p in parts)


def to_camel_case(text: str, upper: bool = True) -> str:
    """Convert snake_case / kebab-case to (Upper)CamelCase."""
    parts = [p for p in _CAMEL_BOUNDARY.split(text) if p]
    first = parts[0].capitalize() if upper else parts[0].lower()
    rest = [p.capitalize() for p in parts[1:]]
    return "".join([first, *rest])
