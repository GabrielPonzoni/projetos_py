#1. Implemente um programa que solicita dois números ao usuário e exibe na tela:
#a) A soma destes dois números
#b) A subtração destes dois números
#c) A multiplicação destes dois números
#d) A divisão destes dois números
#e) A divisão inteira destes dois números
#f) O resto da divisão inteira destes dois números
#g) A exponenciação destes dois números
#h) O maior destes dois números
#i) O menor destes dois números
#

n1,n2 = int(input('Usuário me informe dois números:\n')),int(input())
soma = (n1 + n2)
sub = (n1 - n2)
mult = (n1 * n2)
div = (n1/n2)
divd = (n1//n2)
rest = (n1 % n2)
exp = (n1 ** n1)
if (n1 > n2):
  maior = n1
  menor = n2
else:
  maior = n2
  menor = n1

print(f'\n a) A soma de {n1} + {n2} = {soma} \n b) A subtração de {n1} - {n2} = {sub} c) A multiplicação de {n1} X {n2} = {mult} \n d) A divisão de {n1}/{n2} = {div:.2f} \n e) A divisão inteira de {n1}//{n2} = {divd} \n f) O resto da divisão inteira de {n1}/{n2} = {rest} \n g) A exponenciação de {n1}^{n2} = {exp} \n h) O maior destes dois números é {maior} \n i) O menor destes dois números é {menor}')