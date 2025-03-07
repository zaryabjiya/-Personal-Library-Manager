import streamlit as st
import base64

# Configure Page
st.set_page_config(page_title="Professional Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Modern Styling
st.markdown("""
    <style>
    /* Vibrant Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #3498DB, #8E44AD);
        color: white;
        font-family: 'Arial', sans-serif;
        padding: 20px;
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
    /* Buttons */
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
        background: white;
        color: black;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        font-family: 'Arial', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])

if profile_pic:
    profile_pic_encoded = base64.b64encode(profile_pic.read()).decode("utf-8")
    st.markdown(f"""
        <img src="data:image/png;base64,{profile_pic_encoded}" class="profile-img" />
    """, unsafe_allow_html=True)

# Input Fields
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Education")

# Generate Resume Button
if st.button("Generate Resume"):
    if name and email and phone and summary and skills and experience and education:
        st.markdown("### 📜 Generated Resume Preview")
        st.markdown(f"""
        <div class='resume-preview'>
            <h2>{name}</h2>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone:</strong> {phone}</p>
            <h3>🏆 Professional Summary</h3>
            <p>{summary}</p>
            <h3>🔧 Skills</h3>
            <p>{skills}</p>
            <h3>💼 Work Experience</h3>
            <p>{experience}</p>
            <h3>🎓 Education</h3>
            <p>{education}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
        
