import streamlit as st
import openai
import fpdf from FPDF

# Set OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Page Config
st.set_page_config(page_title="🚀 AI Resume & Cover Letter Generator", page_icon="📄", layout="centered")

# Custom Styles
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stApp {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2E86C1;
            text-align: center;
        }
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📄 AI-Powered Resume & Cover Letter Generator 🚀")

# User Input Form
st.markdown("### ✨ Enter Your Details Below:")
with st.form("resume_form"):
    name = st.text_input("🔹 Your Full Name")
    job_title = st.text_input("🔹 Job Title You're Applying For")
    skills = st.text_area("🔹 List Your Skills (comma-separated)")
    experience = st.text_area("🔹 Work Experience (Describe your past jobs)")
    education = st.text_area("🔹 Educational Background")
    submit_button = st.form_submit_button("Generate Resume & Cover Letter")

if submit_button:
    if name and job_title and skills and experience and education:
        with st.spinner("⏳ Generating Resume & Cover Letter..."):
            prompt = f"Generate a professional resume for {name} applying for {job_title}. Skills: {skills}. Experience: {experience}. Education: {education}."

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}]
            )

            resume_text = response["choices"][0]["message"]["content"]

        st.subheader("📜 Your AI-Generated Resume:")
        st.markdown(f"{resume_text}")

        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, resume_text)
        pdf.output("resume.pdf")

        # Download Button
        with open("resume.pdf", "rb") as file:
            st.download_button("📥 Download Resume (PDF)", file, file_name="AI_Resume.pdf")

        st.success("✅ Your AI-Powered Resume & Cover Letter is Ready!")
    else:
        st.warning("⚠️ Please fill in all details before generating your resume!")
