import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Phishing Website Detector")
st.write("Select the website details below and click Predict.")

st.divider()

# ---------------- Inputs ----------------

using_ip = st.selectbox(
    "Does the website use an IP address instead of a domain name?",
    ["No", "Yes"]
)

long_url = st.selectbox(
    "Is the website URL very long?",
    ["No", "Yes"]
)

https = st.selectbox(
    "Does the website use HTTPS?",
    ["Yes", "No"]
)

domain_reg = st.selectbox(
    "Domain Registration Period",
    ["Long", "Short"]
)

age_domain = st.selectbox(
    "Website Age",
    ["Old", "New"]
)

traffic = st.selectbox(
    "Website Popularity",
    ["Low", "Medium", "High"]
)

google = st.selectbox(
    "Can you find this website on Google?",
    ["Yes", "No"]
)

page_rank = st.selectbox(
    "Website Reputation",
    ["Low", "Medium", "High"]
)

# ---------------- Convert Values ----------------

using_ip = 1 if using_ip == "Yes" else -1

long_url = 1 if long_url == "Yes" else -1

https = 1 if https == "Yes" else -1

domain_reg = 1 if domain_reg == "Long" else -1

age_domain = 1 if age_domain == "Old" else -1

traffic = {
    "Low": -1,
    "Medium": 0,
    "High": 1
}[traffic]

google = 1 if google == "Yes" else -1

page_rank = {
    "Low": -1,
    "Medium": 0,
    "High": 1
}[page_rank]

# ---------------- Prediction ----------------

if st.button("🔍 Predict Website"):

    data = pd.DataFrame([[
        using_ip,
        long_url,
        https,
        domain_reg,
        age_domain,
        traffic,
        google,
        page_rank
    ]], columns=[
        "UsingIP",
        "LongURL",
        "HTTPS",
        "DomainRegLen",
        "AgeofDomain",
        "WebsiteTraffic",
        "GoogleIndex",
        "PageRank"
    ])

    prediction = model.predict(data)

    st.write("Prediction Value:", prediction[0])   # For debugging

    st.divider()

    if prediction[0] == 1:
        st.success("✅ Legitimate Website")
    else:
        st.error("⚠️ Phishing Website Detected")

st.divider()
st.caption("Built using Streamlit & Decision Tree Classifier")