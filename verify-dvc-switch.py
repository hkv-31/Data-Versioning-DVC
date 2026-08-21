import pandas as pd

df = pd.read_csv("Data-Versioning-DVC/data/winequality-red.csv", sep=";")

print(df.shape)