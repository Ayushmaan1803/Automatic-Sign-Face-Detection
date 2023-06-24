import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components
from PIL import Image
import numpy as np
import tensorflow as tf
import h5py
from tensorflow.keras.models import load_model

st.set_page_config(layout="wide")



# css markdown
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             height : 100%;
             background-image: url("https://wallpaperaccess.com/full/3901966.jpg");
             width:100%;
             height:100%; 
             background-attachment: fixed;
             background-size: cover
             background-color: rgba(0, 0, 0, 0)

             height:100%;

        }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()


#css markdown
st.markdown("<h2 <b  style='text-align: center;  font-family: Times New Roman, Times, serif; '> AUTOMATIC SIGN AND PHOTO DETECTION </b></h2>", unsafe_allow_html=True)



def load_model():
    model = tf.keras.models.load_model('imageclassifier.h5')
    return model
model = load_model()

def predict(image):
    img = Image.open(image)

    # Check if image has an alpha channel (4 channels)
    if img.mode == 'RGBA':
        # Convert image to RGB (3 channels) by removing alpha channel
        img = img.convert('RGB')

    img = img.resize((256, 256))  # Resize image to match the input shape of the model
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    prediction = model.predict(img)
    return prediction



# Add custom CSS to display inputs side by side
st.markdown(
    """
    <style>
    .side-by-side {
        display: flex;
    }
    .side-by-side > div {
        flex: 50%;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
uploaded_file = st.file_uploader("**Upload your image**", key="image1" , type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image1 = Image.open(uploaded_file)
    st.image(image1, caption='Uploaded Face Image', width=300)
    Prediction_1 = predict(uploaded_file)


st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

uploaded_file_2 = st.file_uploader("****Upload your signature****", key="image2" ,type=["jpg", "jpeg", "png"])

if uploaded_file_2 is not None:
    image2 = Image.open(uploaded_file_2)
    st.image(image2, caption='Uploaded Signature Image', width=300)
    prediction2 = predict(uploaded_file_2)


if uploaded_file is not None and uploaded_file_2 is not None:

    #Check if the "Check Images" button is clicked
    if st.button("VERIFY"):
        Prediction_1 = predict(uploaded_file)
        prediction2 = predict(uploaded_file_2)

        if Prediction_1 >= 0.5 and prediction2 < 0.5:
            uploaded_file, uploaded_file_2 = uploaded_file_2, uploaded_file  # Swap the files
            st.write("WRONG DETAILS ENTERED\n")
            st.write("RESULTS AFTER SWAPPING\n")



            # Display the predictions
            if predict(uploaded_file) < 0.5:
                st.write("YOUR FIRST UPLOADED IMAGE SHOULD BE YOUR FACE")
                st.image(uploaded_file, width=300)

            else:
                st.write("YOUR FIRST UPLOADED IMAGE SHOULD BE YOUR SIGNATURE")
                st.image(uploaded_file, width=300)

            if predict(uploaded_file_2) < 0.5:
                st.write("\nYOUR SECOND UPLOADED IMAGE SHOULD BE YOUR FACE")
                st.image(uploaded_file_2, width=300)

            else:
                st.write("\nYOUR SECOND UPLOADED IMAGE SHOULD BE YOUR SIGNATURE")
                st.image(uploaded_file_2, width=300)


        elif Prediction_1 < 0.5 and prediction2 < 0.5:
            st.write("Both are face images , please upload correct documents!!!")

        elif Prediction_1 >= 0.5 and prediction2 >= 0.5:
            st.write("Both are signatures, please upload correct documents!!!")

        else:
            st.write("SUCCESS! CORRECT DETAILS ENTERED")




st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

st.write("If you have any issue , please write to us below")

with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your e-mail")
    message = st.text_area("Enter your comment")


    submit = st.form_submit_button("Submit this form")






