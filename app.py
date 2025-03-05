import streamlit as st
from fpdf import FPDF

def generate_pdf(name, email, phone, summary, skills, experience, education):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=20)
    pdf.cell(200, 10, name, ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, email + " | " + phone, ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(0, 10, "Professional Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, summary)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, skills)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(0, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, experience)
    pdf.ln(5)
    
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, education)
    
    pdf_file = "resume.pdf"
    pdf.output(pdf_file)
    return pdf_file

st.set_page_config(page_title="Resume Generator", page_icon="📄", layout="centered")
st.title("📄 Professional Resume Generator")

st.write("Fill out the details below to generate your resume.")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (separate by commas)")
experience = st.text_area("Work Experience")
education = st.text_area("Education")

if st.button("Generate Resume PDF 📄"):
    if name and email and phone and summary and skills and experience and education:
        pdf_file = generate_pdf(name, email, phone, summary, skills, experience, education)
        with open(pdf_file, "rb") as file:
            st.download_button(label="Download Resume 📥", data=file, file_name="Resume.pdf", mime="application/pdf")
    else:
        st.warning("⚠️ Please fill in all fields before generating your resume!")
