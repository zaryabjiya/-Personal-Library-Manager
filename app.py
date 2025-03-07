import streamlit as st
from fpdf import FPDF
import base64

# Function to Generate PDF
def generate_pdf(name, email, phone, summary, skills, experience, education, profile_pic_encoded):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set Font
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(25, 25, 112)  # Dark Blue
    pdf.cell(200, 10, name, ln=True, align="C")

    # Profile Picture
    if profile_pic_encoded:
        profile_path = "profile_pic.png"
        with open(profile_path, "wb") as file:
            file.write(base64.b64decode(profile_pic_encoded))
        pdf.image(profile_path, x=80, y=30, w=50, h=50)
        pdf.ln(60)
    
    # Contact Details
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(0, 0, 0)  # Black
    pdf.cell(200, 10, f"📧 {email} | 📞 {phone}", ln=True, align="C")
    pdf.ln(10)

    # Sections
    sections = [("Professional Summary", summary), 
                ("Skills", skills), 
                ("Work Experience", experience), 
                ("Education", education)]

    pdf.set_font("Arial", "B", 14)
    for title, content in sections:
        pdf.set_fill_color(230, 230, 250)  # Light Blue Background
        pdf.cell(0, 10, title, ln=True, fill=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, content)
        pdf.ln(5)

    return pdf.output(dest="S").encode("latin1")

# Streamlit Page Configuration
st.set_page_config(page_title="Professional Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
        font-family: 'Arial', sans-serif;
    }
    h1 {
        color: #1565C0;
        text-align: center;
    }
    .stTextInput label, .stTextArea label {
        font-weight: bold;
        font-size: 16px;
        color: #333;
    }
    .stButton>button {
        background: #2E7D32;
        color: white;
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
        font-size: 18px;
        padding: 12px;
        transition: 0.3s;
    }
    .stDownloadButton>button:hover {
        background: #C62828;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("Upload Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
profile_pic_encoded = ""

if profile_pic:
    profile_pic_encoded = base64.b64encode(profile_pic.read()).decode("utf-8")
    st.image(profile_pic, width=150, caption="Profile Picture", use_column_width=False)

# Input Fields with Proper Headings
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Contact Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Education")

# Generate Resume Button
if st.button("Generate Resume"):
    if name and email and phone and summary and skills and experience and education:
        pdf_data = generate_pdf(name, email, phone, summary, skills, experience, education, profile_pic_encoded)
        
        # Download Button
        st.download_button(label="📥 Download Resume (PDF)", data=pdf_data, file_name="Resume.pdf", mime="application/pdf")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
        
