import streamlit as st
from PIL import Image


# Start the camera
camera_image = st.camera_input("Camera")

# Create a pillow instance
img = Image.open(camera_image)

# Convert the pillow img to grayscale
gray_img = img.convert("L")

# Render the grayscale image to the webpage
st.image(gray_img)

