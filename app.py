# app.py

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("soc_model.pkl")

st.set_page_config(page_title="Battery SoC Predictor", page_icon="🔋")
st.title("🔋 Battery State of Charge Predictor")
st.write("Predict SoC for batteries in photovoltaic systems (Mining Sector)")

# User inputs
voltage = st.number_input("Voltage (V)", min_value=0.0, max_value=100.0, value=48.0)
current = st.number_input("Current (A)", min_value=0.0, max_value=100.0, value=10.0)
irradiance = st.number_input("Irradiance (W/m²)", min_value=0.0, max_value=1500.0, value=800.0)
temperature = st.number_input("Temperature (°C)", min_value=-20.0, max_value=60.0, value=25.0)
power = st.number_input("PV Output Power (W)", min_value=0.0, max_value=10000.0, value=1200.0)
time = st.number_input("Time of Day (Hour)", min_value=0.0, max_value=23.99, value=12.0)

# Predict
if st.button("🔍 Predict SoC"):
    input_data = np.array([[voltage, current, irradiance, temperature, power, time]])
    soc_pred = model.predict(input_data)[0]
    st.success(f"🔋 Predicted State of Charge: {soc_pred:.2f}%")
