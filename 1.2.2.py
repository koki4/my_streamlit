import streamlit as st

if st.button('circle'):
    st.write('まる')
elif st.button('rect'):
    st.write('四角')
else:
    st.write('その他')