# -*- coding: utf-8 -*-
import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

s2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})

print("s1['a']:" , s1['a'])
print("s2['b']:" , s2['b'])

data1 = [
    [1,'Alice',24,'New York'],
    [2,'Bob',25,'Los Angeles'],
    [3,'Charlie',26,'Chicago'],
    [4,'David',27,'Houston']
]

data2 = {
    'id': [1,2,3,4],
    'name': ['Alice','Bob','Charlie','David'],
    'age': [24,25,26,27],
    'city': ['New York','Los Angeles','Chicago','Houston']
}

df1 = pd.DataFrame(data1, columns=['id','name','age','city'])
df2 = pd.DataFrame(data2)
print(df1)
print(df2)