""" Crie um ‘loop’ que imprimirá todas as variáveis de uma determinada lista multiplicadas por 2. Deixe a lista conter
todos os números de 1 a 27. Crie-a com a ajuda da função range()"""
lista = list(range(1, 28))
print(lista)
for n in lista:
    print(n * 2, end=' ')
print('FIM!!!')

""" Crie um pequeno programa que execute um loop sobre todos os valores de 1 a 30. Deixe-o imprimir todos os números 
ímpares e, no lugar dos números pares, deverá imprimir "Par". Use a função range() para resolver este ecercício"""
for n in range(1, 31):
    if n % 2 == 1:
        print(n, end=' ')

    else:
        print('Par', end=' ')
print('FIM!!!')

""" Você tem a seguinte lista de números. Repita esta lista, imprimindo cada valor da lista multiplicado por 10. 
Encontre duas soluções para este problema."""
c = 1
numeros = [1, 2, 3, 4, 5, 6]
while c <= len(numeros):
    print(numeros[c - 1] * 10, end=' ')
    c += 1
print('FIM!!!')

for v in numeros:
    print(v * 10, end=' ')
print('FIM!!!')
