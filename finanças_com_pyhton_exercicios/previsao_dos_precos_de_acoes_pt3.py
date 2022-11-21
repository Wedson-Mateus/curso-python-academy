# Previsão de preços de ações no futuro - continuação:
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

ticker = 'ITUB4.SA'
dados = pd.DataFrame()
dados[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2000-1-1')['Adj Close']

log_retorno = np.log(1 + dados.pct_change())
u = log_retorno.mean()
var = log_retorno.var()
drift = u - (0.5 * var)
stdev = log_retorno.std()

print(drift.values)
print(stdev.values)

t_intervals = 250
iterations = 10

retorno_d = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))

# Crie uma variável s0 igual ao último preço de fechamento ajustado do Itaul. Use o método "iloc".
s0 = dados.iloc[-1]
print(s0)

# Crie uma variável "lista_preco" com a mesma dimensão da matriz retorno_d.
lista_preco = np.zeros_like(retorno_d)
print(lista_preco)
print(lista_preco[0])

# Defina os valores na primeira linha da matriz price_list iguais a s0.
lista_preco[0] = s0
print(lista_preco)

""" Crie um loop no intervalo(1, t_intervals) que reatribui ao preço no tempo t o produto do preço no dia (t-1) com o 
valor dos retornos diários em t. """
for t in range(1, t_intervals):
    lista_preco[t] = lista_preco[t - 1] * retorno_d[t]

print(lista_preco)

# Finalmente, plote os dados da lista de preços obtidos.
plt.figure(figsize=(10, 6))
plt.plot(lista_preco)
plt.show()
