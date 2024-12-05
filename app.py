import streamlit as st
import pickle
import numpy as np

# Load the model
with open("Dorimodel.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Dori Tavsiya Qilish Tizimi")

# Input form
st.header("Bemorning parametrlarini kiriting")
age = st.number_input("Yoshi", min_value=10, max_value=80, step=1)
sex = st.selectbox("Jinsi", options=["Erkak", "Ayol"])
bp = st.selectbox("Qon bosimi (BP)", options=["Past", "NORMAL", "YUQORI"])
cholesterol = st.selectbox("Xolesterin darajasi", options=["NORMAL", "BALAND"])
na_to_k = st.number_input("Natriy va kaliy nisbati", min_value=6.0, max_value=40.0, step=0.1)

# Map categorical inputs to numeric
sex_map = {"M": 0, "F": 1}
bp_map = {"LOW": 0, "NORMAL": 1, "HIGH": 2}
cholesterol_map = {"NORMAL": 0, "HIGH": 1}

# Prepare features for prediction
features = np.array([[age, sex_map[sex], bp_map[bp], cholesterol_map[cholesterol], na_to_k]])
predicted_drug = model.predict(features)

# Map prediction to drug name
drug_map = {0: "drugA", 1: "drugB", 2: "drugC", 3: "drugX", 4: "drugY"}
predicted_drug_category = int(round(predicted_drug[0]))  # Convert float to nearest integer
st.subheader(f"Tavsiya etilgan dori: {drug_map[predicted_drug_category]}")