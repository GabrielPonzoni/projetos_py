#3. Solicite um número ao usuário. Sendo este número uma temperatura em graus 
#Fahrenheit,faça um programa que converte esta temperatura em graus Celsius e 
#exibe o resultado na tela. Celsius = (Fahrenheit - 32) / 1.8

print('Me informe uma temperatura em graus Fahrenheit: ')
fah = float(input())
cel = (fah - 32)/1.8
print('Fahrenheit para Celsios: {:.1f}'.format(cel))