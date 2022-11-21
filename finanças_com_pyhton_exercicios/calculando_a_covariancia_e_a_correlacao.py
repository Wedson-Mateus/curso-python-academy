""" Considere um portfólio composto por * VALE * e * GOL *. Você espera que os retornos dessas empresas apresentem
covariância alta ou baixa? Ou você poderia adivinhar qual seria a correlação? Será mais próximo de 0 ou mais
próximo de 1? Baixe os dados da Vale ('VALE3') do Yahoo Fimance para o período '2010-1-1' até hoje. """
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['VALE3.SA', 'GOLL4.SA']
dados = pd.DataFrame()

for t in tickers:
    dados[t] = wb.DataReader(t, data_source='yahoo', start='2010-1-1')['Adj Close']

retorno = np.log(dados / dados.shift(1))
print(retorno)
print('-=' * 20)

# VALE
# Risco Diario:
risco_diario_va = retorno['VALE3.SA'].std()
print(risco_diario_va)
print('-' * 40)

# Risco Anual:
risco_anual_va = retorno['VALE3.SA'].std() * 250 ** 0.5
print(risco_anual_va)
print('-' * 40)

# GOL
# Risco Diario:
risco_diario_go = retorno['GOLL4.SA'].std()
print(risco_diario_go)
print('-' * 40)

# Risco Anual:
risco_anual_go = retorno['GOLL4.SA'].std() * 250 ** 0.5
print(risco_anual_go)
print('-' * 40)

# Armazene as volatilidades das duas ações em uma matriz chamada "vol".
vol = retorno[['VALE3.SA', 'GOLL4.SA']].std() * 250 ** 0.5
print(vol)
print('-' * 40)

# COVARIÂNCIA E A CORRELAÇÃO
# Covariância Diaria
cov_matrix = retorno.cov()
print(cov_matrix)
print('-' * 40)

# Covariância Anual
cov_matrix_a = retorno.cov() * 250
print(cov_matrix_a)
print('-' * 40)

# CorrelaÇão
corr_matrix = retorno.corr()
print(corr_matrix)
