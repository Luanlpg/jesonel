import random

aluno1 = input('Digite o nome do Primeiro aluno: ')
aluno2 = input('Digite o nome do Segundo aluno: ')
aluno3 = input('Digite o nome do Terceiro aluno: ')
aluno4 = input('Digite o nome do Quarto aluno: ')

Lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(Lista)
print("A ordem de apresentação é: ")
print(Lista)
