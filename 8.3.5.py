import streamlit as st
import seaborn as sns
df = sns.load_dataset("tips")
ax = df.plot.scatter(x="total_bill", y="tip", c="size", colormap="cool")
st.pyplot(ax.figure)