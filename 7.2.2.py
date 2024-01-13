import seaborn as sns
df = sns.load_dataset("iris")
print(df["species"].unique())