# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:03:42 2026

@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load Models
riding_model = pickle.load(open("Riding_model.sav", 'rb'))
loan_model = pickle.load(open("loan_model.sav", 'rb'))
bmi_model = pickle.load(open("bmi_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu(
        'Classification', ['Loan', 'Riding', 'BMI']
    )

# Dictionaries
gender_map = {'Male': 1, 'Female': 0}
education_map = {'Associate': 0, 'Bachelor': 1, 'Doctorate': 2, 'High School': 3, 'Master': 4}
home_map = {'MORTGAGE': 0, 'OTHER': 1, 'OWN': 2, 'RENT': 3}
intent_map = {'DEBTCONSOLIDATION': 0, 'EDUCATION': 1, 'HOMEIMPROVEMENT': 2, 'MEDICAL': 3, 'PERSONAL': 4, 'VENTURE': 5}
default_map = {'No': 0, 'Yes': 1}

# ----------------- BMI Section -----------------
if selected == 'BMI':
    st.title('BMI Classification')
    person_gender = st.selectbox('Gender', list(gender_map.keys()))
    height = st.number_input('Height (cm)', min_value=0.0, value=170.0)
    weight = st.number_input('Weight (kg)', min_value=0.0, value=60.0)
    
    BMI_prediction = ''
    if st.button('Predict'):
        # แก้ไข BMI_model เป็น bmi_model
        prediction = bmi_model.predict([
            [
                gender_map[person_gender],
                float(height),
                float(weight)
            ]
        ])
        
        if prediction[0] == 0:
            BMI_prediction = 'Extremely Weak'
        elif prediction[0] == 1:
            BMI_prediction = 'Weak'
        elif prediction[0] == 2:
            BMI_prediction = 'Normal'
        elif prediction[0] == 3:
            BMI_prediction = 'Overweight'
        elif prediction[0] == 4:
            BMI_prediction = 'Obesity'
        elif prediction[0] == 5:
            BMI_prediction = 'Extreme Obesity'
            
        st.success(f"Result: {BMI_prediction}")

# ----------------- Loan Section -----------------
if selected == 'Loan':
    st.title('Loan Classification')
    person_age = st.text_input('person_age', '0')
    person_gender = st.selectbox('person_gender', list(gender_map.keys()))
    person_education = st.selectbox('person_education', list(education_map.keys()))
    person_income = st.text_input('person_income', '0') 
    person_emp_exp = st.text_input('person_emp_exp', '0')
    person_home_ownership = st.selectbox('person_home_ownership', list(home_map.keys()))
    loan_amnt = st.text_input('loan_amnt', '0')
    loan_intent = st.selectbox('loan_intent', list(intent_map.keys()))
    loan_int_rate = st.text_input('loan_int_rate', '0.0')
    loan_percent_income = st.text_input('loan_percent_income', '0.0')
    cb_person_cred_hist_length = st.text_input('cb_person_cred_hist
