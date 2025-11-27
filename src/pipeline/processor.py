"""
Article normalization, basic shaping, and safe placeholder relevance tagging.

All proprietary relevance logic is removed. This only demonstrates structure.
"""

from typing import List, Dict, Any

def normalize_article(raw: Dict[str, Any]) -> Dict[str, Any]:
    """
    Basic structural normalization of a single article. No alpha here.
    """
    return {
        "symbol": raw.get("symbol"),
        "headline": raw.get("headline", "").strip(),
        "source": raw.get("source", "").strip(),
        "published": raw.get("published"),
        "body": raw.get("body", ""),
        "entities": raw.get("entities", {}),
        "engagement": raw.get("engagement", 0),
        "form_type": raw.get("form_type"),# e.g. 10-K, 13D, etc.
        "is_relevant": True, # real filter redacted
    }


def process_articles(raw_articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Apply normalization to a batch of raw articles.
    Real relevance filters are intentionally removed here.
    """
    return [normalize_article(a) for a in raw_articles]
