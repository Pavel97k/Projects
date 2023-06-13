# %% [markdown]
# # Практическая 5

# %% [markdown]
# Импорт библиотек

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# Чтение датасета

# %%
df = pd.read_csv("vgsales_12.csv")
df

# %% [markdown]
# Удаление колонки Unnamed

# %%
df = df.drop(columns='Rank')
df

# %% [markdown]
# Удаление колонки Date

# %%
df = df.drop(columns='Other_Sales')
df

# %% [markdown]
# Использование OrdinalEncoder

# %%
from sklearn.preprocessing import OrdinalEncoder

Oenc = OrdinalEncoder()
Oenc.fit(df[['Name','Platform','Year','Genre']])
df

# %% [markdown]
# Вывод категорий OrdinalEncoder

# %%
Oenc.categories_

# %% [markdown]
# Использование OrdinalEncoder

# %%
from sklearn.preprocessing import OrdinalEncoder

Oenc = OrdinalEncoder()
df[['Name','Platform','Year','Genre']] = Oenc.fit_transform(df[['Name','Platform','Year','Genre']])
df

# %% [markdown]
# Использование LabelEncoder

# %%
from sklearn.preprocessing import LabelEncoder

Lenc = LabelEncoder()
Lenc.fit(df['Global_Sales'])
df['Global_Sales'] = Lenc.fit_transform(df['Global_Sales'])
df

# %% [markdown]
# Вывод классов LabelEncoder

# %%
Lenc.classes_

# %% [markdown]
# Использование OneHotEncoder

# %%
from sklearn.preprocessing import OrdinalEncoder

Onhot = OrdinalEncoder()
Onhot.fit(df[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']])
df

# %% [markdown]
# Вывод категорий OneHotEncoder

# %%
Onhot.categories_

# %% [markdown]
# Перевод столбца у OneHotEncoder в массив

# %%
Onhot.transform(df[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']])

# %% [markdown]
# Вывод 

# %%
df[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']] = Onhot.fit_transform(df[['NA_Sales','EU_Sales','JP_Sales','Global_Sales']])
df

# %% [markdown]
# Удаление столбца RainToday

# %%
df = df.drop(columns='Global_Sales')
df

# %% [markdown]
# Использование Normalizer

# %%
from sklearn.preprocessing import Normalizer

Norm = Normalizer()
df[['NA_Sales','EU_Sales']] = Norm.fit_transform(df[['NA_Sales','EU_Sales']])
df

# %% [markdown]
# Использование train_test_split

# %%
from sklearn.model_selection import train_test_split

Y = df['Genre']
X = df.drop(columns=['Genre'])

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
x_train



# %%
y_test

# %%
x_test


