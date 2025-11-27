"""
Basic string normalization utilities (non-proprietary).
"""
import re
def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()

def to_lower(text: str) -> str:
    return (text or "").lower()
