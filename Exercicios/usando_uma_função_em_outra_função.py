""" Defina uma função que adiciona 5 ao parâmetro. Em seguida, defina outra função que multiplicará o número recém-
obtido por 10. Verifique se o seu código chamava a segunda função com um argumento de 2. A sua saída foi igual a 70? """


def adiciona_cinco(x):
    return x + 5


def multiplica_dez(x):
    return adiciona_cinco(x) * 10


print(adiciona_cinco(2), multiplica_dez(2))
