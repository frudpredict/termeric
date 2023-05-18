import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from streamlit_cropper import st_cropper
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload an image and set some options for demo purposes
st.header("Cropper Demo")
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
    "2:3": (2, 3),
    "Free": None
}
aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    img = Image.open(img_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                aspect_ratio=aspect_ratio)
    
    # Manipulate cropped image at will
    st.write("Preview")
    _ = cropped_img.thumbnail((150,150))
    st.image(cropped_img)

    model = tf.keras.models.load_model("saved_model/diseases.hdf5")

    container = st.container()

    st.subheader("Disease Identification")
    uploaded_file = cropped_img

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
            
