
import pandas as pd
import numpy as np
import string
import random
np.random.seed(56)

pd.DataFrame({"a":[1,2],"b":[3,4],"c":[5,6]}, index=[1,2])
pd.DataFrame([[1,2,3],[4,5,6]], index=[1,2], columns=["A","B","C"])
pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], index=[1,2,3,4], columns=["A","B","C","D"])
pd.Series({"A":"서울","B":"부산","C":"인천"})
pd.DataFrame(np.random.randint(0, 100, size=(2,3)))
''.join(random.choice(string.ascii_letters) for i in range(5))
def a():
    return ''.join(random.choice(string.ascii_letters) for i in range(5))
print(a())
[i for i in range (1,10)]
pf = pd.DataFrame(np.random.randint(0,100, size=(10,5)), index=[a() for i in range (1,11)], columns=["국어","영어","수학","사회","과학"])
print(pf)