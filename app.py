import streamlit as st
import pickle

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Streamlit app
st.title("Health Prediction System")

# Select the model
model_choice = st.sidebar.selectbox("Choose the model:", ["Diabetes", "Heart Disease", "Parkinson's"])

if model_choice == "Diabetes":
    st.write("## Diabetes Prediction")
    # Add diabetes-specific inputs and predictions here
elif model_choice == "Heart Disease":
    st.write("## Heart Disease Prediction")
    # Add heart-disease-specific inputs and predictions here
else:
    st.write("## Parkinson's Prediction")
    # Add Parkinson's-specific inputs and predictions here
