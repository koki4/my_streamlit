import streamlit as st
genre = st.radio("好きな食べ物は？", ['ラーメン', 'カレー', '寿司'], horizontal=True)
st.write(f"{genre}が好きなんですね!")