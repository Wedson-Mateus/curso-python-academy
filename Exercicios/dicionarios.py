# Este é um menu de um restaurante próximo:
menu = {'prato_1': 'macarrão', 'prato_2': 'salada', 'prato_3': 'Hamburger', 'prato_4': 'peixe'}

# Qual a segunda refeição da lista?
print(menu['prato_2'])

# Adicione uma nova refeição — "frango".
menu['prato_5'] = 'frango'
print(menu)

# Substitua o hambúrguer por o omelete.
menu['prato_3'] = 'omelete'
print(menu)

# Anexe a lista de sobremesa na forma de uma sexta refeição.
sobremesas = ['Bolo', 'Sorvete', 'chocolate']
menu['prato_6'] = sobremesas
print(menu)

""" Crie um novo dicionário que contenha as cinco primeiras refeições como chave e atribua os seguintes cinco valores 
como preços (em reais): 10, 5, 8, 12, 5. Comece por lista_de_preco = {}"""
lista_de_preco = {}
lista_de_preco['macarrão'] = 10
lista_de_preco['salada'] = 5
lista_de_preco['omelete'] = 8
lista_de_preco['peixe'] = 12
lista_de_preco['frango'] = 5
print(lista_de_preco)

# use o método .get() para verificar o preço do omelete.
print(lista_de_preco.get('omelete'))
