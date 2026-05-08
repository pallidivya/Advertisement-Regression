import streamlit as st
import numpy as np
import pickle

# Page Config
st.set_page_config(
    page_title="Advertising Sales Prediction",
    page_icon="📈",
    layout="centered"
)

# Title
st.title("📈 Advertising Sales Prediction")
st.write("Predict product sales using advertising budgets")

# Load model
with open("advertising_model.pkl", "rb") as f:
    artifact = pickle.load(f)

model = artifact["model"]
scaler = artifact["scaler"]

# Sidebar
st.sidebar.header("Enter Advertising Budget")

tv = st.sidebar.slider("TV Budget", 0.0, 300.0, 100.0)
radio = st.sidebar.slider("Radio Budget", 0.0, 50.0, 25.0)
newspaper = st.sidebar.slider("Newspaper Budget", 0.0, 120.0, 10.0)

# Prediction Button
if st.button("Predict Sales"):

    input_data = np.array([[tv, radio, newspaper]])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)[0]

    st.success(f"Predicted Sales: {prediction:.2f} units")

    st.subheader("Entered Budgets")
    st.write(f"TV: {tv}")
    st.write(f"Radio: {radio}")
    st.write(f"Newspaper: {newspaper}")