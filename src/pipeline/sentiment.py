"""
Placeholder sentiment scoring.

In Real Pipeline, this would call an LLM / classifier / transformer. Here I
only provide a stable interface and always return neutral sentiment.
"""

from typing import Dict, Any


def score_article_sentiment(article: Dict[str, Any]) -> Dict[str, Any]:
    """
    Assign placeholder sentiment. Real model logic is private.
    """
    return {
        "sentiment_score": 0.0, 
        "aspect_sentiment": {}, # aspect → score mapping redacted
    }
