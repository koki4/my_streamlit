import streamlit as st
from datetime import date
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
time_rage = st.slider(
    "When do you start/finish?",
    value=(date(2020,1,1),date(2021,1,1)),
    format="YYYY/MM/DD"
)
st.write("Start time:", time_rage)