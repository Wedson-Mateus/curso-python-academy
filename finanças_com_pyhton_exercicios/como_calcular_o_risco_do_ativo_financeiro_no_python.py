""" Baixe os dados da Vale('VALE3') do yahoo Finance para o período '2010-1-1' até hoje. Avalie o risco diário e anual
de 'VALE3'. Repita o exercício para a Gol linhas aereas pelo mesmo período."""
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

acoes = ['VALE3.SA', 'GOLL4.SA']
dados = pd.DataFrame()

for a in acoes:
    dados[a] = wb.DataReader(a, data_source='yahoo', start='2010-1-1')['Adj Close']

retorno = np.log(dados / dados.shift(1))

retorno['VALE3.SA'].mean()
retorno['VALE3.SA'].mean() * 250

retorno['GOLL4.SA'].mean()
retorno['GOLL4.SA'].mean() * 250

# --------------- VALE ---------------
# Risco Diario:
retorno['VALE3.SA'].std()

# Risco Anual:
retorno['VALE3.SA'].std() * 250 ** 0.5


# --------------- GOL ---------------
# Risco Diario:
retorno['GOLL4.SA'].std()

# Risco Anual:
retorno['GOLL4.SA'].std() * 250 ** 0.5

# Armazene as volarilidades das duas ações em um matriz chamada "vol".
vol = retorno[['VALE3.SA', 'GOLL4.SA']].std() * 250 ** 0.5
print(vol)
