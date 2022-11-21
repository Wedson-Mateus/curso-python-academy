""" Você é fornecido com a lista 'numeros'. Complete o código na célular a seguir. Use um while loop para contar o
número de valores abaixo de 40."""
numeros = [1, 35, 12, 24, 31, 51, 70, 100]


def conatador(lista):
    c = 0
    lista = sorted(lista)
    while lista[c] < 40:
        c += 1

    return c


print(conatador(numeros))
