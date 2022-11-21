# Crie uma tupla, chamando "times", com os elementos "Santos", "Flamengo" e "Palmeiras".
times = ('Santos', 'Flamengo', 'Palmeiras')
print(times)

# Acesse o segundo elemento desta tupla.
print(times[1])

""" Chame um método que permita extrair o nome ea idade fornecidos separadamente. Em seguida, imprima os valores de 
"nome" e "idade" para ver se funcionou corretamente."""
nome, idade = 'marcela,27'.split(',')
print(nome, idade)

""" Crie uma função que recebe como argumentos os dois valores de um retângulo e depois retorna a Área e o Perímetro do
retângulo. Chame a função com os argumentos 5 e 9 para verificar se funcionou corretamente."""


def arimetro(a, la):
    area = a * la
    perimetro = 2 * (a + la)
    return area, perimetro


print(arimetro(5, 9))
