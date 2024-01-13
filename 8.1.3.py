import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({"x":[1,2,3,4,5], "y":[5,4,3,8,7]})
sns.lineplot(df)
plt.show()
