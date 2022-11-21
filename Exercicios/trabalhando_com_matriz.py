# Importando a biblioteca numpy
import numpy as np

# Matriz base
a = np.array([[0, 1, 2, 3, 15.25, 6.15], [4.15, 5.65, 6.23, 7, 8.0, 81.5], [4, 5, 8.3, 7, 17.5, 20]])
print(a)
print('-=' * 20)

# Verifique se a dimensão que você criu está correta(use"*.shape*")
print(a.shape)
print('-=' * 20)

# Substitua o 5° elemento da 2ª linha linha por 19,75.
a[1, 4] = 19.75
print(a)

# Extrai a 2ª e a 3ª linha da matriz que você criou.
print('-=' * 20)
print(f'{a[1]}\n{a[2]}')

