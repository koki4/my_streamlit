import streamlit as st
options = st.multiselect(
    'What are you favorite fruits?',
    ['Apple', 'Orange', 'Melon', 'Peach'],
    ['Apple', 'Melon'],
)
st.write('You selected', options)