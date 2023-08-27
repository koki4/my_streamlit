import streamlit as st

matsu = st.button("松")
take = st.button("竹")
ume = st.button("梅")

if matsu:
    st.write("2500円")
elif take:
    st.write("2000円")
elif ume:
    st.write("1500円")
else:
    st.write("コースを選んでください")