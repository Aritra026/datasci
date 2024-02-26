# import streamlit as st
# import pickle
# import re
# import nltk

import streamlit as st
#import docx2txt
import re
import pickle
import re
# import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('punkt')
# nltk.download('stopwords')

# Load the trained classifier
clf = pickle.load(open('clf.pkl', 'rb'))
# Load the trained TfidfVectorizer
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

def clean_resume(resume_txt):
    clean_text = re.sub(r'http\S+', ' ', resume_txt)
    clean_text = re.sub(r'@\S+', ' ', clean_text)
    clean_text = re.sub(r'#\S+', ' ', clean_text)
    clean_text = re.sub(r'RT|cc', ' ', clean_text)
    clean_text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text

def main():
    st.title(":blue[Enter] :green[designated] :red[skills]")
    myresume = st.text_area(":red[Type your skills here:]")
    
    if st.button(":blue[Predict]"):
        cleaned_resume = clean_resume(myresume)
        input_features = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(input_features)[0]

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")
        st.write("Predicted Category:", category_name)

if __name__ == "__main__":
    main()





    
import subprocess
import sys

# Function to install a Python package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install docx2txt if not already installed
try:
    import docx2txt
except ImportError:
    print("docx2txt not found. Installing...")
    install_package("docx2txt")
    import docx2txt
    
    
    
    
    
    
    
    









# nltk.download('punkt')
# nltk.download('stopwords')

# Load the trained classifier
clf = pickle.load(open('clf.pkl', 'rb'))
# Load the trained TfidfVectorizer
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

def extract_text_from_docx(file_path):
    text = docx2txt.process(file_path)
    return text

def extract_skills(text):
    # Regular expression to find sections that contain skills
    # Modify this regex based on the structure of the resumes you expect
    # This example assumes that skills are listed in bullet points or as comma-separated values
    skill_sections = re.findall(r'(?<=skills)[:\n]?(.*?)(?=\n\n|\n\w+:|$)', text, re.IGNORECASE | re.DOTALL)
    skills = []
    for section in skill_sections:
        skills.extend(re.findall(r'\b\w+\b', section))
    return skills

def extract_name_and_phone(text):
    # Regular expression to extract name and phone number
    # Modify this regex based on the structure of the resumes you expect
    name_match = re.search(r'\b[a-zA-Z\s]+\b', text)
    name = name_match.group() if name_match else "Name not found"
    
    phone_match = re.search(r'\b\d{10}\b', text)
    phone = phone_match.group() if phone_match else "Phone number not found"
    
    return name, phone

def main():
    st.title(":blue[Upload] :green[your] :red[resume]")
    uploaded_file = st.file_uploader(":red[Upload a resume:]", key="resume_uploader", type=['pdf', 'docx'])
    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            if uploaded_file.type == "application/pdf":
                st.write("blue[PDF file format not supported yet. Please upload a DOCX file.]")
                return
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                resume_text = extract_text_from_docx(uploaded_file)
                st.write(resume_text)
                
                skills = extract_skills(resume_text)
                name, phone = extract_name_and_phone(resume_text)
                st.header(":blue[Name and Phone Number]")
                st.write(f":blue[Name:] {name}")
                st.write(f":blue[Phone Number:] {phone}")
                st.header(":blue[Extracted Skills]")
                if skills:
                    for skill in skills:
                        st.write(skill)
                else:
                    st.write(":red[No skills extracted.]")

                input_features = tfidf.transform([resume_text])

                prediction_id = clf.predict(input_features)[0]

                category_mapping = {
                    0: "Advocate",
                    1: "Arts",
                    2: "Automation Testing",
                    3: "Blockchain",
                    4: "Business Analyst",
                    5: "Civil Engineer",
                    6: "Data Science",
                    7: "Database",
                    8: "DevOps Engineer",
                    9: "DotNet Developer",
                    10: "ETL Developer",
                    11: "Electrical Engineering",
                    12: "HR",
                    13: "Hadoop",
                    14: "Health and fitness",
                    15: "Java Developer",
                    16: "Mechanical Engineer",
                    17: "Network Security Engineer",
                    18: "Operations Manager",
                    19: "PMO",
                    20: "Python Developer",
                    21: "SAP Developer",
                    22: "Sales",
                    23: "Testing",
                    24: "Web Designing"
                }

                category_name = category_mapping.get(prediction_id, "Unknown")
                st.header(":red[Predicted Category:]")
                if prediction_id in category_mapping:
                    st.markdown(f"**{category_name}**")
                else:
                    st.write(":red[Unknown category]")

        except UnicodeDecodeError:
            st.write(":red[Error: Unable to read the file. Please ensure it is in a readable format.]")

if __name__ == "__main__":
    main()




