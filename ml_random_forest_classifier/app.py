import streamlit as st
import pickle
import numpy as np

# Load model and encoders
model = pickle.load(open("rf_model.pkl", "rb"))
state_encoder = pickle.load(open("state_encoder.pkl", "rb"))
crop_encoder = pickle.load(open("crop_encoder.pkl", "rb"))

st.set_page_config(page_title="Crop Recommendation", page_icon="🌱")

st.title("🌱 Crop Recommendation System")

st.write("Enter the details below to predict the recommended crop.")

# Inputs
n = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=90)
p = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=40)
k = st.number_input("Potassium (K)", min_value=0, max_value=200, value=40)

temperature = st.number_input("Temperature (°C)", value=25.0)

humidity = st.number_input("Humidity (%)", value=80.0)

ph = st.number_input("Soil pH", value=6.5)

rainfall = st.number_input("Rainfall (mm)", value=200.0)

# State dropdown
state = st.selectbox(
    "Select State",
    state_encoder.classes_
)

crop_price = st.number_input("Crop Price (₹)", value=5000)

if st.button("Predict Crop"):

    # Convert state name to encoded number
    state_encoded = state_encoder.transform([state])[0]

    # Arrange inputs in the same order used during training
    input_data = np.array([[
        n,
        p,
        k,
        temperature,
        humidity,
        ph,
        rainfall,
        state_encoded,
        crop_price
    ]])

    # Predict encoded crop
    prediction = model.predict(input_data)

    # Convert encoded crop to crop name
    crop_name = crop_encoder.inverse_transform(prediction.astype(int))[0]

    st.success(f"🌾 Recommended Crop: {crop_name}")