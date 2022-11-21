# Lista base
numeros = [8, 56, 87, 94, 15, 31]

# Usando slicing de lista, obtenha os números 94 e 15.
print(numeros[3:5])

# Usando o sliciing, extraia os primeiros quatro elementos da lista.
print(numeros[:4])

# Usando o slicing, extraia todos os elementos da lista a partir da 3 posição.
print(numeros[3:])

# Usando o slicing, extraia os últimos 4 elementos da lista.
print(numeros[2:])

# Qual é a posição do valor 15?
print(numeros.index(15))

""" Crie uma lista chamada "dois_numeros". Sejam seus elementos os valores 1 e 2. Em seguida, crie um novo, denominado
"todos_numeros", que conterá as listas "Números" e "dois_numeros"."""
dois_numeros = [1, 2]
todos_numeros = [numeros, dois_numeros]
print(todos_numeros)

# Classifique todos os números na lista "Números", do maior para o menor.
numeros.sort(reverse=True)
print(numeros)
