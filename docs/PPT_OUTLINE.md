# CivicPulse AI — 6-Slide Pitch Deck Outline

Keep it visual: one big idea per slide, minimal text, screenshots where possible.
Suggested tools: Google Slides / Canva. Brand colors: teal `#0e7490`, blue `#1d4ed8`.

---

## Slide 1 — Title / Problem statement
**Title:** CivicPulse AI — *Not just answers, better decisions.*
**Subtitle:** Community decision intelligence, powered by Gemini on Google Cloud.
- Cities collect thousands of complaints & service requests.
- The data sits idle in spreadsheets.
- The real question is unanswered: **"What should we do next?"**
- *Visual:* messy spreadsheet → question mark.

## Slide 2 — Why existing solutions fail
- **Generic AI chatbots:** hallucinate numbers, no real analytics, no decisions.
- **BI dashboards (Looker/Tableau):** costly, slow to set up, show charts not actions.
- **Manual analysis:** too slow for weekly civic response.
- *Takeaway:* teams need **trustworthy, decision-oriented** insight — fast and cheap.

## Slide 3 — Solution: CivicPulse AI
- Upload community data (CSV/JSON/PDF/text).
- **Deterministic analytics first** → trends, hotspots, anomalies (no hallucination).
- **Gemini explains + recommends** → plain-language decisions.
- Signature features: **Decision Scoreboard**, **Anomaly detection**, **One-click Executive Brief**.
- *Visual:* screenshot of the Overview tab (snapshot + scoreboard).

## Slide 4 — Architecture & Google Cloud stack
- Flow: `Upload → data_loader → analytics.py (facts) → Gemini (explain) → Dashboard`.
- **Gemini `gemini-2.5-flash-lite`** via Vertex AI / Gemini API.
- **Cloud Run** (serverless, scale-to-zero) + **Cloud Build** + **Artifact Registry**.
- Built & deployed with the **`gcloud` CLI**.
- *Visual:* the architecture diagram from the README.

## Slide 5 — Live demo flow
1. Load demo dataset → Community Snapshot + Decision Scoreboard.
2. Ask *"What should we prioritize this week?"* (grounded answer).
3. Anomalies tab → 2.8σ surge auto-detected.
4. **Generate Executive Brief** → downloadable action memo.
- *Visual:* screenshot of the generated Executive Brief.

## Slide 6 — Impact, cost & scalability
- **Impact:** faster civic response, resource prioritization, transparent decisions.
- **Cost:** flash-lite tier · one AI call per action · scale-to-zero Cloud Run ≈ near-zero idle cost.
- **Scalability:** stateless container, add BigQuery/GCS only when data grows.
- **Trust:** grounded outputs + explainability panel = no hallucinated stats.
- **Close:** *"CivicPulse AI — not just answers, better decisions."* + live URL + GitHub link.

---

### Appendix (optional backup slides)
- Sample dataset schema.
- Cost breakdown table.
- Roadmap: multi-city support, alerting, BigQuery connector, role-based access.
