import streamlit as st

txt = st.text_area('Text to analyze', '男はつらいよ')
st.write(f'単語数={len(txt.split(" "))}単語')