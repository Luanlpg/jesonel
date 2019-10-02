frase = 'Curso em Video Python'
print(frase)

print(frase[3:13])

print(frase[:13])
print(frase[13:])

print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print(frase[9])
print(frase[9:13])#pega do 9 ao 12
print(frase[9:21])# pega do 9 ao 20
print(frase[9:21:2]) #pega do 9 ao 21 pulando de 2 em 2

print(frase[:5]) # pega do 0 ao 4
print(frase[15:]) # pega do 15 em diante


print(frase[9::3]) # começa no 9 e vai ate o final pulando de 3 em 3

len(frase) # conta o numero de caracteres
print(len(frase))

print(frase.count('o')) # conta quantas vezes aparece a letra 'o'

print(frase.count('o', 0, 13))# conta quantas vezes aparece a letra 'o' entre os caracteres de 0 a 12

print(frase.find('deo')) # mostra a posicao que começou o 'deo'

print('Curso' in frase) # se existe a palavra curso na variavel frase

print(frase.replace('Python', 'Android')) #substitui

print(frase.upper().count('O'))

print(frase.split())

print('-'.join(frase.split()))
# OU
dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) #mostra a letra da dividido 2

frase = 'Curso em Video Python'
print(len(frase.strip()))

print(frase.split()[0])


frase.replace('Python', 'Android')
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)

print(len(frase.replace(' ', '')))
