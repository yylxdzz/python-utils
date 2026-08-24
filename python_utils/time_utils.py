"""Date / time helpers."""

from datetime import datetime, timedelta
from typing import Optional


def format_iso(dt: Optional[datetime] = None) -> str:
    """Return ISO 8601 string. Defaults to now (naive, local)."""
    return (dt or datetime.now()).isoformat(timespec="seconds")


def humanize_duration(seconds: int) -> str:
    """Convert seconds to a compact human readable duration."""
    if seconds < 60:
        return f"{seconds}s"
    minutes, sec = divmod(int(seconds), 60)
    if minutes < 60:
        return f"{minutes}m {sec}s"
    hours, minute = divmod(minutes, 60)
    return f"{hours}h {minute}m"


def date_range(start: datetime, end: datetime, step_days: int = 1):
    """Yield dates from start to end (inclusive) by step_days."""
    cur = start
    while cur <= end:
        yield cur
        cur += timedelta(days=step_days)
