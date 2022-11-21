# Continue de onde paramos no exercício anterior.
import numpy as np
import matplotlib.pyplot as plt

rev_m = 150
rev_stdev = 7
iteracoes = 250

rev = np.random.normal(rev_m, rev_stdev, iteracoes)
cmv = - (rev * np.random.normal(0.25, 0.1))

print(cmv.mean(), cmv.std())

# Com base na receita prevista e nos valores das CMV, estime o lucro bruto esperado de sua empresa.
""" Lembrete: tenha cuidado ao estimar o lucro bruto. Se você armazenou o valor das CMV como um número negativo, o 
lucro bruto será igual às receitas mais as CMV. Se você criou CMV com um valor positivo, o lucro bruto seria igual às 
receitas menos CMV. De qualquer forma, você obterá o mesmo resultado para o lucro bruto. """

lucro_bruto = rev + cmv
print(lucro_bruto)

plt.figure(figsize=(15, 6))
plt.plot(lucro_bruto)
plt.show()

# Qual é o valor máximo e mínimo do lucro bruto obtido?
print(max(lucro_bruto))
print(min(lucro_bruto))

# Qual é a sua média e desvio padrão?
print(lucro_bruto.mean())
print(lucro_bruto.std())

""" Você se lembra o que é um histograma? Trace os dados do lucro bruto em um histrograma. Use 20 caixas diretamente 
para verificar a fistribuição dos dados. """
plt.figure(figsize=(10, 6))
plt.hist(lucro_bruto, bins=20)
plt.show()
