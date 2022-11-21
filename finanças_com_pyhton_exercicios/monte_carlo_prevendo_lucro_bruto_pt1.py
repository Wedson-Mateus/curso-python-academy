""" Imagine que você é um gerente experiente e tem uma receita prevista de $ 150 milhões, com um desvio esperado de
$ 7 milhões. Você está convencido de que as CMV ficarão perto de 25% das receitas e seu desvio esperado é de 10% de
seu próprio valor. Use a função random.random de NumPy para simular o fluxo de receita potencial para 250 iterações
(que é o número de dias de negociação em um ano) e, em seguida, o valor previsto de CMV."""

import numpy as np
import matplotlib.pyplot as plt

rev_m = 150
res_stdev = 7
iteracoes = 250

rev = np.random.normal(rev_m, res_stdev, iteracoes)
print(rev)

# Trace os dados obtidos para receitas e CMV em um gráfico e observe o comportamento dos valores obtidos.
plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

cmv = - (rev * np.random.normal(0.25, 0.1))
plt.figure(figsize=(15, 6))
plt.plot(cmv)
plt.show()

# CMV médio:
print(cmv.mean())

# CMV desvio padrão:
print(cmv.std())
