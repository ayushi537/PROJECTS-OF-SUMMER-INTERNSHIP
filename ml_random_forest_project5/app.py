import streamlit as st
import pandas as pd
import pickle

# ---------------- Load Model ----------------

model = pickle.load(open("model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details below and click Predict Price.")

st.divider()

# ---------------- User Inputs ----------------

make_year = st.number_input(
    "Manufacturing Year",
    min_value=1995,
    max_value=2026,
    value=2020
)

mileage = st.number_input(
    "Mileage (km/l)",
    min_value=5.0,
    max_value=40.0,
    value=18.0
)

engine = st.number_input(
    "Engine CC",
    min_value=800,
    max_value=5000,
    value=1200
)

owner = st.selectbox(
    "Number of Owners",
    [1, 2, 3, 4]
)

fuel = st.selectbox(
    "Fuel Type",
    encoders["fuel_type"].classes_
)

brand = st.selectbox(
    "Brand",
    encoders["brand"].classes_
)

transmission = st.selectbox(
    "Transmission",
    encoders["transmission"].classes_
)

color = st.selectbox(
    "Color",
    encoders["color"].classes_
)

service = st.selectbox(
    "Service History",
    encoders["service_history"].classes_
)

accidents = st.selectbox(
    "Accidents Reported",
    [0, 1]
)

insurance = st.selectbox(
    "Insurance Valid",
    encoders["insurance_valid"].classes_
)

# ---------------- Predict ----------------

if st.button("Predict Price"):

    fuel = encoders["fuel_type"].transform([fuel])[0]
    brand = encoders["brand"].transform([brand])[0]
    transmission = encoders["transmission"].transform([transmission])[0]
    color = encoders["color"].transform([color])[0]
    service = encoders["service_history"].transform([service])[0]
    insurance = encoders["insurance_valid"].transform([insurance])[0]

    data = pd.DataFrame([[
        make_year,
        mileage,
        engine,
        fuel,
        owner,
        brand,
        transmission,
        color,
        service,
        accidents,
        insurance
    ]], columns=[
        "make_year",
        "mileage_kmpl",
        "engine_cc",
        "fuel_type",
        "owner_count",
        "brand",
        "transmission",
        "color",
        "service_history",
        "accidents_reported",
        "insurance_valid"
    ])

    prediction = model.predict(data)

    st.success(f"💰 Estimated Car Price: ${prediction[0]:,.2f}")

st.divider()
st.caption("Built with Streamlit & Random Forest Regressor")