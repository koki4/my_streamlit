import seaborn as sns
df = sns.load_dataset("iris")
print(df[["species", "sepal_length"]].head())