import streamlit as st
import seaborn as sns

data_names = ['iris', 'taxis', 'titanic']
tabs = st.tabs(data_names)
for tab,data_name in zip(tabs, data_names):
    with tab:
        st.write(data_name)
        df = sns.load_dataset(data_name)
        st.write(df)