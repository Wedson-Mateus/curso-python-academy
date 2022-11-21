""" Neste exercício, você usará os mesmos dicionários que usamos na lição - "precos" e "quantidade". Desta vez, não
calcule apenas todo o dinheiro que Carlos gastou. Calcule quatno ele gastou em produtos com preço de 5 reais ou mais."""
precos = {'macarrão': 4,
          'lasanha': 5,
          'hamburguer': 2, }

quantidade = {'macarrão': 6,
              'lasanha': 10,
              'hamburguer': 0, }

gastos = maior_5 = menor_5 = 0

for g in precos:
    gastos += (precos[g] * quantidade[g])
    print(gastos)

    if precos[g] >= 5:
        maior_5 += (precos[g] * quantidade[g])

# E quanto Carlos gastou em prutos que custam menos de 5 dólares?
    if precos[g] < 5:
        menor_5 += (precos[g] * quantidade[g])

print(maior_5)
print(menor_5)
