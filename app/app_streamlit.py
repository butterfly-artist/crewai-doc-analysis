import streamlit as st
import os
from crew_setup import kickoff

st.set_page_config(page_title="PDF Summarizer", page_icon="📄", layout="centered")
st.title("📄 PDF Summarizer")
st.markdown("""
Upload a PDF file and get a concise executive summary and TL;DR. Powered by LLMs.
""")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing and summarizing your PDF..."):
        # Save uploaded file to a temp location
        temp_path = os.path.join("temp_" + uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())
        try:
            result = kickoff(temp_path)
            st.subheader("Executive Summary & TL;DR")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            os.remove(temp_path)
else:
    st.info("Please upload a PDF file to begin.")

# Install streamlit package
os.system('pip install streamlit')
