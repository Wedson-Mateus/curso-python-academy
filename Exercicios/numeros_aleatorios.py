# Importe o módulo aleatório e gere uma probabilidade aleatória.
import random
import numpy as np
probabilidade = random.random()
print(probabilidade)

# Em seguida, gere um número inteiro aleatório no intervalo de 1 a 40.
interiro = random.randint(1, 40)
print(interiro)

""" Por fim, importe Numpy e crie uma matriz 3 x 5-dimensional, preenchida com interios aleatórios no intervalo
de 1 e40. """
# Importei a biblioteca no começo do código, pois sei que importar ela aqui, não seria uma boa prática no python.
matriz = np.random.randint(1, 40, (3, 5))
print(matriz)
