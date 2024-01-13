import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib
st.set_page_config("wide")

df = sns.load_dataset("healthexp")
st.subheader("データフレーム")
st.dataframe(df, height=150)

countries = df["Country"].unique()
values = st.multiselect("countries", countries, default=countries)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].set_title("年間消費額")
axes[1].set_title("平均寿命")

sns.lineplot(df[df["Country"].isin(values)],
                x="Year", y="Spending_USD",  hue="Country", ax=axes[0])
sns.lineplot(df[df["Country"].isin(values)],
                x="Year", y="Life_Expectancy", hue="Country", ax=axes[1])
st.pyplot(fig)