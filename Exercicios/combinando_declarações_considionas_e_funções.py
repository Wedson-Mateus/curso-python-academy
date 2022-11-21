""" Defina uma função, chamada compare_as_duas(), com dois argumentos. Se o primeiro for maior que o segundo, deixe
imprimir "Maior". Se o segundo for maior, deve imprimir "Menor". Deixe imprimir "Igual" se os dois valores forem o mesmo
número"""


def compare_as_duas(x, y):
    if x < y:
        print('Maior')

    elif x > y:
        print('Menor')

    else:
        print('Igual')


compare_as_duas(3, 3)
