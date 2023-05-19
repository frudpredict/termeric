import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

model = tf.keras.models.load_model("saved_model/dryness.hdf5")
### load file
uploaded_file = st.file_uploader("Choose a image file")

map_dict = {0:'Half Dry1',
            1:'Toodryturmeric',
            2:'Not',
            3:'Half Dry2',
            4:'Driedturmeric'
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

    Genrate_pred = st.button("Dryness Level")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Dryness Level for the image is {}".format(map_dict [prediction]))
        if(map_dict [prediction] == 'Toodryturmeric'):
            st.markdown('The turmeric in the uploaded image is too dry and cannot be used for making powders. ')
        if(map_dict [prediction] == 'Half Dry'):
            st.markdown('The turmeric in the uploaded image has not dried enough to make a powder. You have to dry the turmeric for another 2 or 3 days to make the powders.')
        if(map_dict [prediction] == 'Driedturmeric'):
            st.markdown('The turmeric in the uploaded image has dried enough to make powders')
        if(map_dict [prediction] == 'Half Dry2'):
            st.markdown('The turmeric in the uploaded image has not dried enough to make a powder. You have to dry the turmeric for another 1 or 2 days to make the powders. ')
        if(map_dict [prediction] == 'NOT'):
            st.markdown('Not a Turmeric')
           
