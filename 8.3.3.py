import streamlit as st
import pandas as pd
x = [100,50,60,70,80]
y = [80,60,90,100,80]
df = pd.DataFrame({"x":x, "y":y})
col1, col2 = st.columns(2)
with col1:
    st.pyplot(df.plot.bar().figure)
with col2:
    st.pyplot(df.plot.bar(stacked=True).figure)