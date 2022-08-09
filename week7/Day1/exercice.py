import numpy as np
import pandas as pd
from dateutil.parser import parse
# b=int(input("choose a start: "))
# c=int(input("choose a length:"))
# d=int(input("choose a stop: "))
# e=np.arange(b,c,d)
# print(e)

# a= np.arange(6,428,4)
# print(a)

# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# print(a[~np. isnan(a)])


# g= np.random.randint(1,100,(5,6))
# h=np.amax(g,axis=1)
# print(g)
# # print(h)

# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# print(series)
# y=series.value_counts()
# print(y)


# series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# result = series.map(lambda iterator: parse(iterator))
# print("Day of week: ", result.dt.weekday_name.tolist())