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
            feedback_dict = analyze_resume(resume_text)
            feedback = f"""
            **Total Lines:** {feedback_dict['total_lines']}
            **Word Count:** {feedback_dict['word_count']}
            **Matched Keywords:** {', '.join(feedback_dict['matched_keywords'])}
            **Education:** {feedback_dict['education']}
            """
            st.success("✅ Analysis Complete")
            st.markdown("### 🔍 Feedback from AI:")

            st.markdown(f"""
            **📄 Total Lines:** {feedback['total_lines']}  
            **🔢 Word Count:** {feedback['word_count']}  
            **🧠 Matched Keywords:** {', '.join(feedback['matched_keywords']) or "None"}  
            **🎓 Education:** {feedback['education']}
            """)

