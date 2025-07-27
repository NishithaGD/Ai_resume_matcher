AI Resume Matcher

AI Resume Matcher is a smart web-based application that uses Natural Language Processing (NLP) and Machine Learning (ML) to analyze resumes and match them against job descriptions. It helps recruiters and job seekers evaluate resume-job fit, extract key resume information, and provide a compatibility score.

Features

- Resume parsing and text extraction (PDF)
- Intent-based resume-job matching
- Contact info, education, skills, and certification extraction
- Similarity scoring based on job description
- Clean, user-friendly interface using Streamlit

Tech Stack

- Python 3.10+
- Streamlit for UI
- scikit-learn for similarity computation
- spaCy or transformers (BERT) for NLP
- PyPDF2 or pdfplumber for PDF parsing
- pandas & NumPy for data handling

Project Structure

resume-matcher/
│
├── app/
│   ├── Resume_parsing.py          # Extracts text from PDF
│   ├── NLP_vectorization.py       # Computes similarity
│   ├── extraction.py              # Extracts skills, contact info, etc.
│   └── __init__.py
│
├── main.py                        # Streamlit frontend
├── requirements.txt
└── README.md

How to Run

1. Clone the repository:

   git clone https://github.com/your-username/resume-matcher.git
   cd resume-matcher

2. Install dependencies:

   pip install -r requirements.txt

3. Run the application:

   streamlit run main.py

Example Use Cases

- Upload a resume and compare it against a job description to see match percentage.
- Extract and preview skills, education, and certifications from a candidate's resume.
- Use as a recruitment tool or job seeker optimization tool.

Future Enhancements

- Multiple job descriptions input and ranking
- Resume recommendations for better fit
- Cloud deployment (Streamlit Cloud, AWS, or GCP)
- REST API support for integration

License

This project is licensed under the MIT License.

Contributing

Contributions are welcome. Please open an issue to discuss before submitting a pull request.
