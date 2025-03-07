import streamlit as st
import base64

# Function to Generate Resume Text
def generate_resume_text(name, email, phone, summary, skills, experience, education, profile_pic_encoded):
    resume_content = f"""
    <div style='padding: 20px; border: 2px solid #ddd; border-radius: 10px; background: white; color: #333; font-family: Arial, sans-serif;'>
        
        <div style="text-align: center;">
            <img src="data:image/png;base64,{profile_pic_encoded}" style="border-radius: 50%; width: 120px; height: 120px; border: 3px solid #4CAF50;" />
        </div>
        
        <h1 style='text-align: center; color: #4CAF50;'>{name}</h1>
        <p style='text-align: center; font-size: 16px;'><strong>Email:</strong> {email} | <strong>Phone:</strong> {phone}</p>
        
        <h2 style='color: #4CAF50;'>Professional Summary</h2>
        <p>{summary}</p>

        <h2 style='color: #4CAF50;'>Skills</h2>
        <ul>{"".join([f"<li>{skill.strip()}</li>" for skill in skills.split(",")])}</ul>

        <h2 style='color: #4CAF50;'>Work Experience</h2>
        <p>{experience}</p>

        <h2 style='color: #4CAF50;'>Education</h2>
        <p>{education}</p>
        
    </div>
    """
    return resume_content

# Page Config
st.set_page_config(page_title="🚀 Professional Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Modern Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
        color: black;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #1565C0;
    }
    .stTextInput, .stTextArea {
        border-radius: 8px;
        border: 1px solid #90CAF9;
        padding: 12px;
        background-color: white;
        color: black;
    }
    .stButton>button {
        background: #2E7D32;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 12px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #43A047;
        transform: scale(1.05);
    }
    .stDownloadButton>button {
        background: #D32F2F;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 12px;
        transition: 0.3s;
    }
    .stDownloadButton>button:hover {
        background: #C62828;
        transform: scale(1.05);
    }
    .resume-preview {
        background: white;
        color: black;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        font-family: Arial, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='title'>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("📷 Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])
profile_pic_encoded = ""

if profile_pic:
    profile_pic_encoded = base64.b64encode(profile_pic.read()).decode("utf-8")
    st.image(profile_pic, width=150, caption="Profile Picture", use_column_width=False)

# Input Fields for Resume
name = st.text_input("📝 Full Name")
email = st.text_input("📧 Email Address")
phone = st.text_input("📞 Contact Number")
summary = st.text_area("🏆 Professional Summary")
skills = st.text_area("🔧 Skills (comma-separated)")
experience = st.text_area("💼 Work Experience")
education = st.text_area("🎓 Education")

# Generate Resume Button
if st.button("Generate Resume 📄"):
    if name and email and phone and summary and skills and experience and education:
        resume_html = generate_resume_text(name, email, phone, summary, skills, experience, education, profile_pic_encoded)
        
        # Resume Preview
        st.markdown("### 📜 Your Resume Preview:")
        st.markdown(f"<div class='resume-preview'>{resume_html}</div>", unsafe_allow_html=True)
        
        # Download Button
        st.download_button(label="📥 Download Resume as HTML", data=resume_html, file_name="Resume.html", mime="text/html")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
