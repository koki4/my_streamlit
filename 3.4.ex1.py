import streamlit as st
import random

omikuji = ["大吉", "中吉", "小吉", "凶"]
if st.button("おみくじ"):
    result = random.choice(omikuji)
    st.header(f"あなたのおみくじは{result}です")
    st.write(result)
    if result == "大吉":
        st.balloons()