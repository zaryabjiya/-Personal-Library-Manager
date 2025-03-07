import streamlit as st
import base64

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
st.set_page_config(page_title="🚀 Professional Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Modern Styling
st.markdown("""
    <style>
    /* Vibrant Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #3498DB, #8E44AD);
        color: white;
        font-family: 'Arial', sans-serif;
    }
    /* Centered Title */
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #FFFFFF;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    /* Stylish Input Fields */
    .stTextInput, .stTextArea {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 12px;
        background-color: #FFFFFF;
        color: #2C3E50;
    }
    /* Stylish Buttons */
    .stButton>button {
        background: #27AE60;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 12px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #2ECC71;
        transform: scale(1.05);
    }
    /* Download Button */
    .stDownloadButton>button {
        background: #E74C3C;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 12px;
        transition: 0.3s;
    }
    .stDownloadButton>button:hover {
        background: #C0392B;
        transform: scale(1.05);
    }
    /* Profile Picture */
    .profile-img {
        display: block;
        margin: auto;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        border: 4px solid #F1C40F;
    }
    /* Resume Preview */
    .resume-preview {
        background: #FFFFFF;
        color: #2C3E50;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='title'>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])

if profile_pic:
    profile_pic_encoded = base64.b64encode(profile_pic.read()).decode("utf-8")
    st.markdown(f"""
        <img src="data:image/png;base64,{profile_pic_encoded}" class="profile-img" />
    """, unsafe_allow_html=True)

# Input Fields for Resume
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
        st.markdown("### 📜 Generated Resume")
        st.markdown(f"<div class='resume-preview'><pre>{resume_text}</pre></div>", unsafe_allow_html=True)
        
        # Download Button
        st.download_button(label="Download Resume as TXT 📥", data=resume_text, file_name="Resume.txt", mime="text/plain")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")

