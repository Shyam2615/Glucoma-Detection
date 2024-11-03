import streamlit as st
import pickle

# Load the model
def load_model():
    with open('rf_model_no_risk.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Prediction function
def predict_glaucoma(model, Rl, ocular_pressure, Md, Psd, Ght, cornea_thickness, Rnfl4, age_group_under_40, age_group_40_60, age_group_over_60):
    prediction = model.predict([[Rl, ocular_pressure, Md, Psd, Ght, cornea_thickness, Rnfl4, age_group_under_40, age_group_40_60, age_group_over_60]])
    return prediction

# Streamlit UI
st.title("Glaucoma Risk Prediction")

st.header("Patient Information")
st.write("Please enter the following details to assess glaucoma risk:")

# Input fields
Rl = st.text_input('Retinal Layer Thickness (Rl)', 'Enter value')
ocular_pressure = st.text_input('Ocular Pressure', 'Enter value')
Md = st.text_input('Mean Deviation (MD)', 'Enter value')
Psd = st.text_input('Pattern Standard Deviation (PSD)', 'Enter value')
Ght = st.text_input('Generalized Horizontal Thickness (GHT)', 'Enter value')
cornea_thickness = st.text_input('Cornea Thickness', 'Enter value')
Rnfl4 = st.text_input('Retinal Nerve Fiber Layer Thickness (RNFL4)', 'Enter value')

# Age group selection
st.write("Select Age Group:")
age_group_under_40 = st.radio('Under 40 years', ["Yes", "No"])
age_group_40_60 = st.radio('40-60 years', ["Yes", "No"])
age_group_over_60 = st.radio('Over 60 years', ["Yes", "No"])

# Convert age group selections to binary values
age_group_under_40 = 1 if age_group_under_40 == 'Yes' else 0
age_group_40_60 = 1 if age_group_40_60 == 'Yes' else 0
age_group_over_60 = 1 if age_group_over_60 == 'Yes' else 0

# Load model and make prediction
model = load_model()
if st.button('Predict'):
    result = predict_glaucoma(model, Rl, ocular_pressure, Md, Psd, Ght, cornea_thickness, Rnfl4, age_group_under_40, age_group_40_60, age_group_over_60)
    if result == 0:
        st.success("No risk of glaucoma detected.")
    else:
        st.warning("There is a risk of glaucoma.")
