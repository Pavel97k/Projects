# %% [markdown]
# // импорт библиотек для работы с файлом csv

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# // Запись в переменную файла и его чтение.

# %%
df = pd.read_csv('vgsales_12.csv')
df

# %% [markdown]
# // Кол-во строк и столбцов

# %%
df.shape

# %% [markdown]
# // Заголовки столбцов в файле csv

# %%
df.head()

# %% [markdown]
# // Описание столбцов

# %%
df.describe()

# %% [markdown]
# // Поиск занчения по Rank = 7564

# %%
df.where(df['Rank'] == 7564).dropna()

# %% [markdown]
# // Краткая сводка об столбцах в csv

# %%
df.info()

# %% [markdown]
# // Удаление строки по индексу

# %%
df.drop(axis=0, index=0)

# %% [markdown]
# // Замена значения to_replace на value

# %%
df.replace(to_replace='Mini Ninjas', value="Big Ninjas")

# %% [markdown]
# // Импорт класса SimpleImputer

# %%
from sklearn.impute import SimpleImputer

# %% [markdown]
# // Работа с классом SimpleImputer

# %%
imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
data = [[99, np.nan, 2], [45, 12, np.nan], [np.nan, 10, 20]]
 
print("Оригинальный набор чисел : \n", data)
imputer = imputer.fit(data)
 
data = imputer.transform(data)
 
print("Измененный набор чисел : \n", data)

# %% [markdown]
# // Отображения уникальный значений столбца Platform и его кол-ва 

# %%
print('Количество уникальных платформ', len(df.Platform.unique()))
print("Наименования платформы", df.Platform.unique())


