import streamlit as st
import numpy as np
import pandas as pd

st.header("Examples of streamlit inputs.")

st.markdown("---")

# text inputs

name = st.text_input("Enter your name")
surname = st.text_input("Enter your surname")

# button
status = st.button("Submit")

if status:
    st.subheader(f"Welcome {name} {surname}")


st.markdown("----")

st.write("Now enter some details about you")

# radio button (single option choices) (returns a string)

gender = st.radio("Select Gender: ", ('Male', 'Female', 'Prefer not to disclose'))

# Selection box (single option drop down) (returns a string)

education_level = st.selectbox("Highest Educational Qualification",
                               ['Higher Secondary', 'Bachelors', 'Masters', 'PhD', 'Others'])

if education_level == "Others":
    education_level = st.text_input("Please enter your educational qualification")

# Multi-selection box (returns a list)

hobbies = st.multiselect("Hobbies", 
                         ['Dancing', 'Photography', 'Painting', 'Sketching', 'Singing'])


# slider
age = st.slider("Select your age in years", min_value=18.0, max_value=60.0, step=0.5)

# bootstrap like status output

# st.success("Success message")
# st.info("Information message")
# st.warning("This is a warning")
# st.error("This is an error")

st.info(f"Your age is {age} years")

# checkbox (return a boolean)

smoker = st.checkbox("Do you smoke? check if yes")

if smoker:
    st.warning(f"You're a smoker.")
