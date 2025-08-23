import streamlit as st
import numpy as np

st.title("Welcome to BMI calculator app")

st.write("Body Mass Index (BMI) is calculated using following formula:")

st.latex(r'''
         BMI = \frac{weight}{height^2}
         ''')

st.text("Where weight is in kg and height is in meters")

weight = st.number_input("Enter your weight (in kg)")

unit = st.radio("Select your height format: ", ['cms', 'meters', 'feet'])

height = st.number_input(f"Enter your height in {unit}")

# height conversion (converts the height to meter)

if unit == "cms":
    height = height/100  # 100 cms = 1 meter
elif unit == "feet":
    height = height/3.28 # 3.28 feet = 1 meter

# BMI calculation

if (st.button("Calculate BMI")):
    BMI = np.round(weight/(height**2), 3)
    st.write(f"Your BMI is {BMI}")

    if (BMI < 16):
        st.error("You are extremely underweight")
    elif (BMI >= 16 and BMI < 18.5):
        st.warning("You are Underweight")
    elif (BMI > 18.5 and BMI < 25):
        st.success("You are Healthy")
    elif (BMI >= 25 and BMI < 30):
        st.warning("You are overweight")
    elif (BMI >= 30):
        st.error("You are extremely overweight")