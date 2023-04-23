#4. Solicite um número qualquer seguido de um valor inicial e um final de um intervalo. Mostre uma
#mensagem informando se o número digitado está abaixo, dentro ou acima do intervalo;
numM = int(input('Informe um número qualquer '))
num1 = int(input('Informe um valor inicial '))
num2 = int(input('Informe um valor final '))

abaixo = numM < num1
dentro = numM > num1 and numM < num2

if(abaixo):
  print(f'O número {numM} esta abaixo do intervalo. Observe de {numM}[{num1}-{num2}]')
elif(dentro):
  print(f'O número {numM} esta dentro do intervalo de [{num1}-{numM}-{num2}]')
else:
  print(f'O número {numM} esta acima do intervalo de [{num1}-{num2}]{numM}')