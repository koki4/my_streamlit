import streamlit as st
import random

cols = st.columns(5)
if 'atari' not in st.session_state:
    st.session_state.atari = random.randint(0,4)
if 'pushed' not in st.session_state:
    st.session_state.pushed = [0 for _ in range(5)]
for i in range(0,5):
    with cols[i]:
        if st.button("button"+str(i)):
            st.session_state.pushed[i] = 1
        if st.session_state.pushed[i] and st.session_state.atari != i:
            st.write("はずれ")