import streamlit as st
import base64

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

st.set_page_config(page_title="Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
    }
    .title {
        text-align: center;
        color: #2C3E50;
    }
    .stTextInput, .stTextArea {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stButton>button {
        background-color: #3498DB;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px;
    }
    .stDownloadButton>button {
        background-color: #27AE60;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px;
    }
    .profile-img {
        display: block;
        margin: auto;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        border: 4px solid #3498DB;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>📄 Stylish Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])

if profile_pic:
    profile_pic_encoded = base64.b64encode(profile_pic.read()).decode("utf-8")
    st.markdown(f"""
        <img src="data:image/png;base64,{profile_pic_encoded}" class="profile-img" />
    """, unsafe_allow_html=True)

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Education")

if st.button("Generate Resume 📄"):
    if name and email and phone and summary and skills and experience and education:
        resume_text = generate_resume_text(name, email, phone, summary, skills, experience, education)
        
        # Show resume preview
        st.text_area("Generated Resume", resume_text, height=300)
        
        # Download button
        st.download_button(label="Download Resume as TXT 📥", data=resume_text, file_name="Resume.txt", mime="text/plain")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
