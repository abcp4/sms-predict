import streamlit as st
import streamlit.components.v1 as components
import requests
import os

"""
## LIME Explainer Dashboard for SMS Spam Detection

It is a web application that allows you to visualize the explanation of a prediction made by a trained model.
Each prediction is explained using LIME. The explanation is based on the model's predictions and the text of the SMS.
"""
input_text = st.text_area("Enter your text:", "", max_chars=256, height=100)

API_URL = os.getenv("API_URL", "http://localhost:8000")

if st.button("Explain Results"):
    with st.spinner('Calculating...'):
        r = requests.get(
            os.path.join(API_URL, "predict"),
            params={"text": input_text},
        )
        result = r.json()
        components.html(result['html'], height=800)
