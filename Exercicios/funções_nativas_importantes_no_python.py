# Obtenha o número máximo entre os valores 12, 18, 89, e 21.
numeros = (12, 18, 89, 21)
print(max(numeros))

# Obtenha o número mínimo entre os valores 12, 18, 89 e 21.
print(min(numeros))

# Encontre o valor absoluto de -400.
print(abs(-400))

# Arredonde o valor de 95,5.
print(round(95.5))

# Arredonde 87,582364 para o terceiro dígito.
print(round(87.582364, 3))

# Encontre a soma de todos os elementos na lista fornecida, denominada "Números".
numeros_two = [3, 7, 88, 3.3]
print(sum(numeros_two))

# Use uma função integrada para elevar 10 à potência de 5.
print(pow(10, 5))

# Quantos caracteres existem na palavra "Gratidão"?
print(len('Gratidão'))

""" Crie uma função, chamada "distancia_de_zer", que retorna o valorabsoluto de um único argumento fornecido e imprime 
uma instrução "Não Possível" se o argumento fornecido não for um número. Chame a função com valores de -77 e "Sucesso"
para verificar se ela funciona corretamente."""


def distancia_de_zero(x):
    if type(x) == str:
        return 'Não Possivel'

    else:
        return abs(x)


print(distancia_de_zero(-77))
print(distancia_de_zero('sucesso'))
