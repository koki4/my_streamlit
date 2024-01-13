import streamlit as st
import pandas as pd
from random import gauss
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
mu, sigma, bins = 50, 10, 60

n = 1000
x = np.linspace(0, 100, n)
y = norm.pdf(x, mu, sigma)*1000
score = [gauss(mu, sigma) for _ in range(n)]
df = pd.DataFrame({"score": score})

fig, ax = plt.subplots()
a,b,c = ax.hist(df, bins=bins)
ax.plot(x, y)
ax.set_xlim(0, 100)
ax.figure