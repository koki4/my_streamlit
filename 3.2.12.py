import datetime
import streamlit as st
t = st.time_input("Set an alarm for", datetime.time(8,50))
st.write('Alarm is set for', t)