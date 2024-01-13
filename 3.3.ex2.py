import requests
import streamlit as st
st.title("Jokes")
if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Say something"):
    r = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = r.json()
    st.session_state.messages.append({"role": "assistant", "content": data["setup"]})
    st.session_state.messages.append({"role": "user", "content": data["punchline"]})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])