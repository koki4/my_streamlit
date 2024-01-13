import streamlit as st
import cv2
from PIL import Image, ImageEnhance

image_file = st.sidebar.file_uploader("画像アップロード (jpg, jpeg, png)", type=['jpg', 'png', 'jpeg'])

if image_file:
    image = Image.open(image_file)
    if st.sidebar.button("プレビュー"):
        st.sidebar.image(image)
    
    modes = ["Original", "Contrast", "Brightness", "Sharpness"]
    option = st.sidebar.radio("モード", modes)

    if option == "Original":
        st.subheader("Original")
        st.image(image, use_column_width=True)
    elif option == "Contrast":
        v = st.slider("Contrast", 0.5, 5.0)
        enhancer = ImageEnhance.Contrast(image)
        img_output = enhancer.enhance(v)
        st.image(img_output, use_column_width=True)
    elif option == "Brightness":
        v = st.slider("Brightness", 0.5, 5.0)
        enhancer = ImageEnhance.Brightness(image)
        img_output = enhancer.enhance(v)
        st.image(img_output, width=600, use_column_width=True)
    elif option == "Sharpness":
        v = st.slider("Sharpness", 0.5, 5.0)
        enhancer = ImageEnhance.Sharpness(image)
        img_output = enhancer.enhance(v)
        st.image(img_output, width=600, use_column_width=True)