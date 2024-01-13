import streamlit as st
import requests
st.session_state.zip=3510101
with st.sidebar:
    st.text_input("郵便番号", key=zip)
    if st.button("検索"):
        r = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={st.session_state.zip}")
        data=r.json()
        st.write(data["results"][0])


