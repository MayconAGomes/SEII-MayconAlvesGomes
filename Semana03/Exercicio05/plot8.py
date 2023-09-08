#%%

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("C:/Users/Windows 10/Desktop/Programação/Semana03/Exercicio05/athlete_events.csv")

dados.head()

masculinos = dados.loc[dados['Sex']=='M']
masculinos.head()

a = masculinos['Height']
p = masculinos['Weight']

plt.scatter(a,p)
plt.show()
# %%
