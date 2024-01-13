import streamlit as st
st.button("hello", key="hello")
st.button("world", key="world")
st.write(st.session_state)