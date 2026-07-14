import streamlit as st
import pickle

# Load model
model = pickle.load(open("Weather_Temperature_Model.pkl", "rb"))

st.title("🌦️ Weather Temperature Prediction")

prcp = st.number_input("Precipitation (prcp)")
tmin = st.number_input("Minimum Temperature (tmin)")
tmax = st.number_input("Maximum Temperature (tmax)")

if st.button("Predict Temperature"):
    #  FIX: Rearranged to match the training data order: tmin, tmax, prcp
    prediction = model.predict([[tmin, tmax, prcp]])[0]

    st.success(f"Predicted Average Temperature: {prediction:.2f} °C")

    if prediction >= 30:
        st.warning("🌞 Weather: Hot Day")
    elif prediction >= 20:
        st.info("🌤️ Weather: Pleasant Day")
    else:
        st.error("❄️ Weather: Cold Day")