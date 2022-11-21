""" Considere um portfólio composto por * VALE * e * GOL *. Você espera que os retornos dessas empresas apresentem
covariância alta ou baixa? Ou você poderia adivinhar qual seria a correlação? Será mais próximo de 0 ou mais próximo
de 1? Baixe os dados da Vale (‘VALE3’) do Yahoo Finance para o período ‘2010-1-1’ até hoje."""
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['VALE3.SA', 'GOLL4.SA']
dados = pd.DataFrame()

for t in tickers:
    dados[t] = wb.DataReader(t, data_source='yahoo', start='2010-1-1')['Adj Close']

retorno = np.log(dados / dados.shift(1))
print(retorno)

# VALE
# Risco Diario:
risco_diario_va = retorno['VALE3.SA'].std()
print(f'Vale Risco Diario:{risco_diario_va}')

# Risco Anual:
risco_anual_va = retorno['VALE3.SA'].std() * 250 ** 0.5
print(f'Vale Risco Anual: {risco_anual_va}')

# GOL
# Risco Diario:
risco_diario_go = retorno['GOLL4.SA'].std()
print(f'Gol Risco Diario:{risco_diario_go}')

# Risco Anual:
risco_anual_go = retorno['GOLL4.SA'].std() * 250 ** 0.5
print(f'Gol Risco Anual:{risco_anual_go}')

# Armazene as volatilidades das duas ações em uma matriz chamada "vol".
vol = retorno[['VALE3.SA', 'GOLL4.SA']].std() * 250 ** 0.5
print(vol)

# COVARIÂNCIA E A CORELAÇÃO
cov_matrix = retorno.cov()
print(cov_matrix)

cov_matrix_a = retorno.cov() * 250
print(cov_matrix_a)

# CALCULANDO O RISCO DE UMA CARTEIRA
# ESQUEMA DE PESAGEM IGUAL:
pesos = np.array([0.5, 0.5])

# Variância da Carteira:
carteira_var = np.dot(pesos.T, np.dot(retorno.cov() * 250, pesos))
print(carteira_var)
# Para obter o vetor de pesos tranposto, basta colocar '.T'

# Volatilidade da Carteira:
carteira_vol = (np.dot(pesos.T, np.dot(retorno.cov() * 250, pesos))) ** 0.5
print(carteira_vol)
print(str(round(carteira_vol, 5) * 100) + '%')
