# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:03:42 2026

@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

riding_model = pickle.load(open("Riding_model.sav",'rb'))
loan_model = pickle.load(open("loan_model.sav",'rb'))
bmi_model = pickle.load(open("bmi_model.sav",'rb')) # โหลดมาเป็น bmi_model (ตัวเล็ก)


with st.sidebar:
    selected = option_menu(
        'Classification',['Loan','Riding','BMI']
        )

gender_map = {
    'Male':1,
    'Female':0
    }

education_map = {
    'Associate': 0,
    'Bachelor': 1,
    'Doctorate': 2,
    'High School': 3,
    'Master': 4
}

home_map = {
    'MORTGAGE': 0,
    'OTHER': 1,
    'OWN': 2,
    'RENT': 3
}

intent_map = {
    'DEBTCONSOLIDATION': 0,
    'EDUCATION': 1,
    'HOMEIMPROVEMENT': 2,
    'MEDICAL': 3,
    'PERSONAL': 4,
    'VENTURE': 5
}

default_map = {
    'No': 0,
    'Yes': 1
}

# ---------------------------------------------------------
# ส่วนของ BMI
# ---------------------------------------------------------
if (selected == 'BMI'):
    st.title('BMI Classification')
    person_gender = st.selectbox('Gender', gender_map)
    height = st.number_input('Height (cm)', min_value=0.0)
    weight = st.number_input('Weight (kg)', min_value=0.0)
    
    BMI_prediction = ''
    if st.button('Predict'):
        # แก้ไขจาก BMI_model เป็น bmi_model ให้ตรงกับที่โหลดไว้ด้านบน
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
        elif prediction[0] ==
