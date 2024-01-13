import streamlit as st
import matplotlib.pyplot as plt

from wordcloud import WordCloud

text = st.text_area("なんでも記入してください", 
"""A faster way to build and share data apps.
Streamlit lets you turn data scripts into shareable web apps in minutes, not
weeks.
It’s all Python, open-source, and free!
And once you’ve created an app you can use our Community Cloud platform to
deploy,
manage, and share your app.""", height=150)

wcloud = WordCloud().generate(text)
fig = plt.figure(figsize=(20,10))
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(fig)