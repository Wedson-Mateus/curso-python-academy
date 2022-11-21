# Baixe os dados da Sabesp('SBSP3.SA') do Yahoo Finence para o período '2010-1-1' até hoje.
from pandas_datareader import data as wb

sbsp3 = wb.DataReader('SBSP3.SA', data_source='yahoo', start='2010-1-1')
print(sbsp3)

""" Aplique os métodos ** .head() ** e ** .Tail ** para verificar se os dados estão corretos. Sempre preste atenção nas
datas. Tente ter uma ideia de como o preço das ações mudou durante o período."""
print('-=' * 40)
print(sbsp3.head())
print('-=' * 40)
print(sbsp3.tail())

# Calcule os retornos simples de 'SBSP3.SA' para o período determinado.
print('-=' * 40)
sbsp3['taxa_de_retorno'] = (sbsp3['Adj Close'] / sbsp3['Adj Close'].shift(1))-1
print(sbsp3['taxa_de_retorno'])
