import re

def extract_contact_info(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'(?:(?:\+91|91)?[\s\-]?)?[789]\d{9}', text)
    linkedin = re.findall(r'https?://(www\.)?linkedin\.com/in/[^\s]+', text)
    github = re.findall(r'https?://(www\.)?github\.com/[^\s]+', text)

    return {
        "email": email[0] if email else "Not Found",
        "phone": phone[0] if phone else "Not Found",
        "linkedin": linkedin[0] if linkedin else "Not Found",
        "github": github[0] if github else "Not Found"
    }

def extract_summary(text):
    lines = text.strip().split('\n')
    for line in lines[:10]:
        if len(line.split()) > 6:
            return line.strip()
    return "Not Found"

def extract_skills(text):
    skills_list = [
        "python", "java", "sql", "machine learning", "deep learning", "nlp",
        "tensorflow", "pytorch", "html", "css", "javascript", "react", "git"
    ]
    found = []
    text_lower = text.lower()
    for skill in skills_list:
        if skill in text_lower:
            found.append(skill)
    return found

def extract_education(text):
    lines = text.split('\n')
    education = []
    for line in lines:
        if any(x in line.lower() for x in ["b.tech", "bachelor", "master", "msc", "be", "m.tech", "degree"]):
            education.append(line.strip())
    return education

def extract_certifications(text):
    cert_keywords = ['certified', 'certification', 'completed', 'course', 'coursera', 'udemy', 'udacity']
    lines = text.split('\n')
    certs = [line for line in lines if any(k in line.lower() for k in cert_keywords)]
    return certs
