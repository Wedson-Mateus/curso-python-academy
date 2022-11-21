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

# Use ".values" para transformar os objetos drift e stdev em matrizes.
print(type(drift))
print(drift.values)

print(type(stdev))
print(stdev.values)

""" Prever os preços das ações futuras para todos os dias de negociação do ano seguinte portanto, atribua 250 a 
't_intervals'. Vamos examinar 10 resultados possíveis. Vincule 'interações' ao valor de 10. """
t_intervals = 250
iterations = 10

# Calcule os retornos diários.
retorno_d = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
print(retorno_d)
