import random

numero = random.randint(1,5)
print(numero)

numeroadvinhado = int(input('Advinhe um numero de 1 a 5: '))
if numeroadvinhado == numero:
    print('Voce adivinhou!!!')
else:
    print('Voce nao acertou!')
