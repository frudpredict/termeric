import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

model = tf.keras.models.load_model("saved_model/gradee.hdf5")
### load file
uploaded_file = st.file_uploader("Choose a image file")

map_dict = { 0:'turmericfingers',
             1:'turmericbulbs',
             2:'sproutedturmeric',
             3:'insectdamages',
             4:'healthyrawturmeric',
             5:'Not'
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

    Genrate_pred = st.button("Grade")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        # if(map_dict [prediction] == 'turmericfingers'){
        #     Grade = 1
        # }
        st.text(map_dict [prediction])
        if(map_dict [prediction] == 'turmericfingers'):
            st.title('grade A')
            st.markdown('The uploaded image contains a high percentage of processed turmeric fingers. Processed turmeric fingers refer to turmeric roots that have been harvested, cleaned, and undergone various processing methods to transform them into a more usable form. Processed turmeric fingers, in the form of dried and ground powder, are known for their vibrant yellow color and distinctive earthy flavor. They contain a bioactive compound called curcumin, which is responsible for many of its health benefits and medicinal properties, including anti-inflammatory, antioxidant, and antimicrobial effects. ')
            progress_text_one = "100%"
            my_bar_one = st.progress(0, text=progress_text_one)
            my_bar_one.progress(100, text=progress_text_one)
        if(map_dict [prediction] == 'turmericbulbs'):
            st.title('grade B')
            progress_text_one = "100%"
            my_bar_one = st.progress(0, text=progress_text_one)
            my_bar_one.progress(100, text=progress_text_one)
            st.markdown('The uploaded image contains a high percentage of processed turmeric bulbs. When harvesting turmeric, certain rhizomes are chosen to serve as seed rhizomes for future plantings. These selected rhizomes are typically larger and healthier than the others. ')
        if(map_dict [prediction] == 'sproutedturmeric'):
            st.title('grade E')
            progress_text_one = "100%"
            my_bar_one = st.progress(0, text=progress_text_one)
            my_bar_one.progress(100, text=progress_text_one)
            st.markdown('The uploaded image contains a high percentage of sprouted turmeric rhizomes. During the sprouting process, the rhizomes tend to absorb more moisture from the environment. This increased moisture content can make sprouted turmeric more prone to spoilage and microbial growth if not stored properly. As the rhizomes sprout and start developing shoots, there may be a decrease in the concentration of certain nutrients. The energy stored in the rhizomes is utilized for the growth of new shoots, which can result in a slight reduction in the overall nutrient content.')
        if(map_dict [prediction] == 'insectdamages'):
            st.title('grade D')
            progress_text_one = "100%"
            my_bar_one = st.progress(0, text=progress_text_one)
            my_bar_one.progress(100, text=progress_text_one)
            st.markdown('The uploaded image contains a high percentage of insect damaged turmeric rhizomes. Insect damage to turmeric rhizomes can occur during the growing process or while they are stored. Insects such as termites, beetles, or grubs may infest the rhizomes and cause varying degrees of damage. If only a few rhizomes are affected by insect damage, they can be discarded to prevent further infestation or spread to other rhizomes. However, if a significant portion of the crop is damaged, it may be necessary to take appropriate measures such as fumigation or using natural insecticides to control the infestation. It is essential to follow recommended guidelines and regulations for pesticide use and disposal.')
        if(map_dict [prediction] == 'healthyrawturmeric'):
            st.title('grade C')
            progress_text_one = "100%"
            my_bar_one = st.progress(0, text=progress_text_one)
            my_bar_one.progress(100, text=progress_text_one)
            st.markdown('The uploaded image contains a high percentage of healthy raw turmeric rhizomes.Raw turmeric refers to the fresh, unprocessed form of turmeric root, also known as rhizome. It is the same plant as dried turmeric, but in its raw state, it has a distinct appearance and texture. Raw turmeric should be firm and free from mold or soft spots. To store it, keep the unpeeled root in a cool, dry place or refrigerate it. It can stay fresh for several weeks when stored properly. Special Note: Turmeric can stain hands and surfaces, so wearing gloves while handling it is recommended. Its also advised to be cautious with clothing and utensils, as the vibrant color can be difficult to remove. While raw turmeric is generally safe for consumption, some individuals may be sensitive to its active compounds. Its advisable to consult with a healthcare professional if you have specific health conditions, are on medication, or if you plan to consume large amounts regularly.')
        if(map_dict [prediction] == 'Not'):
            st.title('This is Not a Termeric')
