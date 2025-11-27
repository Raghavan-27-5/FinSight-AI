"""
High-level orchestration for the FinSight AI public skeleton.
"""

from typing import Dict, Any
import pandas as pd

from .loader import load_cached_articles
from .processor import process_articles
from .sentiment import score_article_sentiment
from .weighting import compute_dynamic_weight
from .dsp import calculate_institutional_dsp
from .relevance import is_relevant_article


def run_cached_pipeline(symbol: str) -> Dict[str, Any]:
    raw = load_cached_articles(symbol)
    processed = process_articles(raw)
    # attach sentiment, weight, relevance
    enriched = []
    for art in processed:
        sent = score_article_sentiment(art)
        art.update(sent)
        art["weight"] = compute_dynamic_weight(
            source=art.get("source"),
            published=art.get("published"),
            engagement=art.get("engagement", 0),
            form_type=art.get("form_type"),
        )
        art["is_relevant"] = is_relevant_article(symbol, art)
        enriched.append(art)

    df = pd.DataFrame(enriched)
    if not df.empty:
        df_relevant = df[df["is_relevant"] == True].copy()
    else:
        df_relevant = df.copy()

    dsp = calculate_institutional_dsp(df_relevant)

    return {
        "symbol": symbol.upper(),
        "dsp": float(dsp),
        "article_count": int(len(df_relevant)),
        "df": df_relevant,
    }
