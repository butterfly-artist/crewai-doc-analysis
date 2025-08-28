# app/utils.py
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def load_pdf_text(path):
    reader = PdfReader(path)
    pages = [p.extract_text() or "" for p in reader.pages]
    return "\n".join(pages)

def chunk_text(text, chunk_size=300, chunk_overlap=30):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = splitter.split_text(text)
    return [{"id": i, "text": t} for i, t in enumerate(chunks)]
