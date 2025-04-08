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

    # Improved education detection
    education_text = text.lower()
    if any(term in education_text for term in ["bachelor", "b.tech", "undergraduate", "bca"]):
        analysis["education"] = "Bachelor's"
    elif any(term in education_text for term in ["master", "m.tech", "postgraduate", "mca"]):
        analysis["education"] = "Master's"
    else:
        analysis["education"] = "Not Found"

    return analysis
