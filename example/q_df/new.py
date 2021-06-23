#1
import pandas as pd
import numpy as np
import string
import random
np.random.seed(56)
#2
#print(pd.__version__)
#print('-'*100)
#3
#print(pd.show_versions())
#print('-'*100)
#4
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(data,labels)
#5
print(df)
print('-'*100+'6번')
#6
print(df.head(3))
print('-'*100+'7번')
#7
print(df[['animal','age']])
print('-'*100+'8번')
#8
#print(df.loc[['c','d','h']])
#print(df.iloc[[3,4,8]])
#print(df.index)
#print(df.columns)
#print(df.values)
hello = df[['animal','age']]
print(hello.iloc[[2,3,7]])
print('-'*100)
print(df[['animal','age']].iloc[[2,3,7]])
print('-'*100+'9번')

#9
visit1 = df['visits']  < 3
visit2= df[visit1]
print(visit2)
print('-'*100+'10번')

#10
print(df[df['age'].isnull()])
print('-'*100+'11번')

#11





'''
pd.DataFrame(np.random.randint(0, 100, size=(2,3)))
''.join(random.choice(string.ascii_letters) for i in range(5))
def a():
    return ''.join(random.choice(string.ascii_letters) for i in range(5))
print(a())
[i for i in range (1,10)]
pd.DataFrame(np.random.randint(0,100, size=(10,5)), index=[a() for i in range (1,11)], columns=["국어","영어","수학","사회","과학"])
'''