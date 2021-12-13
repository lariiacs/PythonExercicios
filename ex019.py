import random
nome1 = str(input('digite o primeiro nome: '))
nome2 = str(input('digite o segundo nome: '))
nome3 = str(input('digite o terceiro nome: '))
lista = (nome3,nome2,nome1)
print('o nome escolhido foi: {}'.format(random.choice(lista)))