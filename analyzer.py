# analyzer.py

import fitz  # PyMuPDF

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Basic resume analysis
def analyze_resume(text):
    analysis = {}

    # Basic stats
    lines = text.split("\n")
    analysis["total_lines"] = len(lines)
    analysis["word_count"] = len(text.split())

    # Keyword checks
    keywords = ["Python", "Machine Learning", "Data Science", "Deep Learning", "NLP", "SQL"]
    found_keywords = [kw for kw in keywords if kw.lower() in text.lower()]
    analysis["matched_keywords"] = found_keywords

    # Education detection (basic)
    if "bachelor" in text.lower() or "b.tech" in text.lower():
        analysis["education"] = "Bachelor's"
    elif "master" in text.lower() or "m.tech" in text.lower():
        analysis["education"] = "Master's"
    else:
        analysis["education"] = "Not Found"

    return analysis
