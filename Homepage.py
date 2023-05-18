import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image




st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Yellow Root")
st.sidebar.success("Select a page above.")
image = Image.open('top.jpg')

st.image(image, caption='@Yellow Root')
st.markdown('Welcome to YellowRoot, a smart and intelligent system designed to maximize turmeric cultivation in Sri Lanka. Our web app offers four essential components powered by machine learning to revolutionize the turmeric industry. Whether youre a farmer, researcher, or enthusiast, YellowRoot is here to provide you with valuable insights and recommendations for enhancing turmeric growth. ')
