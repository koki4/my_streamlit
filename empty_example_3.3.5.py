import streamlit as st
import time

with st.empty():
    for seconds in range(60):
        with st.container():
            st.button(str(seconds))
            st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")