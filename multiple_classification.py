if (selected == 'BMI'):
    st.title('BMI Classification')
    person_gender = st.selectbox('Gender', ['Male', 'Female'])
    person_height = st.number_input('Height (cm)', min_value=0, value=170)
    person_weight = st.number_input('Weight (kg)', min_value=0, value=60)

 
    bmi_labels = {
        0: 'Extremely Weak',
        1: 'Weak',
        2: 'Normal',
        3: 'Overweight',
        4: 'Obesity',
        5: 'Extreme Obesity'
    }
    if st.button('Predict'):
        gender_val = 0 if person_gender == 'Male' else 1
        prediction = bmi_model.predict([[
            gender_val, 
            float(person_height), 
            float(person_weight)
        ]])
        result_label = bmi_labels.get(int(prediction[0]), "Unknown")
        st.success(f'ผลการทำนายคือ: **{result_label}**')
