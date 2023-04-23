#2. Solicite dois números inteiros "a" e "b" e imprima na tela se o primeiro é perfeitamente divisível
#pelo segundo (a % b), sem gerar resto;
print('Informe dois número inteiros "a" e "b": ')
a = int(input())
b = int(input())
perf = a % b == 0
#imp = a % b != 0
if (perf):
  print('O resto de {} com {} é perfeito! (igual a 0)'.format(a,b))
else:
  print('O resto de {} com {} é imperfeito! (difere de 0)'.format(a,b))
