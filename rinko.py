import streamlit as st
import pandas as pd
from random import gauss
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

col1, col2, col3 = st.columns(3)
with col1:
    mu = st.slider("平均", min_value=30, max_value=70, value=50)
with col2:
    sigma = st.slider("標準偏差", min_value=1, max_value=20, value=10)
with col3:
    bins = st.slider("区間の数 bins", min_value=1, max_value=200, value=60)

n = 1000
x = np.linspace(0, 100, n)
y = norm.pdf(x, mu, sigma)
score = [gauss(mu, sigma) for _ in range(n)]
df = pd.DataFrame({"score": score})

fig, ax = plt.subplots()
a,b,c = ax.hist(df, bins=bins, density=True)
ax.plot(x, y)
ax.set_xlim(0, 100)
st.pyplot(ax.figure)
fig1, ax1 = plt.subplots()
a1,b1,c1 = ax.hist(df, bins=bins)

# MSE計算
total = 0
b_means = [(b[i]+b[i-1])/2 for i in range(1,len(b))]
kansokutis = sorted(score)
for i in range(bins):
    total += (a[i] - norm.pdf(b_means[i], mu, sigma))**2 *int(a1[i])
st.subheader(f"MSE*10000: {total/n*10000:.5f}")

########
#MSEシュミレーション(計算時間かかる, 動かすときは以下のコメントアウト外す)
# mse_list = []
# for bins in range(1,100):
#     total = 0
#     a,b,c = ax.hist(df, bins=bins)
#     mediums = [(b[i]+b[i-1])/2 for i in range(1,len(b)) for _ in range(0,int(a[i-1]))]
#     kansokutis = [a[i] for i in range(len(a)) for _ in range(int(a[i]))]
#     for i in range(n):
#         rironti = norm.pdf(mediums[i], mu, sigma)*1000
#         total += (kansokutis[i] - rironti)**2
#     mse_list.append(total/n)

# fig1, ax1 = plt.subplots()
# df = pd.DataFrame({"MSE":mse_list})
# ax1 = df.plot(ax=ax1)
# ax1.set_xlim(1, 100)
# #ax1.set_ylim(0,10000)
# ax1.set_ylabel("MSE (Log Scale)")
# ax1.set_yscale('log')
# st.pyplot(fig1)

# fig2, ax2 = plt.subplots()
# ax2 = df.plot(ax=ax2)
# ax2.set_xlim(1, 100)
# ax2.set_ylim(0,10000)
# ax2.set_xlabel("Number of bins")
# ax2.set_ylabel("MSE")
# st.pyplot(fig2)
