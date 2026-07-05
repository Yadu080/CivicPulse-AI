# CivicPulse AI — Deployment Checklist

Use this to go from empty machine to a live, judge-ready public link.

## ✅ Prerequisites
- [ ] Google Cloud account with **billing enabled** (free-tier credits are fine).
- [ ] [`gcloud` CLI](https://cloud.google.com/sdk/docs/install) installed (`gcloud --version`).
- [ ] Python 3.11+ locally (`python --version`).
- [ ] A GitHub account.

## ✅ Local verification (do this first)
- [ ] `pip install -r requirements.txt`
- [ ] `python sample_data/generate_sample.py` (regenerates demo data)
- [ ] `cp .env.example .env` and set `GEMINI_API_KEY`
- [ ] `streamlit run app.py` → app loads at http://localhost:8501
- [ ] Click **Load demo dataset** → Overview populates
- [ ] **Generate Executive Brief** returns real Gemini output (not the offline fallback)

## ✅ Google Cloud setup (one time)
- [ ] `gcloud auth login`
- [ ] `gcloud config set project YOUR_PROJECT_ID`
- [ ] Enable APIs:
  ```bash
  gcloud services enable run.googleapis.com aiplatform.googleapis.com \
                         cloudbuild.googleapis.com artifactregistry.googleapis.com
  ```
  (or run `./setup_gcloud.sh YOUR_PROJECT_ID us-central1`)

## ✅ Deploy to Cloud Run
Choose ONE credentials mode:

**A) Gemini Developer API key (simplest)**
- [ ] `export GEMINI_API_KEY=your_key`
- [ ] `./deploy.sh YOUR_PROJECT_ID us-central1`

**B) Vertex AI (uses the Cloud Run service account)**
- [ ] `./deploy.sh YOUR_PROJECT_ID us-central1` (no key needed)
- [ ] Grant the runtime service account Vertex access:
  ```bash
  PROJECT_NUMBER=$(gcloud projects describe YOUR_PROJECT_ID --format='value(projectNumber)')
  gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:${PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
    --role="roles/aiplatform.user"
  ```

## ✅ Post-deploy verification
- [ ] Deploy command prints a `https://...run.app` URL.
- [ ] Open the URL → dashboard loads.
- [ ] Load demo dataset → Ask AI → Generate Executive Brief works in the cloud.
- [ ] Sidebar shows **"Connected via …"** (not the offline warning).
- [ ] Copy the public URL into your submission + deck.

## ✅ Submission assets
- [ ] **Public link:** the Cloud Run URL.
- [ ] **GitHub repo:** push the code (see below).
- [ ] **Demo video:** record using `docs/DEMO_SCRIPT.md` (≤3 min), upload to YouTube (unlisted OK).
- [ ] **PPT:** build from `docs/PPT_OUTLINE.md`, export to PDF.
- [ ] Add the live URL + video link to the README top section.

## ✅ Push to GitHub
```bash
git init
git add .
git commit -m "CivicPulse AI: initial hackathon prototype"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/civicpulse-ai.git
git push -u origin main
```

## ✅ Cost hygiene (after the hackathon)
- [ ] `--min-instances 0` keeps idle cost ≈ $0 (already set).
- [ ] To fully stop: `gcloud run services delete civicpulse-ai --region us-central1`
- [ ] Review billing at https://console.cloud.google.com/billing

## 🧯 Common gotchas
- **Container fails to start:** ensure the app binds `0.0.0.0:$PORT` (handled in Dockerfile).
- **403 from Vertex:** missing `roles/aiplatform.user` on the runtime SA.
- **Slow cold start:** first request after idle takes a few seconds (scale-from-zero) — normal.
- **Quota errors:** flash-lite has generous limits; retry logic handles transient 429s.
