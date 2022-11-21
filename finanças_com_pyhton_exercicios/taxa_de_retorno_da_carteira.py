import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Dados base.
tickers = ['PETR4.SA', 'BBAS3.SA', 'GGBR4.SA', 'USIM5.SA', 'GOLL4.SA']
dados = pd.DataFrame()
for t in tickers:
    dados[t] = wb.DataReader(t, data_source='yahoo', start='2013-1-1')['Adj Close']

# Checando se os dados estão corretos.
dados.info()
print('-=' * 40)

# Verificando os 5 primeiros valores de cada ação.
print(dados.head())
print('-=' * 40)

# Verificando os 5 ultimos valores de cada ação.
print(dados.tail())
print('-=' * 40)

# Normalize para cem e plote os dados em um gráfico (você pode aplicar o método .loc() ou .iloc())
print(dados.iloc[0])
print('-=' * 40)
(dados / dados.iloc[0] * 100).plot(figsize=(10, 8))
plt.show()

# Obtenha o retorno simples dos títulos da carteira e armazene os resultados em uma nova tabela.
retorno = (dados / dados.shift(1))-1
print(retorno)
print('-=' * 40)

# Primeiro, suponha que você gostaria de criar um portfólio igualmente ponderado. Crie a matriz, nomeando-a "pesos".
pesos = np.array([0.20, 0.20, 0.20, 0.20, 0.20])

# Obtenha os retornos anuais de cada uma das ações e, a seguir, calcule o produto escalar desses retornos e os pesos.
retorno_anual = retorno.mean() * 250
produto = float(np.dot(retorno_anual, pesos))
print(retorno_anual)
print(produto)
print('-=' * 40)

# Transforme o resultado em porcentagem.
acoes = str(round(produto, 3) * 100) + '%'
print(acoes)
