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

            st.success("✅ Analysis Complete")
            st.markdown("### 📊 Resume Metrics:")
            st.markdown(f"""
**📄 Total Lines:** {feedback_dict.get('total_lines', 'N/A')}  
**🔢 Word Count:** {feedback_dict.get('word_count', 'N/A')}  
**🧠 Matched Keywords:** {', '.join(feedback_dict.get('matched_keywords', [])) or 'None'}  
**🎓 Education:** {feedback_dict.get('education', 'Not Found')}
""")
 
