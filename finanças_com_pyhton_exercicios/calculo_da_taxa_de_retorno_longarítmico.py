import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

# Faça o retorno logarítimico para a Gerdau.
ggbr4 = wb.DataReader('GGBR4.SA', data_source='yahoo', start='2015-1-1')
ggbr4['retorno_longaritimico'] = np.log(ggbr4['Adj Close'] / ggbr4['Adj Close'].shift(1))
print(ggbr4['retorno_longaritimico'])

# Plote o resultado em um Gráfico.
ggbr4['retorno_longaritimico'].plot(figsize=(8, 7))
plt.show()

# Estime a média diária e a média anual dos retornos de log obtidos.
media_diaria = ggbr4['retorno_longaritimico'].mean()
print(media_diaria)

media_anual = ggbr4['retorno_longaritimico'].mean() * 250
print(media_anual)

# Imprima o resultado em uma forma apresentável.
media_diaria_porcentagem = round(media_diaria, 3) * 100
media_anual_porcentagem = round(media_anual, 2) * 100
print(f'A média diaria da Gerdal é de {media_diaria_porcentagem}% e a anual está em torno de '
      f'{media_anual_porcentagem}%')
