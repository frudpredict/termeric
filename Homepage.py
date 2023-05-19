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
st.markdown('1.Disease Identification and Recommendations: With our advanced machine learning algorithms, YellowRoot can accurately identify and classify turmeric leaf diseases. By uploading images of diseased leaves, our system quickly analyzes the symptoms and provides tailored recommendations for disease management. This helps farmers take proactive measures to prevent crop loss and optimize turmeric health.')
