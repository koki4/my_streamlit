import streamlit as st
import datetime

d = st.date_input("誕生日はいつですか？", datetime.date(2019,7,6))
st.write('あなたの誕生日:', d)