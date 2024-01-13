import streamlit as st

with st.sidebar:
    image = st.radio("image", ['page1', 'page2', 'page3'])
st.write(image)
if image == "page1":
    st.write("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
elif image == "page2":
    st.write("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
else:
    st.write("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
