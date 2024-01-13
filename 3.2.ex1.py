import streamlit as st

st.text_input('account')
password = st.text_input('password', type='password')
if st.button('login'):
    if password=="streamlit":
        st.write('Login success')
    else:
        st.write('パスワードが違います')