import pandas as pd
import streamlit as st
df1 = pd.read_excel("latlng_data.xls", 
        header=None, skiprows=5, usecols=[1,5,6],
        names=["name", "lat", "lon"], nrows=47)
print(df1.head())

df2 = pd.read_csv("FEH_00200524_231007143130.csv", header=None,
            skiprows=14, usecols=[3, 5], nrows=47,
            names=["name", "population"], thousands=",",
            dtype={"population": int}, encoding="Shift-JIS")
print(df2.head())

df = df1.join(df2.set_index('name'), on="name")
df["population"] = df["population"].map(lambda x : x*2)

st.map(df, latitude='lat', longitude='lon', size="population")