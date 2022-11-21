""" Atribua 200 a variavel x. Crie o seguinte trecho de código: Se x > 150, imprima "Grande"; se x > 100 e x <= 150,
 imprima "Médio"; e se x <= 100, imprima "Pequeno". Use as palavras-chaves If, Elif, e Else em seu código."""
x = 200
if x > 150:
    print('Grande')

elif 100 < x <= 150:
    print('Médio')

else:
    print('Pequeno')

""" Mantenha as duas primeiras consições do código anterior. Adicione uma nova instrução ELIF, de modo que, 
eventualmente, o programa imprima "Pequeno" se x >= 0 e x <= 100, e "Negativo" se x < 0. Deixe x levar o valor de 50
e depois de -50 para verificar se seu código está correto."""
x = -50
if x > 150:
    print('Grande')

elif 100 < x <= 150:
    print('Médio')

elif x < 0:
    print('Negativo')

else:
    print('Pequeno')
