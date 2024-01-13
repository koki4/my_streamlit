import streamlit as st
import numpy as np

col1, col2, col3 = st.columns([3,2,1])
data = np.random.randn(6, 1)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

col1.subheader("A wide column with a chart")
col1.line_chart(data)


with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
col2.write(data)

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")