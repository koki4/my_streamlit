import requests
import streamlit as st
st.title("Jokes")
if st.button("Say something"):
    r = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = r.json()
    with st.chat_message("assistant"):
        st.write(data["setup"])
    with st.chat_message("user"):
        st.write(data["punchline"])