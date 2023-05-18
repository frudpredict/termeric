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
image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')


