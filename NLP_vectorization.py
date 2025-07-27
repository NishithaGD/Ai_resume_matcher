from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(resume_text, job_text):
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume_text, job_text])
    sim_score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return sim_score
