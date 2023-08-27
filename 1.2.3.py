import streamlit as st
b0 = st.button("グー")
b1 = st.button("チョキ")
b2 = st.button("パー")

if b0:
    st.write("あなたはグーを選びました")
elif b1:
    st.write("あなたはチョキを選びました")
elif b2:
    st.write("あなたはパーを選びました")
else:
    st.write("ボタンを押してください")