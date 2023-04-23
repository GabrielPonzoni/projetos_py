#1. Solicite um número inteiro "n" e imprima na tela se ele é par ou ímpar;
n = int(input('Informe um número inteiro:'))

if(n%2 == 0):
  print('O número {} é par!'.format(n))
else:
  print('O número {} é impar!'.format(n))