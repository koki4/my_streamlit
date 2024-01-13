import streamlit as st
import pandas as pd
import seaborn as sns
from random import gauss

col1, col2 = st.columns(2)
with col1:
    mu = st.slider("平均", min_value=0, max_value=100, value=50)
with col2:
    sigma = st.slider("標準偏差", min_value=1, max_value=30, value=10)
score = [gauss(mu, sigma) for _ in range(1000)]
df = pd.DataFrame({"x":score})
ax = sns.histplot(df)
ax.set_xlim(0,200)
st.pyplot(ax.figure)