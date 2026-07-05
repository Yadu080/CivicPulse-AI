# CivicPulse AI — Project Description

## One-liner
**CivicPulse AI turns raw community data into decisions** — ask questions in plain
English and get patterns, anomalies, and a ready-to-send action memo, powered by a
low-cost Gemini model on Google Cloud Run.

## Short description (for submission form)
Cities and community teams sit on spreadsheets of complaints and service requests
but struggle to answer the only question that matters: *what should we do next?*
CivicPulse AI is a decision-intelligence dashboard that computes real analytics
(trends, hotspots, anomalies) in Python, then uses Gemini to explain them and
generate concrete, assignable recommendations. It ships with a Decision Scoreboard
(urgency · impact · confidence) and a one-click Executive Brief. Because analytics
run deterministically before any AI call, the model never invents numbers — and the
whole thing runs cheaply on Cloud Run with scale-to-zero.

## Theme
AI for Better Living and Smarter Communities.

## Domain framing
Community Services + Citizen Complaints + Local Resource Prioritization.

## Problem
- Local governments collect complaint/service data but lack time and tools to analyze it.
- Generic AI chatbots hallucinate numbers and don't map to real decisions.
- Off-the-shelf BI tools are expensive, slow to set up, and not decision-oriented.

## Solution
A focused dashboard that is **deterministic-first, AI-explained**:
1. Ingest CSV/JSON/PDF/text with forgiving column mapping.
2. Compute counts, weekly trends, severity mix, and anomaly flags in Python.
3. Feed those facts to Gemini for plain-language explanation + recommended actions.
4. Present a Community Snapshot, Decision Scoreboard, Anomalies, and an Executive Brief.

## Why it wins
- **Unique positioning:** decision intelligence, not a chatbot.
- **Trustworthy:** grounded outputs, explainability panel, no hallucinated stats.
- **Low cost:** flash-lite model, one call per action, scale-to-zero Cloud Run.
- **Judge-friendly:** the whole value is clear in under 3 minutes.

## Google Cloud + Gemini
- Gemini `gemini-2.5-flash-lite` via Vertex AI or Gemini API.
- Cloud Run (serverless), Cloud Build, Artifact Registry.
- Deployed and managed entirely through the `gcloud` CLI.
