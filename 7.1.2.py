import seaborn as sns

df = sns.load_dataset("iris")
print(df.head())
print(df.tail(3))
print(df.shape)