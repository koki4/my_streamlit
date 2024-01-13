import streamlit as st
prompt = st.chat_input("ここに入力してください")
if prompt:
    st.write(f"入力内容: {prompt}")