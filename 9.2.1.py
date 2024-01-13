import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")
df = sns.load_dataset("penguins")

st.header("Penguins")
st.subheader("データフレーム")
st.write(df.head(5))

st.header("データフレームのplotメソッドを使った描画")

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.subheader("df.plot")
    st.pyplot(df.plot().figure)

with col2:
    st.subheader("df[列リスト].plot")
    params = st.multiselect("parameter", 
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])
    if len(params) > 0:
        st.pyplot(df[params].plot().figure)

st.header("Seaborn")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.subheader("pairplotによる相関図")
    fig = sns.pairplot(df, hue="species")
    st.pyplot(fig)

with col2:
    st.subheader("species毎の分布")
    st.write("isinメソッドを使ってislandの取りうる値をフィルタリングしています")
    islands = st.multiselect("island", df["island"].unique(),
    default=df["island"].unique())
    if islands:
        fig = sns.catplot(data=df[df["island"].isin(islands)],
            x='species', hue='island', y='body_mass_g')
        st.pyplot(fig)

with col3:
    st.subheader("性別毎の体重分布")
    st.write("subplotsを使って描画領域を分割します")
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.histplot(df[df["sex"]=="Male"]["body_mass_g"], ax=axes[0])
    sns.histplot(df[df["sex"]=="Female"]["body_mass_g"],
                 ax=axes[1], color="r", kde=True)
    axes[0].set(xlim=(2000,6500), ylim=(0,40), title="Male")
    axes[1].set_xlim(2000,6500)
    axes[1].set_ylim(0,40)
    axes[1].set_title("Female")
    print(dir(axes[1]))
    st.pyplot(fig)