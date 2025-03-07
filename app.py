import streamlit as st

# Function to Generate Resume Text
def generate_resume_text(name, email, phone, summary, skills, experience, education):
    resume_content = f"""
    ===============================
            {name.upper()}
    ===============================
    📧 Email: {email} | 📞 Phone: {phone}

    -------------------------------
    🏆 PROFESSIONAL SUMMARY
    -------------------------------
    {summary}

    -------------------------------
    🔧 SKILLS
    -------------------------------
    {skills}

    -------------------------------
    💼 WORK EXPERIENCE
    -------------------------------
    {experience}

    -------------------------------
    🎓 EDUCATION
    -------------------------------
    {education}

    ===============================
    📄 Resume Generated Successfully!
    ===============================
    """
    return resume_content

# Page Config
st.set_page_config(page_title="Professional Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Better Visibility
st.markdown("""
    <style>
    .stApp { 
        background: #F8F9FA;
        color: black;
        font-family: 'Arial', sans-serif;
    }
    h1 { text-align: center; color: #2C3E50; }
    .stTextInput, .stTextArea {
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button {
        background: #27AE60;
        color: white;
        border-radius: 8px;
        font-size: 18px;
    }
    .stDownloadButton>button {
        background: #E74C3C;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])
if profile_pic:
    st.image(profile_pic, caption="Profile Picture", width=150)

# Input Fields
name = st.text_input("👤 Full Name")
email = st.text_input("📧 Email")
phone = st.text_input("📞 Phone Number")
summary = st.text_area("🏆 Professional Summary")
skills = st.text_area("🔧 Skills (comma-separated)")
experience = st.text_area("💼 Work Experience")
education = st.text_area("🎓 Education")

# Generate Resume Button
if st.button("Generate Resume 📄"):
    if name and email and phone and summary and skills and experience and education:
        resume_text = generate_resume_text(name, email, phone, summary, skills, experience, education)

        # Resume Preview
        st.subheader("📜 Generated Resume")
        st.code(resume_text, language="text")

        # Download Button
        st.download_button(label="Download Resume as TXT 📥", data=resume_text, file_name="Resume.txt", mime="text/plain")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
    
