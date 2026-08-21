import pandas as pd

df = pd.read_csv("Data-Versioning-DVC/data/winequality-red.csv", sep=";")

print(df.shape)

df = df.drop_duplicates()

df.to_csv("Data-Versioning-DVC/data/winequality-red.csv", sep=";", index=False)

print(df.shape)
