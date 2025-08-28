# app/prompts.py

SUMMARIZER_PROMPT = '''
Summarize: {chunk_text}
Return JSON:
{{
  "chunk_id": "{chunk_id}",
  "summary": "...(50 words max)...",
  "key_points": ["...(2-3 points)..."],
  "confidence": 0.0-1.0
}}
'''

SYNTH_PROMPT = '''
Synthesize summaries into JSON:
{
  "executive_summary": "...(2 paragraphs max)...",
  "tl_dr": ["...(3 points max)..."],
  "references": {"point": "chunk_id"}
}
'''

REVIEW_PROMPT = '''
Verify facts in summary against chunks. List any inconsistencies or confirm accuracy.
'''
