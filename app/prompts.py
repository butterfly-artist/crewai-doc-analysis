# app/prompts.py

SUMMARIZER_PROMPT = '''
You are a concise technical summarizer.
Input: {chunk_text}
Task: Produce a JSON object:
{{
  "chunk_id": "{chunk_id}",
  "summary": "... (max 150 words) ...",
  "key_points": ["...", "..."],
  "confidence": 0.0-1.0
}}
Do not invent facts. If uncertain, say "uncertain" for that point.
'''

SYNTH_PROMPT = '''
You are an editor. Given a list of chunk summaries (with chunk_id and key_points), produce:
1) A compact executive summary (3-5 short paragraphs)
2) A 5-bullet TL;DR
3) A mapping to original chunk_ids for reference
Return JSON { "executive_summary": "...", "tl_dr": [...], "references": {...} }
'''

REVIEW_PROMPT = '''
You are a fact-checker. Given the original chunks + synthesized summary, verify any named entities, dates, or stats and flag inconsistencies. Output corrections or confirm.
'''
