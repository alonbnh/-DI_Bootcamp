import pandas as pd
import numpy as np

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# print(df.iloc[50])
# print(df.iloc[50])
# print(df.iloc[50:60][['species', 'petal_length', 'petal_width']])
# print(df[['species', 'petal_length']].groupby('species').agg([np.mean, np.median, np.sum]))