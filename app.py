import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("ML Model Deployment")

val = st.number_input("Enter value")

if st.button("Predict"):
    result = model.predict([[val]])
    st.write("Prediction:", result[0])