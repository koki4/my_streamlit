import streamlit as st
apple = st.checkbox('apple')
orange = st.checkbox('orange')
melon = st.checkbox('melon')

fruits = [] #更新があり読み込む度にfruitsは空になる
if apple:
    fruits.append("apple")
if orange:
    fruits.append("orange")
if melon:
    fruits.append("melon")

st.write(f"You selected {fruits}")