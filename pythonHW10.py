import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data.loc[:, 'human'] = 0
data.loc[:, 'robot'] = 0
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
print(data)



