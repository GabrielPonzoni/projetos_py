#2. Solicite um número ao usuário. Sendo este número uma temperatura em graus 
#Celsius, faça um programa que converte esta temperatura para graus Fahrenheit e
#exibe o resultado na tela. Fahrenheit = Celsius * 1.8 + 32

print('Me informe uma temperatura em graus Celsius: ')
cel = float(input())
fah = cel * 1.8 + 32
print('Celsios para Fahrenheit: {:.1f}'.format(fah))