import seaborn as sns
import streamlit as st
df = sns.load_dataset("penguins")
print(df)

st.title("Penguins")
st.write(df)

code = """
import seaborn as sns
import streamlit as st
df = sns.load_dataset("penguins")
print(df)

st.title("Penguins")
st.write(df)
"""
st.code(code)