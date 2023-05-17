import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

model = tf.keras.models.load_model("saved_model/diseases.hdf5")

col1, col2 = st.columns([1, 1])


col1.subheader("Disease Identification")
uploaded_file = col1.file_uploader("Choose a image file")

### load file


map_dict = {
            0:'Leaf Blotch',
            1:'Leaf Spot'
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

    Genrate_pred = st.button("Disease")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Disease for the image is {}".format(map_dict [prediction]))
        if(map_dict [prediction] == 'Leaf Blotch'):
            st.title('Leaf Blotch')
            st.text('The fungus is mainly air borne and primary infection occurs on lower leaves with the inoculum surviving in dried leaves of host, left over in the field. The ascospores discharged from successively maturing asci infect fresh leaves without dormancy, thus causing secondary infection. Secondary infection is most dangerous than primary one causing profuse sprouting all over the leaves. The pathogen persists in summer by means of acrogenous cells on leaf debris, and desiccated ascospores and blastopores in soil and among fallen leaves.')
            st.title('Recommndation')
            st.text('Spray mancozeb @ 2.5 g/liter of water or Carbendazim @ 1g/liter; 2-3 sprays at fortnightly intervals.')
        if(map_dict [prediction] == 'Leaf Spot'):
            st.title('Leaf Spot')
            st.text('The fungus is carried on the scales of rhizomes which are the source of primary infection during sowing. The secondary spread is by wind, water and other physical and biological agents. The same pathogen is also reported to cause leaf-spot and fruit rot of chili where it is transmitted through seed borne infections. If chili is grown in nearby fields or used in crop rotation with turmeric, the pathogen perpetuates easily, building up inoculum potential for epiphytotic outbreaks.')
            st.title('Recommndation')
            st.markdown('Spray mancozeb @ 2.5 g/liter of water or carbendazim @ 1g/litre; 2-3 sprays at fortnightly intervals.The infected and dried leaves should be collected and burnt in order to reduce the inoculum source in the field.')
            
