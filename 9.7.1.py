import streamlit as st
import numpy as np
import cv2
from PIL import Image

cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
img_file = st.sidebar.file_uploader("画像アップロード(jpg, jpeg, png)",
                                        type=['jpg', 'png', 'jpeg'])
if img_file:
    if st.sidebar.button("プレビュー"):
        image = Image.open(img_file)
        st.sidebar.image(image)
    if st.sidebar.button("検出"):
        #変換
        image_bytes = img_file.getvalue()
        np_array = np.frombuffer(image_bytes, dtype=np.uint8)
        img = cv2.imdecode(np_array, flags=cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #結果
        facerect = cascade.detectMultiScale(rgb_image)
        #描画
        for rect in facerect:
            cv2.rectangle(rgb_image,
                        tuple(rect[0:2]),
                        tuple(rect[0:2] + rect[2:4]),
                        (255,0,0), thickness=2)
        st.image(rgb_image, use_column_width=True)
