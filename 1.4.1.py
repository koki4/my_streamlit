import streamlit as st

html = """
<style>
ul {color:red}
</style>
<h1 style="color:blue;">Hello World</h1>
<h3 style="color:green;">Streamlit</h3>
<ul>
<li>Item 1 </li>
<li>Item 2 </li>
<li>Item 3 </li>
</ul>
"""
st.markdown(html, unsafe_allow_html=True)