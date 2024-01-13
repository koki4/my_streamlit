import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

y = [x*x for x in range(-5, 6, 1)]
x =  [x for x in range(-5,6,1)]

# df.plot(pd.DataFrame({})) & plt.show()
df = pd.DataFrame({"v":vals})
df.plot()
plt.show()

# plt.plot(x,y) & plt.show()
plt.plot(x,y)
plt.show()

# sns
df = pd.DataFrame({"x":x, "y":y})
sns.lineplot(df)
plt.show()