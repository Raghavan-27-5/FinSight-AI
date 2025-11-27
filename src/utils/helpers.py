"""
Misc helper functions used across the skeleton repo.
"""
from typing import Any

def safe_get(d: dict, key: str, default: Any = None) -> Any:
    if d is None:
        return default
    return d.get(key, default)
