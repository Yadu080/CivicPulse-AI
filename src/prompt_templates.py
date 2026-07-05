"""Prompt templates that make Gemini behave like a civic decision analyst.

All prompts are grounded strictly in the deterministic analytics dict, so the
model explains and recommends but never invents numbers.
"""

from __future__ import annotations

import json
from typing import Any

SYSTEM_INSTRUCTION = (
    "You are CivicPulse AI, a community decision intelligence assistant for city "
    "and neighborhood teams. Use ONLY the provided analytics JSON as evidence. "
    "Never invent numbers, areas, or categories that are not in the data. "
    "Clearly separate facts (from the analytics) from recommendations (your advice). "
    "Be concise, practical, and evidence-based. Write for a busy public official who "
    "has 60 seconds. Explain what matters, why it matters, and what to do next."
)

# JSON schema we ask the model to fill. Kept flat and small to save tokens.
_REPORT_SHAPE = {
    "title": "string, <= 8 words",
    "summary": "2-3 sentence executive summary",
    "key_findings": ["3-5 short bullet strings grounded in the data"],
    "anomalies": ["short strings explaining the flagged anomalies in plain language"],
    "recommended_actions": [
        {
            "action": "specific next step",
            "owner": "which department/team",
            "timeframe": "e.g. this week / 2 weeks",
        }
    ],
    "explanation": "plain-language reasoning for the top recommendation",
    "confidence": "one of: high, medium, low",
}


def _analytics_block(insights: dict[str, Any]) -> str:
    return json.dumps(insights, indent=2, default=str)


def build_brief_prompt(insights: dict[str, Any], domain: str = "citizen complaints") -> str:
    """One-click executive brief over the whole dataset."""
    return f"""Domain context: {domain}.

Here is the deterministic analytics computed from the uploaded community data:

```json
{_analytics_block(insights)}
```

Produce a decision-ready executive brief. Return ONLY valid minified-or-pretty
JSON (no markdown fences, no prose before/after) matching exactly this shape:

{json.dumps(_REPORT_SHAPE, indent=2)}

Rules:
- Ground every finding in the analytics above; cite specific counts/areas/categories.
- If a field has no data, say so rather than guessing.
- Recommended actions must be concrete and assignable.
- Keep the whole response under 250 words.
"""


def build_question_prompt(
    insights: dict[str, Any],
    question: str,
    domain: str = "citizen complaints",
) -> str:
    """Answer a specific natural-language question over the analytics."""
    return f"""Domain context: {domain}.

Deterministic analytics from the uploaded data:

```json
{_analytics_block(insights)}
```

The user asks: "{question}"

Answer using ONLY the analytics above. Return ONLY valid JSON (no markdown fences)
matching this shape:

{{
  "what_is_happening": "1-2 sentences of factual answer grounded in the data",
  "why_it_matters": "1-2 sentences on impact",
  "where": "the most relevant area(s) from the data, or 'not enough data'",
  "recommended_next_step": "one concrete action",
  "confidence": "high | medium | low",
  "executive_summary": "one crisp sentence a mayor could repeat"
}}

If the analytics do not contain enough information to answer, say so honestly in
'what_is_happening' and set confidence to 'low'.
"""


def build_text_summary_prompt(raw_text: str, domain: str = "citizen complaints") -> str:
    """Summarize pasted text or extracted PDF content (no numeric analytics)."""
    snippet = raw_text[:6000]
    return f"""Domain context: {domain}.

The user pasted the following community report / document text:

\"\"\"
{snippet}
\"\"\"

Summarize it for a decision-maker. Return ONLY valid JSON (no markdown fences):

{{
  "title": "<= 8 words",
  "summary": "2-3 sentences",
  "key_findings": ["3-5 bullets"],
  "recommended_actions": [{{"action": "...", "owner": "...", "timeframe": "..."}}],
  "confidence": "high | medium | low"
}}

Do not invent statistics that are not stated in the text.
"""
