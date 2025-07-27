import streamlit as st
from app.Resume_parsing import extract_text_from_pdf
from app.NLP_vectorization import get_similarity
from app.extraction import (
    extract_contact_info, extract_summary, extract_skills,
    extract_education, extract_certifications
)

st.set_page_config(page_title="AI Resume Matcher", layout="centered")
st.title("AI Resume Matcher with Recruiter Inputs")

st.markdown("Upload a Resume (PDF) and enter the Job Description + Skills to check how well it matches.")

# === User Inputs ===
resume_file = st.file_uploader("Upload Resume", type=["pdf"])
job_text_input = st.text_area("Paste Job Description", height=200)
skills_input = st.text_input("Desired Skills (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning")
experience_input = st.text_input("Required Years of Experience", placeholder="e.g., 2 years")
degree_input = st.text_input("Required Degree (optional)", placeholder="e.g., B.Tech, M.Sc")

# === Trigger Matching ===
if resume_file and job_text_input:
    # Save uploaded resume
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())

    # Extract resume text
    resume_text = extract_text_from_pdf("temp_resume.pdf")
    resume_lower = resume_text.lower()

    # === NLP Matching: Resume vs Job Description ===
    job_match_score = get_similarity(resume_text, job_text_input)

    # === Skill Matching Logic ===
    input_skills = [s.strip().lower() for s in skills_input.split(",") if s.strip()]
    resume_skills = extract_skills(resume_text)
    matched_skills = [skill for skill in input_skills if skill in resume_skills]
    unmatched_skills = [skill for skill in input_skills if skill not in resume_skills]
    skill_score = len(matched_skills) / len(input_skills) if input_skills else 0

    # === Field Extraction ===
    contact_info = extract_contact_info(resume_text)
    summary = extract_summary(resume_text)
    education = extract_education(resume_text)
    certifications = extract_certifications(resume_text)

    # === Display Results ===
    st.success(f"Job Match Score (NLP-based): {round(job_match_score * 100, 2)}%")
    st.success(f"Skill Match Score: {round(skill_score * 100, 2)}%")

    st.subheader("Extracted Resume Summary")

    st.markdown(f"""
    Name: {resume_file.name.replace('.pdf','').replace('_',' ').title()}  
    Email: {contact_info['email']}  
    Phone: {contact_info['phone']}  
    LinkedIn: {contact_info['linkedin']}  
    GitHub: {contact_info['github']}  
    Summary: {summary}  
    """)

    st.markdown("Education:")
    if education:
        for edu in education:
            st.markdown(f"- {edu}")
    else:
        st.markdown("Not found.")

    st.markdown("Certifications:")
    if certifications:
        for cert in certifications:
            st.markdown(f"- {cert}")
    else:
        st.markdown("Not found.")

    st.subheader("Recruiter Inputs vs Resume")

    st.write(f"Matched Skills: {', '.join(matched_skills) if matched_skills else 'None'}")
    st.write(f"Unmatched Skills: {', '.join(unmatched_skills) if unmatched_skills else 'None'}")

    if experience_input:
        st.write(f"Required Experience: {experience_input} – "
                 f"{'Found' if experience_input.lower() in resume_lower else 'Not Found'}")

    if degree_input:
        st.write(f"Required Degree: {degree_input} – "
                 f"{'Found' if degree_input.lower() in resume_lower else 'Not Found'}")

    with st.expander("Full Resume Text"):
        st.write(resume_text)

    with st.expander("Job Description Entered"):
        st.write(job_text_input)

else:
    st.warning("Please upload a resume and enter a job description to begin matching.")
