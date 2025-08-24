
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import json
import joblib
import os

# Load the config file (build the path relative )

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH, 'r') as readfile:
    config = json.load(readfile)
readfile.close()

# Load the model
model_file_path = os.path.join(BASE_DIR, "models", config['model_filename'])
model = joblib.load(model_file_path)

# Load the feature range
feature_range = config['feature_range']

# Streamlit app header and subheader

st.title("Welcome to Bank Customer Churn Prediction App")
st.markdown("""---""")
st.subheader("This app predcts the chances of churning of a customer based on following features")

# Take input from the user

st.markdown("""---""")

col1, col2, col3 = st.columns([4,1,4])

with col1:
    min_credit_score = feature_range['credit_score'].get("min", 0)
    max_credit_score = feature_range['credit_score'].get("max", 850)
    credit_score = st.slider("Credit score of the customer", 
                             min_value=min_credit_score, 
                             max_value=max_credit_score, step=1)

with col3:
    min_age = feature_range['age'].get("min", 18)
    max_age = feature_range['age'].get("max", 100)
    age = st.slider("Age of the customer", min_value=min_age, 
                    max_value=max_age, step=1)

col4, col5, col6 = st.columns([4, 1, 4])

with col4:
    min_balance = feature_range['balance'].get("min", 0)
    max_balance = feature_range['balance'].get("max", 250000)
    balance = st.number_input("Account balance of the customer", 
                              min_value=min_balance, 
                              max_value=max_balance, step=100)

with col6:
    min_salary = feature_range['estimated_salary'].get("min", 0)
    max_salary = feature_range['estimated_salary'].get("max", 200000)
    estimated_salary = st.number_input("Salary of the customer", 
                                       min_value=min_salary, 
                                       max_value=max_salary, step=100)

col7, col8, col9 = st.columns([4, 1, 4])

with col7:
    min_tenure = feature_range['tenure'].get("min", 0)
    max_tenure = feature_range['tenure'].get("max", 10)
    tenure = st.slider("How many years the customer is having account?", 
                       min_value=min_tenure, max_value=max_tenure, step=1)

with col9:
    products_number = st.slider("Number of banking products the customer used.", 
                                min_value=1, max_value=4, step=1)

col10, col11, col12 = st.columns([4, 1, 4])

with col10:
    country = st.selectbox("Country of the account location", 
                           feature_range['country'])

with col12:
    gender = st.selectbox("Gender of the customer", feature_range['gender'])

col13, col14, col15 = st.columns([4, 1, 4])

with col13:
    if (st.checkbox("Is the customer using a credit card? (check if yes)")):
        credit_card = 1
    else:
        credit_card = 0

with col15:
    if (st.checkbox("Is the customer an active member of the bank? (check if yes)")):
        active_member = 1
    else:
        active_member = 0

submit = st.button("Predict")

st.markdown("""---""")

# prediction from the model

if submit:
    # Prepare the data in the format required by the model
    values = np.array([credit_score, age, balance, estimated_salary, tenure, products_number, country, gender, credit_card, active_member]).reshape(1,-1)

    test_df = pd.DataFrame(values, columns=config['feature_list'])

    prediction = float(model.predict_proba(test_df)[0, 1])

    st.write("Based on the inputs provided above")

    if prediction < config['threshold']:
        st.success(f"The customer has low probability ({round(prediction*100, 2)}%) to churn.")
    elif prediction >= config['threshold'] and prediction < 2*config['threshold']:
        st.warning(f"The customer is moderately likely ({round(prediction*100, 2)}%) to churn.")
    else:
        st.error(f"The customer has high probability ({round(prediction*100, 2)}%) to churn.")

    st.markdown("""---""")