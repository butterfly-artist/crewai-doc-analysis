
# --- Refactored pipeline for explicit prompt passing ---
import os
from utils import load_pdf_text, chunk_text
from prompts import SUMMARIZER_PROMPT, SYNTH_PROMPT, REVIEW_PROMPT
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama3-70b-8192",
)

def summarize_chunk(chunk):
    prompt = SUMMARIZER_PROMPT.format(chunk_text=chunk['text'], chunk_id=chunk['id'])
    response = llm.invoke(prompt)
    # Extract text from AIMessage if needed
    if hasattr(response, 'content'):
        response_text = response.content
    else:
        response_text = response
    try:
        return json.loads(response_text)
    except Exception:
        return {"chunk_id": chunk['id'], "summary": response_text, "key_points": [], "confidence": 0.0}

def synthesize_summaries(summaries):
    prompt = SYNTH_PROMPT.replace("{summaries}", json.dumps(summaries))
    prompt = prompt + "\nSummaries: " + json.dumps(summaries)
    response = llm.invoke(prompt)
    if hasattr(response, 'content'):
        response_text = response.content
    else:
        response_text = response
    try:
        return json.loads(response_text)
    except Exception:
        return {"executive_summary": response_text, "tl_dr": [], "references": {}}

def review_summary(chunks, synthesized):
    prompt = REVIEW_PROMPT + f"\nOriginal Chunks: {json.dumps(chunks)}\nSynthesized: {json.dumps(synthesized)}"
    response = llm.invoke(prompt)
    if hasattr(response, 'content'):
        return response.content
    return response

def kickoff(doc_path):
    text = load_pdf_text(doc_path)
    chunks = chunk_text(text)
    # Summarize each chunk
    summaries = [summarize_chunk(chunk) for chunk in chunks]
    # Synthesize summaries
    synthesized = synthesize_summaries(summaries)
    # Review
    reviewed = review_summary(chunks, synthesized)
    return reviewed

if __name__ == "__main__":
    import sys
    doc_path = sys.argv[1] if len(sys.argv) > 1 else "C:\\path\\to\\your\\file.pdf"
    result = kickoff(doc_path)
    print(result)
    import sys
    doc_path = sys.argv[1] if len(sys.argv) > 1 else "C:\\path\\to\\your\\file.pdf"
    kickoff(doc_path)
