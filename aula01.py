print('em qual numero eu estou penssando? entre 1 a 10')
from random import randint
robo = randint(1, 10)
cont = 0
while True:
    eu = int(input('digite um numero:'))
    cont += 1
    if eu == robo:
        break
print(f'parabens voce aceto com {cont} tentativas')