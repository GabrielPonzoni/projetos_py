#4. Implemente um programa que solicita um número ao usuário. Sendo este número 
#uma velocidade em km/h, faça um programa para converter esta velocidade em m/s 
#e exiba o resultado na tela.

print('Informe a velocidade do veículo em km/h:')
km = float(input())
ms = km/3.6
print('Isso equivale à {:.2f} m/s'.format(ms))