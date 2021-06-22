import numpy as np
import pandas as pd
import random
import string

np.random.seed(56)

def a():
    return ''.join(random.choice(string.ascii_letters) for i in range(5))
print(a())

def d(a,b):
    return np.random.randint(0,100, size=(a,b))
def f():
    return np.random.randint(0,100)

df = pd.DataFrame(d(10,5), index=[a() for i in range (1,11)], columns=["국어","영어","수학","사회","과학"])
df['일본어']=[f() for i in range (10)]
df.loc[:,'중국어'] = pd.Series([f() for i in range(10)], index=df.index)
#df.loc[:,'총합'] = df.sum(axis=1)
#df.loc['총합'] = df.sum()
print(df)
sub_sum_list = df.sum().tolist()
print(sub_sum_list)
df.loc['총점'] = sub_sum_list
my_sum_list = df.sum(axis=1).tolist()
print(my_sum_list)
df['내총점'] = my_sum_list
print(df)
#df.drop('총점', inplace=True)
#df = df.drop(columns=['내총점'],axis=1)
#f.loc[:,'평균'] = df.sum(axis=1)/7
#df.loc['과목평균'] = df.sum()/10
#df = df.sort_index(ascending=False)


print(df)