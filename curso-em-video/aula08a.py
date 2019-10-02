import math
#from math import sqrt, ceil
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
