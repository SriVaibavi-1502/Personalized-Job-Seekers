import streamlit as st

st.set_page_config(
    page_title="Job Seekers",
    page_icon="💼",
    layout="centered"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #eaf4ff;
}

.block-container {
    max-width: 750px;
    padding-top: 40px;
    padding-bottom: 40px;
}

h1 {
    text-align: center;
    color: #000000 !important;
    font-size: 40px !important;
    font-weight: 700;
}

h2 {
    text-align: center;
    color: #000000 !important;
}

h3 {
    color: #000000 !important;
    margin-top: 25px;
}

p {
    color: #000000 !important;
}

label {
    color: #000000 !important;
    font-weight: 500 !important;
}

.stTextInput input,
.stTextArea textarea {
    background-color: white;
    color: black;
    border: 1px solid #7aa7d9;
    border-radius: 8px;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #2563a6;
}

.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    border-radius: 8px;
}

.stRadio label,
.stCheckbox label {
    color: #000000 !important;
}

[data-testid="stFileUploader"] {
    background-color: white;
    border: 1px solid #7aa7d9;
    border-radius: 8px;
    padding: 10px;
}

.stButton > button {
    width: 100%;
    background-color: #2563a6;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 11px;
    font-size: 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #174a7c;
}

.job-info {
    background-color: white;
    border-left: 5px solid #2563a6;
    padding: 18px;
    border-radius: 8px;
    margin-top: 20px;
    margin-bottom: 25px;
}

.job-info h4 {
    color: #000000;
    margin-top: 0;
}

.job-info p {
    color: #334155 !important;
    margin-bottom: 5px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- App ----------------

st.title("💼 Job Seekers")

st.header("Welcome to our Job Seekers App!")

st.subheader("Find Your Next Opportunity 🚀")

st.markdown(
    """
    <p style="
        color: #334155 !important;
        font-size: 16px;
        line-height: 1.6;
    ">
        Hey Guys! Here you can explore job opportunities
        based on your skills, interests and preferred work style.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("**Job Seekers**")

st.caption("Find Jobs • Build Your Career • Make Your Future")


# ---------------- About App ----------------

st.markdown("""
<div class="job-info">

<h4>💼 What can you do with this app?</h4>

<p>• Find jobs based on your field</p>
<p>• Select your preferred job type</p>
<p>• Choose your skills</p>
<p>• Select your experience level</p>
<p>• Set your expected salary</p>
<p>• Upload your resume</p>
<p>• Get suitable job opportunities</p>

</div>
""", unsafe_allow_html=True)


# ---------------- Personal Details ----------------

st.subheader("👤 Your Details")

name = st.text_input("Enter your name")

message = st.text_area("Tell us about yourself")


# ---------------- Job Preferences ----------------

st.subheader("🔎 Job Preferences")

field = st.selectbox(
    "Choose your field",
    ["AIML", "CSE", "Data Science", "Web Development", "Other"]
)

skills = st.multiselect(
    "Select your skills",
    [
        "Python",
        "Java",
        "C++",
        "Machine Learning",
        "Data Science",
        "HTML & CSS",
        "SQL"
    ]
)

job_type = st.radio(
    "Choose your preferred job type",
    ["Internship", "Full Time", "Part Time"]
)

work_option = st.multiselect(
    "Choose your preferred work option",
    ["Work From Home", "Office", "Hybrid"]
)

experience = st.selectbox(
    "Select your experience level",
    ["Fresher", "0-1 Years", "1-3 Years", "3+ Years"]
)

location = st.text_input(
    "Enter your preferred job location"
)

salary = st.number_input(
    "Enter your expected salary (₹ per month)",
    min_value=0,
    step=500
)


# ---------------- Resume ----------------

st.subheader("📄 Resume")

file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# ---------------- Agreement ----------------

agree = st.checkbox(
    "I agree to receive job opportunities"
)


# ---------------- Search Button ----------------

if st.button("🔍 Find Job Opportunities"):

    if name == "":
        st.warning("Please enter your name.")

    elif field == "":
        st.warning("Please select your field.")

    else:
        st.success(
            "Your details have been submitted successfully! "
            "Suitable job opportunities will be shown here."
        )