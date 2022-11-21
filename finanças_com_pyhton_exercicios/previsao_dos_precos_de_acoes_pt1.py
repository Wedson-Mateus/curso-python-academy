# Baixe os dados do itau('ITUB4.SA') do Yahoo Finance para o período '2000-1-1' até hoje.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

ticker = 'ITUB4.SA'
dados = pd.DataFrame()
dados[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2000-1-1')['Adj Close']

# Use o método .pct_change() para obter os retornos de log do Itau para o período designado.
log_retorno = np.log(1 + dados.pct_change())
print(log_retorno.tail())
plt.figure(figsize=(10, 6))
plt.plot(dados)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(log_retorno)
plt.show()

# Atribua o valor médio dos retornos de log a uma variável, chamada "U", e sua variância a uma, chamada "var".
u = log_retorno.mean()
print(u)

var = log_retorno.var()
print(var)

# Calcule o Drift.
drift = u - (0.5 * var)
print(drift)

# Armazene o desvio padrão dos retornos do log em uma variável, chamada "stdev".
stdev = log_retorno.std()
print(stdev)
