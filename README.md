# 🏙️ CivicPulse AI

> Community decision intelligence powered by Gemini on Google Cloud.  
> *Not just answers, better decisions.*

CivicPulse AI is a team-built decision intelligence dashboard for cities, communities, and operations teams. It helps users upload local service data, ask natural-language questions, detect emerging anomalies, and generate practical recommendations backed by structured analytics.

Rather than behaving like a generic chatbot, CivicPulse AI computes trends, hotspot areas, severity patterns, and anomaly signals in Python first, then uses Gemini to explain what matters and recommend next steps. The result is a lightweight product that turns community data into decision-ready insight.

## Team
This project was built as a collaborative team effort by:

- Aadithya AR (Team Lead)
- Yadunandan M Nimbalkar
- Kenisha P

Each contributor helped shape the product direction, implementation, and final prototype. The README, codebase, deployment flow, and product framing reflect a shared team effort.

## What CivicPulse AI Does

- Accepts community datasets through CSV, JSON, PDF text, or pasted reports
- Normalizes raw data into a consistent analysis-ready format
- Computes deterministic analytics such as counts, trends, severity mix, and open-case rates
- Flags anomalies using simple, explainable statistical thresholds
- Lets users ask natural-language questions over the uploaded data
- Generates executive-friendly summaries and action recommendations using Gemini
- Produces a simple decision layer through urgency, impact, and confidence scoring

## Why It Stands Out

### Deterministic first
The system does the heavy analytical work before any LLM call. This makes outputs cheaper, faster, and more trustworthy.

### Decision-focused UX
The dashboard is designed around action, not just conversation. Users can quickly understand:

- what is happening
- why it matters
- where attention is needed
- what should be done next

### Low-cost cloud deployment
The app runs on Cloud Run with a small Gemini model tier and scale-to-zero infrastructure, making it realistic for hackathons, pilots, and lightweight civic deployments.

## Core Features

- Natural-language analytics over local community data
- Community Snapshot with top issue, hotspot area, and trend summary
- Decision Scoreboard with urgency, impact, confidence, and severity
- Explainable anomaly detection
- One-click Executive Brief
- Action recommendations grounded in computed analytics
- Offline fallback mode when Gemini is unavailable

## Architecture Overview

```text
User / Community Team
        ↓
Data Upload (CSV / JSON / PDF / text)
        ↓
data_loader.py
        ↓
analytics.py
  - counts by area and category
  - weekly trends
  - severity distribution
  - anomaly detection
  - urgency / impact / confidence scores
        ↓
gemini_client.py + prompt_templates.py
        ↓
Streamlit Dashboard
  - Overview
  - Ask AI
  - Anomalies
  - Recommendations
  - About
```

**Stack:** Streamlit, Python, Gemini, Cloud Run, Cloud Build, Artifact Registry, `gcloud` CLI.

## Repository Structure

```text
civicpulse-ai/
├── app.py
├── src/
│   ├── data_loader.py
│   ├── analytics.py
│   ├── gemini_client.py
│   ├── prompt_templates.py
│   └── utils.py
├── sample_data/
│   ├── citizen_complaints.csv
│   ├── citizen_complaints.json
│   └── generate_sample.py
├── requirements.txt
├── Dockerfile
├── cloudbuild.yaml
├── deploy.sh
├── setup_gcloud.sh
├── .env.example
└── README.md
```

## Local Run

```bash
git clone https://github.com/Yadu080/CivicPulse-AI.git
cd civicpulse-ai

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

# add GEMINI_API_KEY to .env if using Gemini Developer API
streamlit run app.py
```

Open `http://localhost:8501`, load the sample dataset, and explore the dashboard.

## Google Cloud Deployment

### One-time setup

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com aiplatform.googleapis.com \
  cloudbuild.googleapis.com artifactregistry.googleapis.com
```

Or run:

```bash
./setup_gcloud.sh YOUR_PROJECT_ID us-central1
```

### Deploy with Vertex AI

```bash
./deploy.sh YOUR_PROJECT_ID us-central1
```

### Deploy with Gemini API key

```bash
export GEMINI_API_KEY=your_key_here
./deploy.sh YOUR_PROJECT_ID us-central1
```

## Gemini Integration

- `src/gemini_client.py` handles Gemini setup, retries, backend selection, and fallback behavior
- Default model: `gemini-2.5-flash-lite`
- Prompts are grounded in structured analytics so the model does not invent numbers

## Cost-Conscious Design

- One Gemini call per meaningful action
- Flash-lite model tier by default
- No heavy database or always-on backend required
- Cloud Run configured for scale-to-zero
- Bundled sample data keeps demos simple and cheap

## Sample Data

The included demo dataset is a realistic citizen-complaints sample with fields such as:

- `date`
- `area`
- `category`
- `complaint_type`
- `severity`
- `status`
- `department`
- `notes`

It is designed to surface clear hotspots, a rising trend, and anomaly conditions for demo purposes.

To regenerate it:

```bash
python sample_data/generate_sample.py
```

## Troubleshooting

| Issue | What to check |
|---|---|
| Gemini shows offline fallback | Set `GEMINI_API_KEY` or configure Vertex AI environment variables |
| Vertex AI access fails on Cloud Run | Grant `roles/aiplatform.user` to the runtime service account |
| Artifact Registry push fails | Ensure the build service account has `roles/artifactregistry.writer` |
| Upload columns are not recognized | Rename fields to expected values such as `date`, `area`, `category`, `severity` |
| PDF text does not extract | The current flow supports text-based PDFs, not scanned OCR-only files |

## Contributors

This repository represents a shared team effort by:

- Aadithya AR (Team Lead)
- Yadunandan M Nimbalkar
- Kenisha P

## License

MIT
