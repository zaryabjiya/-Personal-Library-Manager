import streamlit as st

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
st.title("📄 Simple Resume Generator")

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
