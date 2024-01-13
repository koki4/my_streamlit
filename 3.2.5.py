import streamlit as st
option = st.selectbox("職業は?", ['学生','会社員','公務員','自営業','その他'])
st.write('あなたの職業は', option)