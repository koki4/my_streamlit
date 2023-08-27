import streamlit as st
import random
clicked = st.button("おみくじ")
omikuji = ["小吉", "中吉", "大吉"]
if clicked:
    st.write(random.choice(omikuji))