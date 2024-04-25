import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    # Display uploaded image
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Convert to grayscale
    gray_image = img.convert("L")
    st.subheader("Grayscale Image")
    st.image(gray_image, caption="Grayscale Image", use_column_width=True)

