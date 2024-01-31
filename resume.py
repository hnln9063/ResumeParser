import pdfplumber
import google.generativeai as palm
palm.configure(api_key='Your_API_KEY')

def parse_resume(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_path = 'HNLakshmiNarasimha_Resume.pdf'
resume_text = parse_resume(pdf_path)
print("Resume Text\n")
print(resume_text)

import spacy

def extract_skills(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    skills = set()

    for token in doc:
        # Check if the token is a skill (you can customize this based on your needs)
        if token.text.lower() in [
        "python", "java", "javascript", "machine learning", "data analysis",
        "c", "c++", "ruby", "swift", "kotlin", "php", "go", "typescript",
        "html", "css", "react", "angular", "vue.js", "node.js", "django",
        "flask", "bootstrap", "express.js", "spring boot", "ruby on rails",
        "flutter", "android", "ios", "swift", "kotlin", "sql", "mysql",
        "postgresql", "mongodb", "sqlite", "oracle", "aws", "azure", "google cloud platform",
        "docker", "kubernetes", "jenkins", "ansible", "terraform", "git",
        "github", "gitlab", "bitbucket", "object-oriented programming", "functional programming",
        "procedural programming", "bash", "powershell", "tcp/ip", "http/https", "dns",
        "ssl/tls", "cybersecurity", "encryption", "penetration testing", "security auditing",
        "machine learning", "data analysis", "pandas", "numpy", "scipy",
        "visual studio code", "intellij idea", "eclipse", "pycharm", "unit testing",
        "integration testing", "selenium", "junit", "travis ci", "circleci", "jenkins",
        "gitlab ci/cd", "scrum", "kanban", "jira", "agile methodologies", "linux",
        "windows", "macos", "restful", "graphql", "raspberry pi", "arduino", "mqtt"]:
            skills.add(token.text)
    return skills

# Example usage
resume_skills = list(extract_skills(resume_text))

print("Skills:", resume_skills)
for i in range(len(resume_skills)):
  reply = palm.chat(context="Generate 2 hard level interview questions with correct answer immediately after every question for the given topics. ", messages='Generate interview related questions about' +resume_skills[i]+ 'along with correct answer immediately after every question. Provide detailed explaination. Dont give questions like what is HTML, What is Eclipse etc..', temperature=0)
  print(reply.last)
