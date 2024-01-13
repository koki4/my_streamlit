import streamlit as st
import pandas as pd
df = pd.DataFrame({
    "LAT": [35.60472,35.44778, 0],
    "LON": [139.69167,139.6425, 0],
    "SZ": [2000, 1000, 3000],
})
st.map(df, latitude='LAT', longitude='LON', size='SZ')