import streamlit as st
import joblib
import numpy as np
import pandas as pd
import json
import os

# Load the config file (build the path relative )

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)
    
features = [x.strip() for x in config['features'].split(',')]

# Load the model

model_file_path = "./models/" + config['model_file_path'].split('/')[-1]
model = joblib.load(model_file_path)

# Putting header and subheader

st.title("Welcome to Graduate Admission Prediction App")
st.markdown("""---""")
st.subheader("This app predcts the chances of Graduate Admission based on following features")
st.markdown("""
    - GRE Score 
    - TOEFL Score
    - University Rating (Between 1 to 5, lower the better)
    - Statement of Purpose (SOP) strength (Between 1 to 5, higher the better)
    - Letter of Recommendation (LOR) strength (Between 1 to 5, higher the better)
    - Cumulative Grade Point Average [CGPA] (out of 10)
    - Research Experience (0 = No, 1 = Yes)
""")
st.markdown("""---""")

st.subheader("Please provide the following information to predict your chances of admission")

# Getting the input data from the user

col1, col2, col3 = st.columns([8,2,8])

with col1:
    gre_score = st.slider("Provide your GRE Score", min_value=260, max_value=340, step=1)

with col3:
    toefl_score = st.slider("Provide your TOEFL Score",min_value=60, max_value=120, step=1)


col4, col5, col6, col7, col8 = st.columns([8,2,8,2,8])

with col4:
    university_rating = st.selectbox("University rating", [1, 2, 3, 4, 5])

with col6:
    sop = st.slider("Strength of Statement of Purpose (SOP)", min_value=0.0, max_value=5.0, step=0.5)

with col8:
    lor = st.slider("Strength of Letter of Recommendation (LOR)", min_value=0.0, max_value=5.0, step=0.5)
    

col9, col10, col11 = st.columns([8,2,8])

with col9:
    cgpa = st.slider("Provide your CGPA", min_value=5.0, max_value=10.0, step=0.01)

with col11:
    research = st.radio("Do you have research experience?", ('Yes', 'No'))
    if research == 'Yes':
        research = 1
    else:
        research = 0

submit = st.button("Predict")

st.markdown("""---""")

if submit:
    # Prepare the data in the format required by the model
    input_data = pd.DataFrame(np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]]),
                                columns=features, index=['input'])
    
    st.write("The input data you provided is as below:")
    st.write(input_data)
    
    # Make prediction
    prediction = model.predict(input_data)[0]*100
    prediction = np.round(prediction, 2)

    # post processing the prediction
    if prediction < 0.0:
        prediction = 0.0
    elif prediction > 100.0:
        prediction = 100.0
    
    if prediction >= 75:
        st.success(f"Probability of getting admission is {prediction}%")
    elif prediction < 75 and prediction >= 50:
        st.warning(f"Probability of getting admission is {prediction}%")
    elif prediction < 50:
        st.error(f"Probability of getting admission is {prediction}%")

    st.markdown("""---""")