# app/run.py

import sys
import os
from crew_setup import kickoff

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("hello this is yash")
        sys.exit(1)
    input_path = sys.argv[1]
    if os.path.isdir(input_path):
        pdf_files = [f for f in os.listdir(input_path) if f.lower().endswith('.pdf')]
        if not pdf_files:
            print(f"No PDF files found in {input_path}.")
            sys.exit(1)
        for pdf in pdf_files:
            pdf_path = os.path.join(input_path, pdf)
            print(f"\nProcessing: {pdf_path}")
            result = kickoff(pdf_path)
            print("Final Result:", result)
    elif os.path.isfile(input_path) and input_path.lower().endswith('.pdf'):
        print(f"\nProcessing: {input_path}")
        result = kickoff(input_path)
        print("Final Result:", result)
    else:
        print(f"Error: {input_path} is not a valid PDF file or directory.")
        sys.exit(1)
