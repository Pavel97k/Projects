# %%
import pandas as pd
import numpy as np

# библиотека для построения графиков
import seaborn as sns
# библиотека с упрощенными графиками
import matplotlib.pyplot as plot

# %%
df = pd.read_csv("vgsales_12.csv")
df

# %%
graph = sns.countplot(x="Platform", data = df)
graph.figure.set_figwidth(15)
graph.figure.set_figheight(10) 

# %%
graph = sns.barplot(x=df["Platform"], y=df["Global_Sales"])
graph.figure.set_figwidth(15)
graph.figure.set_figheight(10) 

# %%
graph = sns.displot(df["Year"], kde = True) 
# kind = "kde", kind = True - аргумент, позволяющий построить отдельный график оценки плотности ядра или 
# kde рисуется в виде линии поверх гистограммы и часто повторяет форму её форму, 
# но дает больше информации о характере распределения.
graph.figure.set_figwidth(10)
graph.figure.set_figheight(5)

# %%
graph = sns.boxplot(x="Genre", y="Global_Sales",data = df,palette='rainbow')
graph.figure.set_figwidth(15)
graph.figure.set_figheight(10) 

# %%
plot.figure(figsize=(15,10))
sns.heatmap(df.corr(numeric_only=True))

# %%
sns.pairplot(df)

# %%
graph = sns.PairGrid(df)
graph = graph.map_upper(sns.scatterplot)
graph = graph.map_lower(sns.kdeplot)
graph = graph.map_diag(sns.kdeplot, lw = 2)

# %%
df_min = df[['NA_Sales', 'EU_Sales', 'JP_Sales']] [::50]
df_min


