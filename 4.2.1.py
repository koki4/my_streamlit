import streamlit as st

st.radio("好きな食べ物は?", ('ラーメン', 'うどん', '寿司'), key='food')
st.write(f"{st.session_state.food}が好きなんですね")