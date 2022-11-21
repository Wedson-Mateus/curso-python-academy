""" Considere três índices famosos do mercado americano e o nosso Índice Bovespa(B3) - Dow Jones, S&P 500, Nasdaq e o
índice Bovespa para o período de 1° de janeiro de 2000 até hoje."""
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

siglas = ['^DJI', '^GSPC', '^IXIC', '^BVSP']
dataframe = pd.DataFrame()

for s in siglas:
    dataframe[s] = wb.DataReader(s, data_source='yahoo', start='2000-1-1')['Adj Close']

print(dataframe)
print('-=' * 40)

# Verificando os primeiros valores.
print(dataframe.head())
print('-=' * 40)
# Verificando os ultimos valores.
print(dataframe.tail())
print('-=' * 40)

# Normalize os dados para 100 e plote os resultados em um gráfico.
(dataframe / dataframe.iloc[0] * 100).plot(figsize=(13, 6))
plt.show()

# Obtenha os retornos simples dos índices.
indice_retorno = dataframe / dataframe.shift(1)-1
print(indice_retorno.tail())
print('-=' * 40)

# Estime o retorno médio anual de cada índice.
retorno_anual = indice_retorno.mean() * 250
print(retorno_anual)
print('-=' * 40)

# Facilitando a compreensão dos dados.
porcentagem = str(round(retorno_anual, 3) * 100)
print(porcentagem)
