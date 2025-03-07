import streamlit as st
import base64

# Function to Generate Resume Text
def generate_resume_text(name, email, phone, summary, skills, experience, education, profile_pic_data):
    profile_section = f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{profile_pic_data}" 
             style="border-radius: 50%; width: 150px; height: 150px; border: 3px solid #F1C40F;">
    </div>
    """ if profile_pic_data else ""

    resume_content = f"""
    {profile_section}
    <h2 style="text-align: center; color: #2C3E50;">{name.upper()}</h2>
    <p style="text-align: center;">
        📧 <b>Email:</b> {email} &nbsp; | &nbsp; 📞 <b>Phone:</b> {phone}
    </p>
    
    <hr>

    <h3>🏆 PROFESSIONAL SUMMARY</h3>
    <p>{summary}</p>

    <h3>🔧 SKILLS</h3>
    <p>{skills}</p>

    <h3>💼 WORK EXPERIENCE</h3>
    <p>{experience}</p>

    <h3>🎓 EDUCATION</h3>
    <p>{education}</p>

    <hr>
    <h4 style="text-align: center; color: green;">📄 Resume Generated Successfully!</h4>
    """

    return resume_content

# Page Config
st.set_page_config(page_title="🚀 Professional Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Modern Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #2C3E50;
        margin-bottom: 10px;
    }
    .stTextInput label, .stTextArea label {
        font-size: 16px;
        font-weight: bold;
        color: #2C3E50;
    }
    .stButton>button {
        background: #27AE60;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #2ECC71;
    }
    .stDownloadButton>button {
        background: #E74C3C;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 10px;
        transition: 0.3s;
    }
    .stDownloadButton>button:hover {
        background: #C0392B;
    }
    .profile-img {
        display: block;
        margin: auto;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        border: 4px solid #F1C40F;
    }
    .resume-preview {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        color: #2C3E50;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='title'>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("📷 Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])
profile_pic_data = None

if profile_pic:
    profile_pic_data = base64.b64encode(profile_pic.read()).decode("utf-8")
    st.markdown(f"""
        <img src="data:image/png;base64,{profile_pic_data}" class="profile-img" />
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
        resume_html = generate_resume_text(name, email, phone, summary, skills, experience, education, profile_pic_data)

        # Resume Preview
        st.markdown("### 📜 Generated Resume")
        st.markdown(f"<div class='resume-preview'>{resume_html}</div>", unsafe_allow_html=True)

        # Download Button
        st.download_button(label="📥 Download Resume as HTML", 
                           data=resume_html, 
                           file_name="Resume.html", 
                           mime="text/html")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
        
