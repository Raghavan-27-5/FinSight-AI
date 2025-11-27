"""
Public pipeline interface for FinSight AI (skeleton).

This exposes a minimal, stable API surface for:
- loading cached data
- processing articles
- computing placeholder sentiment and DSP
"""

from .loader import load_cached_articles
from .processor import process_articles
from .sentiment import score_article_sentiment
from .dsp import calculate_institutional_dsp
