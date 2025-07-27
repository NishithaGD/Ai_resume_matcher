from app.Resume_parsing import extract_text_from_pdf
from app.NLP_vectorization import get_similarity

def match_resume_to_job(resume_file, job_file):
    resume_text = extract_text_from_pdf(resume_file)
    
    with open(job_file, "r", encoding="utf-8") as f:
        job_text = f.read()
    
    similarity_score = get_similarity(resume_text, job_text)
    
    return similarity_score, resume_text, job_text
