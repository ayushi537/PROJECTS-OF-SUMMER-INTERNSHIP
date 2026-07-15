import streamlit as st
import pickle
import pandas as pd
model = pickle.load(open("model.pkl", "rb"))
import streamlit as st
import pandas as pd
import pickle

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

# -------------------- LOAD MODEL --------------------
model = pickle.load(open("model.pkl", "rb"))

# -------------------- CSS --------------------
st.markdown("""
<style>
.stApp{
    background-color:#0E1117;
    color:white;
}
h1{
    text-align:center;
    color:#00E5FF;
}
div.stButton > button{
    width:100%;
    background:#00C853;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:50px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏦 Loan Approval Prediction")

st.write("Enter applicant details below.")

# -------------------- INPUTS --------------------
col1, col2 = st.columns(2)

with col1:
    person_age = st.number_input("Age", 18, 100, 25)

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    education = st.selectbox(
        "Education",
        ["Associate", "Bachelor", "Doctorate", "High School", "Master"]
    )

    income = st.number_input(
        "Annual Income",
        min_value=0.0
    )

    emp_exp = st.number_input(
        "Employment Experience",
        min_value=0
    )

    home = st.selectbox(
        "Home Ownership",
        ["MORTGAGE", "OTHER", "OWN", "RENT"]
    )

with col2:

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0
    )

    loan_intent = st.selectbox(
        "Loan Purpose",
        [
            "DEBTCONSOLIDATION",
            "EDUCATION",
            "HOMEIMPROVEMENT",
            "MEDICAL",
            "PERSONAL",
            "VENTURE"
        ]
    )

    interest_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0
    )

    percent_income = st.number_input(
        "Loan % of Income",
        min_value=0.0
    )

    credit_history = st.number_input(
        "Credit History Length",
        min_value=0.0
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=650
    )

    previous_default = st.selectbox(
        "Previous Loan Default",
        ["No", "Yes"]
    )

# -------------------- MAPPINGS --------------------

gender_map = {
    "Female": 0,
    "Male": 1
}

education_map = {
    "Associate": 0,
    "Bachelor": 1,
    "Doctorate": 2,
    "High School": 3,
    "Master": 4
}

home_map = {
    "MORTGAGE": 0,
    "OTHER": 1,
    "OWN": 2,
    "RENT": 3
}

loan_map = {
    "DEBTCONSOLIDATION": 0,
    "EDUCATION": 1,
    "HOMEIMPROVEMENT": 2,
    "MEDICAL": 3,
    "PERSONAL": 4,
    "VENTURE": 5
}

default_map = {
    "No": 0,
    "Yes": 1
}

# -------------------- PREDICT --------------------

if st.button("Predict Loan Status"):

    data = pd.DataFrame([{
        "person_age": person_age,
        "person_gender": gender_map[gender],
        "person_education": education_map[education],
        "person_income": income,
        "person_emp_exp": emp_exp,
        "person_home_ownership": home_map[home],
        "loan_amnt": loan_amount,
        "loan_intent": loan_map[loan_intent],
        "loan_int_rate": interest_rate,
        "loan_percent_income": percent_income,
        "cb_person_cred_hist_length": credit_history,
        "credit_score": credit_score,
        "previous_loan_defaults_on_file": default_map[previous_default]
    }])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("✅ Congratulations! Loan Approved")
        st.balloons()
    else:
        st.error("❌ Sorry! Loan Rejected")