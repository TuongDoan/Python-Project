from ast import Del
import pandas as pd

x = pd.read_csv('tested.csv',index_col = 'PassengerId')
print(x.shape)
y = Del(x['PassengerId'])
print(y.head())
