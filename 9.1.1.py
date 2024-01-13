import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
selected = st.sidebar.radio("species", ['setosa', 'versicolor', 'virginica'])
st.header("IRIS")

col1, col2 = st.columns(2)
with col1:
    st.write("all species")
    st.pyplot(df.plot().figure)

with col2:
    st.write(selected)
    st.pyplot(df[df["species"]==selected].plot().figure)

st.divider()

st.header(f"Histgram of {selected}")

fig, ax = plt.subplots(2,2)
plt.subplots_adjust(hspace=0.5)

select_df = df[df["species"]==selected]
a = select_df["sepal_length"].hist(ax=ax[0,0])
select_df["sepal_width"].hist(ax=ax[0,1])
select_df["petal_width"].hist(ax=ax[1,0])
select_df["petal_width"].hist(ax=ax[1,1])
ax[0,0].set_title("sepal_length")
ax[0,1].set_title("sepal_width")
ax[1,0].set_title("petal_length")
ax[1,1].set_title("petal_width")

st.pyplot(fig)
