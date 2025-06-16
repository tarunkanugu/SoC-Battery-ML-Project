# 🔋 SoC Battery ML Project — Predicting Battery State of Charge in PV Systems for the Mining Sector

![Project Banner](A_project_showcase_banner_in_digital_graphic_desig.png)

## 📌 Problem Statement

In remote mining operations, ensuring uninterrupted power supply from **photovoltaic (PV) systems** is critical. Batteries store excess solar energy, but **inefficient battery management** can cause energy waste or power loss.

This project uses **supervised machine learning** to predict the **State of Charge (SoC)** of batteries in real time — helping improve energy efficiency, reduce maintenance, and extend battery lifespan in mining sites.

---

## ⚙️ Technologies Used

- **Python** 🐍
- **Pandas / NumPy / scikit-learn** 📊
- **Streamlit** for Web UI 🌐
- **Android WebView** for mobile app deployment 📱
- **Git & GitHub** for version control 🌍

---

## 📈 Machine Learning Model

We trained a **Random Forest Regressor** using synthetic data that mimics real-world parameters collected from PV systems:

### 📥 Input Features:
- PV Output Power (W)
- Battery Voltage (V)
- Battery Current (A)
- Temperature (°C)
- Load (W)

### 📤 Output:
- State of Charge (SoC) %

The model was trained on a large dataset and saved as `model.pkl` for real-time predictions in a Streamlit app.

---

## 📊 Streamlit Web App

An interactive web interface was built using Streamlit where users can:

- Input sensor values (PV power, current, voltage, etc.)
- Get real-time prediction of SoC
- Understand battery health and plan accordingly

To run the app:

```bash
streamlit run app.py
