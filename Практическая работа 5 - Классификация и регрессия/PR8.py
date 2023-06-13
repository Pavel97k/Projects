# %% [markdown]
# # Практическая работа 8

# %% [markdown]
# Импорт библиотек

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, PolynomialFeatures
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, RandomForestRegressor

# %% [markdown]
# Чтение датасета

# %%
df = pd.read_csv("vgsales_12.csv").fillna(0)
df

# %% [markdown]
# Закодирирование категориальных признаков как целочисленный массив.

# %%
Oenc = OrdinalEncoder()
Oenc.fit(df[['Name','Platform','Year','Genre', 'Publisher']])
Oenc

# %% [markdown]
# Замена значений

# %%
df[['Name','Platform','Year','Genre', 'Publisher']] = Oenc.fit_transform(df[['Name','Platform','Year','Genre', 'Publisher']])
df

# %% [markdown]
# Закодирование категорианльного признака в целое число

# %%
Lenc = LabelEncoder()
Lenc.fit(df['Genre'])
df['Genre'] = Lenc.fit_transform(df['Genre'])
df

# %% [markdown]
# Вызов: Логиечской регрессии, К-ближайших соседей, дерево решений, опорных векторов, Гауссовский наивный байесовский метод

# %%
lgr = LogisticRegression()
knc = KNeighborsClassifier()
dtc = DecisionTreeClassifier()
svc = SVC()
gsnb = GaussianNB()

# %% [markdown]
# ##### Разбивка данных

# %%
X = df.drop(columns='Genre')
Y = df['Genre']
kf = KFold(n_splits = 5, shuffle = False, random_state=None)
kf

# %%
kf.split(df)

# %%
for train_index, test_index in kf.split(df):
    print("Train: ", train_index, "Tests: ", test_index)
    X_train_kfold = X.iloc[train_index]
    X_test_kfold = X.iloc[test_index]
    Y_train_kfold = Y.iloc[train_index]
    Y_test_kfold = Y.iloc[test_index]

    #Обучение и предсказание 'дерева решений'
    dtc = dtc.fit(X_train_kfold, Y_train_kfold)
    pred_dtc = dtc.predict(X_test_kfold)

    #Обучение и предсказание 'Логическая регрессия'
    lgr.fit(X_train_kfold, Y_train_kfold)
    pred_lgr = lgr.predict(X_test_kfold)

    #Обучение и предсказание 'K-ближайших соседей'
    knc.fit(X_train_kfold, Y_train_kfold)
    pred_knc = knc.predict(X_test_kfold)

    #Обучение и предсказание 'Опорные векторы'
    svc.fit(X_train_kfold, Y_train_kfold)
    pred_svc = svc.predict(X_test_kfold)

    #Обучение и предсказание 'Гауссовский наивный байесовский метод'
    gsnb.fit(X_train_kfold, Y_train_kfold)
    pred_gsnb = gsnb.predict(X_test_kfold)

    print("\nНабор предсказаний 'Дерева решений'", pred_dtc, "\nНабор предсказаний  'Логическая регрессия'", pred_lgr, "\nНабор предсказаний 'K-ближайших соседей'", pred_knc , "\nНабор предсказаний 'Опорные векторы'", pred_svc , "\nНабор предсказаний 'Гауссовский наивный байесовский метод'", pred_gsnb)

# %% [markdown]
# Вызов: случайный лес, градиентный бустинг

# %%
rfc = RandomForestClassifier()
gbc = GradientBoostingClassifier()

# %%
Y = df["Genre"]
X = df.drop(columns= "Genre")

kf = KFold(n_splits=4, shuffle=False, random_state=None)
kf

# %%
for train_index, test_index in kf.split(df):
    print("Train: ", train_index, "Tests: ", test_index)
    X_train_kfold = X.iloc[train_index]
    X_test_kfold = X.iloc[test_index]
    Y_train_kfold = Y.iloc[train_index]
    Y_test_kfold = Y.iloc[test_index]

    #Обучение и предсказание 'дерева решений'
    dtc = dtc.fit(X_train_kfold, Y_train_kfold)
    pred_dtc = dtc.predict(X_test_kfold)

    #Обучение и предсказание 'Логическая регрессия'
    lgr.fit(X_train_kfold, Y_train_kfold)
    pred_lgr = lgr.predict(X_test_kfold)

    #Обучение и предсказание 'K-ближайших соседей'
    knc.fit(X_train_kfold, Y_train_kfold)
    pred_knc = knc.predict(X_test_kfold)

    #Обучение и предсказание 'Опорные векторы'
    svc.fit(X_train_kfold, Y_train_kfold)
    pred_svc = svc.predict(X_test_kfold)

    #Обучение и предсказание 'Гауссовский наивный байесовский метод'
    gsnb.fit(X_train_kfold, Y_train_kfold)
    pred_gsnb = gsnb.predict(X_test_kfold)

    print("\nНабор предсказаний 'Дерева решений'", pred_dtc, "\nНабор предсказаний  'Логическая регрессия'", pred_lgr, "\nНабор предсказаний 'K-ближайших соседей'", pred_knc , "\nНабор предсказаний 'Опорные векторы'", pred_svc , "\nНабор предсказаний 'Гауссовский наивный байесовский метод'", pred_gsnb)

# %% [markdown]
# Вызов: линейная регрессия, полиноминальная регрессия, опорные векторы, дерево решений, случайный лес

# %%
lrc = LinearRegression()
prc = PolynomialFeatures()
svr = SVR()
dtr = DecisionTreeClassifier()
rfr = RandomForestRegressor()

# %%
Lenc = LabelEncoder()
Lenc.fit(df['JP_Sales'])
df['JP_Sales'] = Lenc.fit_transform(df['JP_Sales'])
df

# %%
Y = df['JP_Sales']
X = df.drop(columns= "JP_Sales")

kf = KFold(n_splits=4, shuffle=False, random_state=None)
kf

# %%
for train_index, test_index in kf.split(df):
    print("Train: ", train_index, "Tests: ", test_index)
    X_train_kfold = X.iloc[train_index]
    X_test_kfold = X.iloc[test_index]
    Y_train_kfold = Y.iloc[train_index]
    Y_test_kfold = Y.iloc[test_index]

    #Обучение и предсказание 'дерева решений'
    dtc = dtc.fit(X_train_kfold, Y_train_kfold)
    pred_dtc = dtc.predict(X_test_kfold)

    #Обучение и предсказание 'Логическая регрессия'
    lgr.fit(X_train_kfold, Y_train_kfold)
    pred_lgr = lgr.predict(X_test_kfold)

    #Обучение и предсказание 'K-ближайших соседей'
    knc.fit(X_train_kfold, Y_train_kfold)
    pred_knc = knc.predict(X_test_kfold)

    #Обучение и предсказание 'Опорные векторы'
    svc.fit(X_train_kfold, Y_train_kfold)
    pred_svc = svc.predict(X_test_kfold)

    #Обучение и предсказание 'Гауссовский наивный байесовский метод'
    gsnb.fit(X_train_kfold, Y_train_kfold)
    pred_gsnb = gsnb.predict(X_test_kfold)

    print("\nНабор предсказаний 'Дерева решений'", pred_dtc, "\nНабор предсказаний  'Логическая регрессия'", pred_lgr, "\nНабор предсказаний 'K-ближайших соседей'", pred_knc , "\nНабор предсказаний 'Опорные векторы'", pred_svc , "\nНабор предсказаний 'Гауссовский наивный байесовский метод'", pred_gsnb)


