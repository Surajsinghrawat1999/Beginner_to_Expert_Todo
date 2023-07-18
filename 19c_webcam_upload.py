import streamlit as st
from PIL import Image
st.subheader("Color to grayscale Converter: ")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create a pillow image instance
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")

    #Render the grayscale image on the webpage
    st.image(gray_img)
if uploaded_image:
    img = Image.open(uploaded_image)

    # Convert the pillow image to grayscale
    gray_uploaded_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_uploaded_img)