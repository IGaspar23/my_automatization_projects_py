import pandas as pd
import csv

df = pd.read_csv("FashionDataset.csv")

# For show information about the dataset
print(df.info())

shape = df.shape
print(shape)