from pandas_datareader import data as wb
vale = wb.DataReader('VALE3.SA', data_source='yahoo', start='2015-1-1')

""" Use o método "info" para obter estatísticas básicas sobre os dados extraídos no exercício anterior (dados da 
Morningstar para a VALE S.A a partir de 1 de janeiro de 2015 até hoje)."""
print(vale.info())
print('-=' * 45)

# Aplique os métodos "head" e "tail" e observe a saída.
print(vale.head())
print('-=' * 45)
print(vale.tail())
