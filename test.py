import pandas as pd

df = pd.read_csv("datasets\ed2derecha.csv")

df = df.groupby(["day"]).size()

print("n")