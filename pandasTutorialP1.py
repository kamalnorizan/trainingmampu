import pandas as pd

df = pd.read_csv('data.csv', sep='\t')

print(df.head(10))