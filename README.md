FinSight AI — Institutional-Grade Sentiment & DSP Engine (Open Skeleton)

Config-driven, source-weighted, relevance-filtered news intelligence.

FinSight AI is a modular sentiment engine built for institutional signal research.
This public repo contains the full architecture, entire pipeline skeleton, and clean mock data, while all proprietary weighting logic and alpha formulas remain private.

This project demonstrates how to build a real-world research system with:

Source-weighted sentiment extraction

Entity-level NLP parsing

Relevance filtering (sector → competitor → fundamental)

Direction–Magnitude–Weight DSP scoring

Time-decayed weighting

EDGAR/NSE/BSE form-type boosts

Safe clamps + anti-noise logic

Async multi-source news ingestion

SQLite caching layer

Transparent reporting interface

⚠️ The core alpha math is intentionally redacted.
This repo shows how the system is built, not the proprietary signal logic.

1. Project Structure
FinSight-AI/
│
├── config/
│   ├── config.py
│   └── base_weights.json
│
├── pipeline/
│   ├── fetchers.py
│   ├── models.py
│   ├── nlp_utils.py
│   ├── dsp_engine.py
│   └── pipeline.py
│
├── examples/
│   ├── AAPL_report.json
│   ├── TSLA_report.json
│   ├── TATAMOTORS_report.json
│
├── tests/
│   ├── test_relevance.py
│   ├── test_weighting.py
│   └── test_dsp.py
│
├── data/ (empty placeholder)
│
├── README.md
└── requirements.txt

2. What This System Does (High-Level)

FinSight AI ingests news from multiple sources, parses entities, assigns dynamic weights, filters irrelevant noise, and computes a Directional Sentiment Pressure (DSP) score.

DSP = direction × magnitude × weight, aggregated and L2-normalized.

Key properties:

Signal-first design (no SEO spam, no marketbeat noise, no irrelevant chatter)

Institutional recency decay with half-life weighting

SEC/EDGAR form-type adjustments

Bearish-asymmetric scoring (market moves faster on negative news)

Aspect-level sentiment (earnings, competition, margins, tech, regulatory, etc.)

Transparent reporting similar to professional research systems

3. What Is Included in This Public Repo

This repo includes:

Full pipeline structure

Complete relevance filtering rules

Complete entity/NLP parsing logic

Test suite for reproducibility

Configuration-driven source weighting framework


4. What Is NOT Included (Proprietary / Redacted)

Not included:

❌ Real-time API keys
❌ Dynamic institutional weighting math
❌ Proprietary alpha functions
❌ Direction–Magnitude tuning hyperparameters
❌ Market microstructure logic
❌ Position sizing & trading rules
❌ Live NLP model weights

6. Installation
git clone https://github.com/<Raghavan-27-5>/FinSight-AI
cd FinSight-AI
pip install -r requirements.txt
streamlit run app/streamlit_app.py

7. Contact

For collaboration or hiring:

LinkedIn: <https://www.linkedin.com/in/raghavan-m-820732367>
Email: <raghavan27052005@gmail.com>
