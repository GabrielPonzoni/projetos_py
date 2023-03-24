#3. So#3. Solicite dois números inteiros "a" e "b" e imprima na tela se o resultado da subtração entre eles
#(a - b) resulta em número positivo ou negativo. Considere o zero como positivo;

print('Informe dois número inteiros "a" e "b": ')
a = int(input()) 
b = int(input())

pos = (a - b) > 0
res = a - b
if(pos):
  print(f'A subtração deu positivo! -> {a} - {b} = {res}')
else:
  print(f'A subtração deu negativo! -> {a} - {b} = {res}')