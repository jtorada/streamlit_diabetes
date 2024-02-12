import pickle
import streamlit as st

#Membaca atau load model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul WEB
st.title('Data Mining Prediksi Diabetes')

# Membagi 2 kolom
col1, col2 = st.columns(2)
with col1 :
    Pregnancies = st.text_input ('Input nilai Pregnancies')
with col1 :    
    Glucose = st.text_input ('Input nilai Glucose')
with col1 :
    BloodPressure = st.text_input ('Input nilai BloodPressure')
with col1 :
    SkinThickness = st.text_input ('Input nilai SkinThickness')
with col2 :
    Insulin = st.text_input ('Input nilai Insulin')
with col2 :
    BMI = st.text_input ('Input nilai BMI')
with col2 :
    DiabetesPedigreeFunction = st.text_input ('Input nilai DiabetesPedigreeFunction')
with col2 :
    Age = st.text_input ('Input nilai Age')

# code untuk prediksi
diabet_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes') :
    diabet_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diabet_prediction[0] == 0) :
        diabet_diagnosis = 'Pasien tidak terkena diabetes'
    else :
        diabet_diagnosis = 'Pasien terkena diabetes'
    st.success(diabet_diagnosis)
