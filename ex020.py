import random
nome1 = str(input('digite o primeiro nome: '))
nome2 = str(input('digite o segundo nome: '))
nome3 = str(input('digite o terceiro nome: '))
nome4 = str(input('digite o quarto nome: '))
lista = [nome4, nome3, nome2, nome1]
random.shuffle(lista)
print('a ordem de chamada é: {}'.format(lista))
