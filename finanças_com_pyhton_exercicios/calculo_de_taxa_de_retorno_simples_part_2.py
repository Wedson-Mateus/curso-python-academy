from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# informações base.
sabesp3 = wb.DataReader('SBSP3.SA', data_source='yahoo', start='2010-1-1')
sabesp3['taxa_de_retorno'] = (sabesp3['Adj Close'] / sabesp3['Adj Close'].shift(1))-1
print(sabesp3['taxa_de_retorno'])

# Trace os retornos simples em um gráfico.
sabesp3['taxa_de_retorno'].plot(figsize=(8, 7))
plt.show()
print('-=' * 40)

# Calcule o retorno médio diário.
retonor_diario = sabesp3['taxa_de_retorno'].mean()
print(retonor_diario)

# Estime o retorno médio anual.
retonor_anual = sabesp3['taxa_de_retorno'].mean() * 250
print(retonor_anual)

# Imprima a versão percentual do resultado como float com 2 dígitos após o ponto decimal.
print(f'{round(retonor_anual, 4) * 100}%')
