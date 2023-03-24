#7. Desenvolva um programa que solicite dois números ao usuário e que exiba o 
#resultado do primeiro número elevado ao segundo, ou seja, potência

print('Informe dois números inteiros: ')
x, y= int(input()),int(input())
val1 = pow(x,y)
print(f'Resultado: {x}^{y} = {val1}')