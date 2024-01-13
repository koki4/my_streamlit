import streamlit as st
import datetime
st.header('アンケート')
name = st.text_input('氏名')
mail = st.text_input('メール')
birthday = st.date_input('誕生日', datetime.date(2000,1,1))
sex = st.radio('性別', ['男', '女', 'その他'])
work = st.selectbox('職業', ['学生', '会社員', '自営業'])
hobby = st.multiselect('趣味', ['スポーツ', 'グルメ', '映画', '陶芸', '美術鑑賞', '散歩'], ['スポーツ', 'グルメ', '映画'])

text = {
    "name": name,
    "mail": mail,
    "birthday": birthday,
    "gender": sex,
    "occupation": work,
    "hobby": hobby,
}

st.write(text)