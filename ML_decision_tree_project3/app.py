import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Mobile Price Prediction", page_icon="📱")

st.title("📱 Mobile Price Range Prediction")
st.write("Enter the mobile specifications below to predict its price range.")

battery_power = st.number_input("Battery Power (mAh)", min_value=500, max_value=2500, value=1500)
blue = st.selectbox("Bluetooth", [0, 1])
clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.5, max_value=3.5, value=2.0)
fc = st.number_input("Front Camera (MP)", min_value=0, max_value=25, value=5)
int_memory = st.number_input("Internal Memory (GB)", min_value=2, max_value=128, value=32)
m_dep = st.number_input("Mobile Depth (cm)", min_value=0.1, max_value=1.0, value=0.5)
mobile_wt = st.number_input("Mobile Weight (g)", min_value=80, max_value=250, value=150)
n_cores = st.number_input("Number of Cores", min_value=1, max_value=8, value=4)
pc = st.number_input("Primary Camera (MP)", min_value=0, max_value=30, value=12)
px_height = st.number_input("Pixel Height", min_value=0, max_value=2000, value=800)
px_width = st.number_input("Pixel Width", min_value=0, max_value=3000, value=1200)
ram = st.number_input("RAM (MB)", min_value=256, max_value=8000, value=4000)
sc_h = st.number_input("Screen Height", min_value=5, max_value=25, value=12)
sc_w = st.number_input("Screen Width", min_value=1, max_value=20, value=7)
talk_time = st.number_input("Talk Time (Hours)", min_value=2, max_value=30, value=10)
touch_screen = st.selectbox("Touch Screen", [0, 1])

if st.button("Predict Price Range"):

    features = np.array([[battery_power,
                          blue,
                          clock_speed,
                          fc,
                          int_memory,
                          m_dep,
                          mobile_wt,
                          n_cores,
                          pc,
                          px_height,
                          px_width,
                          ram,
                          sc_h,
                          sc_w,
                          talk_time,
                          touch_screen]])

    prediction = model.predict(features)[0]

    if prediction == 0:
        st.success("💰 Price Range: Low Cost")
    elif prediction == 1:
        st.success("💰 Price Range: Medium Cost")
    elif prediction == 2:
        st.success("💰 Price Range: High Cost")
    else:
        st.success("💰 Price Range: Very High Cost")