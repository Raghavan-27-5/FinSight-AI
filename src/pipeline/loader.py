
from typing import List, Dict, Any
import json
import os

DEFAULT_CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "cached")

def load_cached_articles(symbol: str, cache_dir: str = DEFAULT_CACHE_DIR) -> List[Dict[str, Any]]:
    """
    Load cached articles for a symbol from a JSON or DB in `cache_dir`.
    This is intentionally minimal and file-format agnostic.
    """
    symbol = symbol.upper().strip()
    fname = f"{symbol}_articles.json"
    path = os.path.join(cache_dir, fname)

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception:
            data = []
    if isinstance(data, dict):
        return [data]
    return data
