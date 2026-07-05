# CivicPulse AI — 3-Minute Demo Video Script

> Total runtime: ~3:00. Keep energy high, cursor movements deliberate.
> Record at 1080p, browser zoom ~110%. Use the bundled demo dataset.

---

### 0:00 – 0:20 · Hook (problem)
**On screen:** your face or a title slide "CivicPulse AI".
> "Every city collects thousands of citizen complaints — potholes, water leaks,
> missed garbage pickups. But the data just sits in spreadsheets. The real
> question isn't *'what happened?'* — it's *'what should we do next?'*
> Meet **CivicPulse AI**."

### 0:20 – 0:40 · What it is
**On screen:** the app hero + tabs.
> "CivicPulse is a decision-intelligence dashboard. It's not a chatbot — it computes
> real analytics in Python first, then uses a small, low-cost Gemini model to turn
> those numbers into decisions. So it never makes up statistics."

### 0:40 – 1:10 · Load data + Community Snapshot
**Action:** click **⚡ Load demo dataset** → Overview tab.
> "I'll load a week of citizen-complaint data. Instantly we get a Community Snapshot:
> 370 records, the top hotspot is **Riverside**, the leading issue is **Waste
> Collection**, and volume is **rising 36%** week over week."
**Action:** point to the **Decision Scoreboard**.
> "This Decision Scoreboard is the heart of the product — Urgency 91, Impact, and
> Confidence scores tell the team this needs action *now*."

### 1:10 – 1:35 · Ask AI
**Action:** Ask AI tab → click *"What should we prioritize this week?"*
> "I can ask in plain English. Watch — the answer is grounded strictly in the data:
> what's happening, why it matters, where, and the recommended next step, with a
> confidence rating. No hallucinated numbers."

### 1:35 – 2:00 · Anomalies
**Action:** Anomalies tab.
> "CivicPulse auto-detects anomalies with transparent statistical thresholds. Here it
> caught a **2.8-sigma volume surge this week** and a Waste Collection spike in
> Riverside — exactly the kind of emerging issue a city team would otherwise miss."

### 2:00 – 2:40 · The wow feature — Executive Brief
**Action:** Recommendations tab → click **🧠 Generate Executive Brief**.
> "And here's the feature judges will remember: one click, one Gemini call, and we get
> a decision-ready **Executive Brief** — summary, key findings, anomalies, and
> concrete recommended actions with owners and timeframes."
**Action:** open the Explainability expander, then click **Download memo**.
> "There's even an explainability panel showing *why*, and I can download the whole
> memo to send to the sanitation department right now."

### 2:40 – 3:00 · Close (cloud + cost)
**On screen:** README architecture / Cloud Run URL.
> "It's deployed on **Google Cloud Run** with **Gemini flash-lite**, built entirely
> with the **gcloud CLI**, and it scales to zero — so it costs almost nothing to run.
> CivicPulse AI: **not just answers — better decisions.** Thank you!"

---

## Recording tips
- Pre-load the demo dataset before hitting record to avoid dead air.
- Have `GEMINI_API_KEY` set so the brief and Q&A show real AI output.
- If the network is flaky, the offline fallback still demos the full flow.
- Keep the Executive Brief generation as the climax — it's the memorable moment.
