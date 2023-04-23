#6. Solicite duas letras "a" e "b" e imprima na tela se a letra "a" é igual, antecessora ou sucessora da
#letra "b";
print('Informe duas letras:')
a = input()
b = input()

igual = a == b
antes = a < b


if(igual):
  print('Igual')
elif(antes):
  print(f'{a} vem antes de {b}')
else:
  print(f'{a} vem depois de {b}')