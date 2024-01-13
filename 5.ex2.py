import streamlit as st
import random

cols = st.columns(4)
atari = random.randint(0,3)

for i in range(4):
    with cols[i]:
        if st.button("button"+str(i)):
            if i == atari:
                st.balloons()
        
