import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input
import time

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

model = tf.keras.models.load_model("saved_model/frud.hdf5")
### load file
uploaded_file = st.file_uploader("Choose a image file")

map_dict = {0:'Turmeric',
            1:'Riceflour',
            2:'R95Turmeric',
            3:'R75Turmeric',
            4:'R85Turmeric',
            5:'R90Turmeric'
            }

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(224,224))
    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="RGB")

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]
    Genrate_pred = st.button("Fraud Percentage")
    col1, col2 = st.columns(2)
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        with col1:
            st.title("Predicted Fraud Percentage for the image is {}".format(map_dict [prediction]))
        with col2:
            if(map_dict [prediction] == 'Turmeric'):
                        st.title("Frud Results")
                        progress_text_one = "Termeric 100%"
                        my_bar_one = st.progress(0, text=progress_text_one)
                        my_bar_one.progress(100, text=progress_text_one)
                        progress_text_two = "Toxic 0%"
                        my_bar_two = st.progress(0, text=progress_text_two)
                        my_bar_two.progress(0, text=progress_text_two)
            if(map_dict [prediction] == 'Riceflour'):
                        st.title("Frud Results")
                        progress_text_one = "Termeric 0%"
                        my_bar_one = st.progress(0, text=progress_text_one)
                        my_bar_one.progress(0, text=progress_text_one)
                        progress_text_two = "Toxic 0%"
                        my_bar_two = st.progress(0, text=progress_text_two)
                        my_bar_two.progress(100, text=progress_text_two)
            if(map_dict [prediction] == 'R95Turmeric'):
                        st.title("Frud Results")
                        progress_text_one = "Termeric 5%"
                        my_bar_one = st.progress(0, text=progress_text_one)
                        my_bar_one.progress(5, text=progress_text_one)
                        progress_text_two = "Toxic 95%"
                        my_bar_two = st.progress(0, text=progress_text_two)
                        my_bar_two.progress(95, text=progress_text_two)
            if(map_dict [prediction] == 'R75Turmeric'):
                        st.title("Frud Results")
                        progress_text_one = "Termeric 25%"
                        my_bar_one = st.progress(0, text=progress_text_one)
                        my_bar_one.progress(25, text=progress_text_one)
                        progress_text_two = "Toxic 75%"
                        my_bar_two = st.progress(0, text=progress_text_two)
                        my_bar_two.progress(75, text=progress_text_two)
            if(map_dict [prediction] == 'R85Turmeric'):
                        st.title("Frud Results")
                        progress_text_one = "Termeric 15%"
                        my_bar_one = st.progress(0, text=progress_text_one)
                        my_bar_one.progress(15, text=progress_text_one)
                        progress_text_two = "Toxic 85%"
                        my_bar_two = st.progress(0, text=progress_text_two)
                        my_bar_two.progress(85, text=progress_text_two)
            if(map_dict [prediction] == 'R90Turmeric'):
                        st.title("Frud Results")
                        progress_text_one = "Termeric 10%"
                        my_bar_one = st.progress(0, text=progress_text_one)
                        my_bar_one.progress(10, text=progress_text_one)
                        progress_text_two = "Toxic 90%"
                        my_bar_two = st.progress(0, text=progress_text_two)
                        my_bar_two.progress(90, text=progress_text_two)
