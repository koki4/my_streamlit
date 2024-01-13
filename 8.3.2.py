import streamlit as st
import pandas as pd
y = [i*i for i in range(-5, 6)]
x = [i for i in range(-5,6)]
df = pd.DataFrame({"v":y})
ax = df.plot()
st.pyplot(ax.figure)