# %%
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
model = DecisionTreeClassifier()
from sklearn import tree


# %% [markdown]
# загружаем датасет

# %%
df = pd.read_csv("vgsales_12.csv")
df

# %% [markdown]
# удаляем столбцы с нерелевантными данными

# %%
df.drop(['Platform', 'Name', 'Genre', 'Publisher'], axis=1, inplace=True)

# %% [markdown]
# удаляем строки с пропущенными значениями

# %%
df.dropna(inplace=True)

# %% [markdown]
# переводим категориальные признаки в числовые

# %%
df['Rank'] = pd.factorize(df['Rank'])[0]
df['NA_Sales'] = pd.factorize(df['NA_Sales'])[0]
df['EU_Sales'] = pd.factorize(df['EU_Sales'])[0]
df['JP_Sales'] = pd.factorize(df['JP_Sales'])[0]
df['Global_Sales'] = pd.factorize(df['Global_Sales'])[0]

# %% [markdown]
# разбиваем датасет на признаки и целевую переменную

# %%
X = df.drop('Global_Sales', axis=1)
y = df['Global_Sales']

# %% [markdown]
# разбиваем данные на обучающую и тестовую выборки в соотношении 70% / 30%

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# %% [markdown]
# создаем и обучаем модель

# %%
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# %% [markdown]
# делаем предсказания на тестовой выборке

# %%
y_pred = model.predict(X_test)

# %% [markdown]
# вычисляем точность предсказаний

# %%
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# %% [markdown]
# вычисляем чувствительность предсказаний

# %%
recall = recall_score(y_test, y_pred, average='weighted')
print(recall)

# %% [markdown]
# вычисляем аккуратность предсказаний

# %%
precision = precision_score(y_test, y_pred, average='weighted')
print(precision)

# %% [markdown]
# вычисляем финальные предсказания

# %%
f1score = f1_score(y_test, y_pred, average='weighted')
print(f1score)

# %% [markdown]
# Рисуем дерево

# %%
tree.plot_tree(model, filled=True, fontsize=2)

# %% [markdown]
# Обучение дерева с гиперпараметрами

# %%
model_plot = DecisionTreeClassifier(max_depth=5, min_samples_leaf=4, max_leaf_nodes=200)
model_plot = model_plot.fit(X_train.iloc[::500], y_train.iloc[::500])

# %% [markdown]
# Рисуем дерево

# %%
tree.plot_tree(model_plot, filled=True, fontsize=12)

# %% [markdown]
# делаем предсказания

# %%
y_pred = model_plot.predict(X_test)

# %% [markdown]
# вычисляем точность предсказаний

# %%
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# %% [markdown]
# вычисляем чувствительность предсказаний

# %%
recall = recall_score(y_test, y_pred, average='weighted')
print(recall)

# %% [markdown]
# вычисляем аккуратность предсказаний

# %%
precision = precision_score(y_test, y_pred, average='weighted')
print(precision)

# %% [markdown]
# вычисляем финальный предсказания

# %%
f1score = f1_score(y_test, y_pred, average='weighted')
print(f1score)


