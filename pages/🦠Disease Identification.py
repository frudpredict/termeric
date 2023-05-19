import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input
from streamlit_cropper import st_cropper
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)

model = tf.keras.models.load_model("saved_model/diseases.hdf5")
### load file
uploaded_file = st.file_uploader("Choose a image file")

map_dict = { 0:'LeafBlotch',
             1:'Leaf Spot',
             2:'NOT'
            }
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

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(224,224))
    # Now do something with the image! For example, let's display it:

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]
    img = Image.open(uploaded_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                aspect_ratio=aspect_ratio)
    
    # Manipulate cropped image at will
    st.write("Preview")
    _ = cropped_img.thumbnail((150,150))
    st.image(cropped_img)
    # Convert the file to an opencv image.

    Genrate_pred = st.button("Disease")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        # if(map_dict [prediction] == 'turmericfingers'){
        #     Grade = 1
        # }
        st.text(map_dict [prediction])
        if(map_dict [prediction] == 'Leaf Spot'):
            st.title('LeafSpot- Colletotrichum capsica (Scientific Name)')
            st.markdown('The fungus is carried on the scales of rhizomes which are the source of primary infection during sowing. The secondary spread is by wind, water and other physical and biological agents. The same pathogen is also reported to cause leaf-spot and fruit rot of chili where it is transmitted through seed borne infections. If chili is grown in nearby fields or used in crop rotation with turmeric, the pathogen perpetuates easily, building up inoculum potential for epiphytotic outbreaks.')
            st.title('Recommndation')
            st.markdown('•Select seed material from disease free areas.Treat seed material with mancozeb @ 3g/liter of water or carbendazim @ 1 g/liter of water, for 30 minutes and shade dry before sowing.•	Spray mancozeb @ 2.5 g/liter of water or carbendazim @ 1g/litre; 2-3 sprays at fortnightly intervals.The infected and dried leaves should be collected and burnt in order to reduce the inoculum source in the field.Spraying Blitox or Blue copper at 3 g/l of water was found effective against leaf spot.•	Crop rotations should be followed whenever possible.')
        if(map_dict [prediction] == 'LeafBlotch'):
            st.title('Leaf Blotch -Taphrina maculans   (Scientific Name)')
            st.markdown('The fungus is mainly air borne and primary infection occurs on lower leaves with the inoculum surviving in dried leaves of host, left over in the field. The ascospores discharged from successively maturing asci infect fresh leaves without dormancy, thus causing secondary infection. Secondary infection is most dangerous than primary one causing profuse sprouting all over the leaves. The pathogen persists in summer by means of acrogenous cells on leaf debris, and desiccated ascospores and blastopores in soil and among fallen leaves.')
            st.title('Recommndation')
            st.markdown('Select seed material from disease free areas.•	Treat the seed material with Mancozeb @ 3g/liter of water or Carbendazim @ 1 g/liter of water for 30 minutes and shade dry before sowing.•	Spray mancozeb @ 2.5 g/liter of water or Carbendazim @ 1g/liter; 2-3 sprays at fortnightly intervals.•	The infected and dried leaves should be collected and burnt in order to reduce the inoculum source in the field.•	Spraying Copper oxy chloride at 3 g/l of water was found effective against leaf blotch.')
        if(map_dict [prediction] == 'NOT'):
            st.title('Not a Disease')

