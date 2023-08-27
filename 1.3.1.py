import streamlit as st

st.title("This is title")
st.header("This is header")
st.subheader("This is subheader")
st.caption("This is caption")
st.text("This is text")
md = """
# markdown header1
## markdown header2
- item1
- item2
"""
st.markdown(md)

code = """
import random
r = random.randint(1,3)
print(r)
"""
st.code(code)