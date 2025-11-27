"""
Institutional relevance filter skeleton.

Real rules (by symbol, sector, competitor graph, legal/reg signals, etc.)
are private. This file only shows a safe placeholder structure.
"""

from typing import Dict, Any

def is_relevant_article(symbol: str, article: Dict[str, Any]) -> bool:
    """
    Minimal placeholder.

    In Real Pipeline, this would:
    - filter SEO spam,
    - discard irrelevant competitor chatter,
    - enforce symbol/entity presence,
    - handle MarketBeat / social / noise sources, etc.
    """
    _ = symbol  
    _ = article
    return True
