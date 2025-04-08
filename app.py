import streamlit as st
from analyzer import extract_text_from_pdf, analyze_resume

st.set_page_config(page_title="LangChain Resume Analyzer", layout="centered")

st.title("📄 LangChain Resume Analyzer")
st.markdown("Upload your resume and get AI-generated feedback tailored for any job role.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_role = st.text_input("Enter the job role you're applying for", value="Data Scientist")

if uploaded_file and job_role:
    if st.button("Analyze"):
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            feedback = analyze_resume(resume_text, job_role)
            st.success("✅ Analysis Complete")
            st.markdown("### 🔍 Feedback from AI:")
            st.markdown(feedback)
