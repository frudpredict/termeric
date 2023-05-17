import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Main Page")
st.sidebar.success("Select a page above.")


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)