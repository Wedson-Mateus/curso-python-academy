# A.(* Desafio! *) Crie um objeto de série de 10 valores inteiros gerados aleatoriamente.
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

serie = pd.Series(np.random.randint(10, size=10, dtype='int'), name='coluna 01')
print(serie)

""" B. Extraia os dados da yahoo para a Vale S.A. de 1° de janeiro de 2015 até o dia atual. O ticker de que você precisa
é 'VALE3.SA'."""
vale3 = wb.DataReader('VALE3.SA', data_source='yahoo', start='2015-1-1')
print(vale3)
