import streamlit as st

st.multiselect("好きなスポーツは?",
               ["ランニング", "水泳", "野球", "サッカー", "ゴルフ"],
               ["水泳", "ランニング"], key="sports")
st.write(st.session_state.sports)
