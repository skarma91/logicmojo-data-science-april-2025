import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title(f"Basic Streamlit application")

# Header
st.header("This is a demo")

# subheader
st.subheader("Welcome to my app")

# Markdowns

st.markdown("----")

st.markdown("# This is markdown header-1")
st.markdown("## This is markdown header-2")
st.markdown("### This is markdown header-3")

st.markdown("---")

# Mathematical equation
st.markdown("$$ a^2 + b^2 = c^2 $$")

st.latex(r'''
         y = \frac{x}{z} + \theta
         ''')

# write method
st.write("This is just a text")

st.write(range(10))

data = np.random.randn(10,2)
df = pd.DataFrame(data, columns=['A', 'B'])

st.write(df)

st.markdown("---")

# Displaying image

from PIL import Image

img = Image.open("./lm10.jpeg")

col1, col2 = st.columns([6,4])

with col1:
    st.image(img, width=600)

with col2:
    st.text("Hi, I am Lionel Messi. I play for argentina. I also played for FC Barcelona.")