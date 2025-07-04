import streamlit as st
import requests
import pandas as pd

API_URL = "https://crop-recommendation-system-28wj.onrender.com/predict"
"
st.set_page_config(page_title="Crop Recommendation System", page_icon="🌾")
st.title("Crop Recommendation System 🌾")
st.markdown("Enter your soil and weather conditions to get crop recommendations.")
with st.form("crop_form"):
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=500, step=1)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=500, step=1)
    K = st.number_input("Potassium (K)", min_value=0, max_value=500, step=1)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
    city = st.text_input("Enter your city (e.g., Jaipur)")
    submit = st.form_submit_button(" Recommend Crop")

if submit:
    if not city:
        st.warning("Please enter a city name.")
    else:
        with st.spinner("Fetching weather & predicting..."):
            try:
                # Send data to FastAPI
                payload = {
                    "N": N,
                    "P": P,
                    "K": K,
                    "ph": ph,
                    "city": city
                }
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ Recommended Crop: **{data['predicted_crop'].capitalize()}**")
                    st.info(f"🌱 Why: {data['why']}")
                else:
                    st.error(f"❌ Failed: {response.json()['detail']}")
            except Exception as e:
                st.error(f"Error: {e}")
