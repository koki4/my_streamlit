import streamlit as st
html = """
<h1>今日の料理</h1>
<h3>カレーライス</h3>
<img src="data/curry.jpg">
<h3>材料</h3>
<ul>
    <li>肉: 300g</li>
    <li>ジャガイモ:中2個</li>
    <li>人参:小1本</li>
</ul>
<h3>作り方</h3>
<ol>
    <li>材料を切ります</li>
    <li>肉を炒めます</li>
    <li>煮込んでルーを入れます</li>
</ol>
"""
st.markdown(html, unsafe_allow_html=True)