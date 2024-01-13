import streamlit as st
count = st.session_state.count if "count" in st.session_state else 0
if st.button('count'):
    count += 1

st.write(f"count={count}")
st.session_state.count = count