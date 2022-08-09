import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import numpy as np

chipotable = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')

# print(chipotable.head(11))
# print(chipotable.count())
# print(len(chipotable.columns))
# print(chipotable.columns)
# Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame. Indexing could mean selecting all the rows and some of the columns, some of the rows and all of the columns, or some of each of the rows and columns. Indexing can also be known as Subset Selection.
# print(chipotable.sort_values('quantity', ascending=False).head(1).item_name)
# items = chipotable[['item_name', 'quantity']].groupby('item_name').sum()
# items.head()
# print(items.sort_values(['quantity'], ascending = False))
# print(chipotable['quantity'].agg(np.sum))
# print(chipotable['choice_description'].mode())
# chipotable['item_price'] = chipotable['item_price'].apply(lambda x: float(x[1:-1]))
# print(chipotable['choice_description'].mode())
# revenue = chipotable['quantity'].dot(chipotable['item_price'])
# print(revenue)
# print(chipotable['order_id'].count())
# np.mean(chipotable['quantity']) * np.mean(chipotable['item_price'])
df= pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')
# df['item_price'] = df['item_price'].apply(lambda x: float(x[1:-1]))
# print(df['item_price']>10)
# print(df[['item_price','item_name']])
# print(df.sort_values(by= ['item_name'], ascending=True))
# print(df.max()) 
# print(df.sort_values(by='item_price',ascending=False).head())
# print(df[df['item_price'] == df.item_price.max()])
