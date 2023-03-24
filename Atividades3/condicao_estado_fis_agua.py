#5. Solicite um número inteiro "n" representando uma temperatura em graus Celsius. Imprima na
#tela se nessa temperatura a água se encontra em estado sólido (abaixo de zero), líquido (entre
#zero e 100) ou gasoso (acima de 100);
temp = int(input('Qual a temperatura em graus Celsius? '))
solid = temp < 0
liq = temp >= 0 and temp < 100

if(solid):
  print(f'A agua está sólida pq ta frioooo {temp}Cº')
elif(liq):
  print(f'A agua está liquido porque tamo na praia ehhehe {temp}Cº')
else:
  print(f'A agua está em estado gasoso porque to fazendo meu mate {temp}Cº')