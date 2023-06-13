# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('vgsales_12.csv')
df

# %%
df.shape

# %%
df.head()

# %%
df.describe()

# %%
df.where(df['Rank'] == 7564).dropna()

# %%
df.info()

# %%
df.drop(axis=0, index=0)

# %%
df.replace(to_replace='Mini Ninjas', value="Big Ninjas")

# %%
from sklearn.impute import SimpleImputer

# %%
imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
data = [[99, np.nan, 2], [45, 12, np.nan], [np.nan, 10, 20]]
 
print("Оригинальный набор чисел : \n", data)
imputer = imputer.fit(data)
 
data = imputer.transform(data)
 
print("Измененный набор чисел : \n", data)

# %%
print('Количество уникальных платформ', len(df.Platform.unique()))
print("Наименования платформы", df.Platform.unique())


