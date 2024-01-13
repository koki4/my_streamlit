import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
df = sns.load_dataset("iris")
col1, col2 = st.columns(2)
with col1:
    st.subheader("jointplot")
    st.write("2つのパラメタの相関を詳しくみるときに使用します")
    ax = sns.jointplot(data=df, x="sepal_width", y="sepal_length")
    st.pyplot(ax)
with col2:
    st.subheader("pairplot")
    st.write("複数のパラメタの相関をみるときに使用します")
    ax = sns.pairplot(data=df)
    st.pyplot(ax)