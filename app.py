import streamlit as st
from fpdf import FPDF
import base64

# Function to generate PDF Resume
class PDF(FPDF):
    def header(self):
        if profile_pic:
            self.image("profile.jpg", 10, 8, 33)  # Profile Image at the Top
        self.set_font("Arial", "B", 18)
        self.cell(200, 10, name, ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(2)
        self.set_font("Arial", "", 11)
        self.set_text_color(80, 80, 80)

def generate_pdf():
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 10, f"📧 {email}  |  📞 {phone}", ln=True, align="C")
    pdf.ln(5)

    pdf.section_title("🏆 Professional Summary")
    pdf.multi_cell(0, 8, summary)
    pdf.ln(5)

    pdf.section_title("🔧 Skills")
    pdf.multi_cell(0, 8, skills)
    pdf.ln(5)

    pdf.section_title("💼 Work Experience")
    pdf.multi_cell(0, 8, experience)
    pdf.ln(5)

    pdf.section_title("🎓 Education")
    pdf.multi_cell(0, 8, education)
    pdf.ln(5)

    pdf.output("resume.pdf")

    with open("resume.pdf", "rb") as f:
        pdf_data = f.read()
    return pdf_data

# Page Configuration
st.set_page_config(page_title="🚀 Resume Generator", page_icon="📄", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp { background: #f4f4f4; color: #333; font-family: Arial, sans-serif; }
    .title { text-align: center; font-size: 36px; font-weight: bold; color: #2C3E50; }
    .stTextInput>label, .stTextArea>label { font-weight: bold; font-size: 16px; }
    .stButton>button { background: #3498DB; color: white; font-size: 18px; padding: 10px; border-radius: 5px; }
    .stButton>button:hover { background: #2980B9; transform: scale(1.05); }
    .stDownloadButton>button { background: #E74C3C; color: white; font-size: 18px; padding: 10px; border-radius: 5px; }
    .stDownloadButton>button:hover { background: #C0392B; transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='title'>📄 Professional Resume Generator</h1>", unsafe_allow_html=True)

# Profile Picture Upload
profile_pic = st.file_uploader("Upload Your Profile Picture (Optional)", type=["jpg", "jpeg", "png"])

if profile_pic:
    with open("profile.jpg", "wb") as f:
        f.write(profile_pic.read())
    st.image("profile.jpg", width=150)

# Input Fields for Resume
name = st.text_input("👤 Full Name")
email = st.text_input("📧 Email Address")
phone = st.text_input("📞 Phone Number")
summary = st.text_area("🏆 Professional Summary")
skills = st.text_area("🔧 Skills (Comma-Separated)")
experience = st.text_area("💼 Work Experience")
education = st.text_area("🎓 Education")

# Generate Resume Button
if st.button("Generate Resume 📄"):
    if name and email and phone and summary and skills and experience and education:
        pdf_data = generate_pdf()
        st.success("✅ Resume Generated Successfully!")

        # Show Download Button
        st.download_button(
            label="📥 Download Resume as PDF",
            data=pdf_data,
            file_name="Resume.pdf",
            mime="application/pdf",
        )
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
