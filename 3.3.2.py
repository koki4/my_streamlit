import streamlit as st

with st.chat_message("assistant"):
    st.write("Hello! How are you?")
with st.chat_message("user"):
    st.write("Fine Thank You. And you?")
with st.chat_message("assistant"):
    st.write("I'm good. Let's get started.")