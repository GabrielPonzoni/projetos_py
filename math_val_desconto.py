#5. Implemente um programa que solicita ao usuário o preço de um calçado e o 
#percentual de desconto. Em seguida, calcule o valor do desconto e o valor final
#a ser pago pelo calçado.

val = float(input('Informe o preço sem desconto do calçado: '))
porc = float(input('Informe agora o porcentual de desconto: '))
vali = val * porc/100
valf = val - vali
print('Desconto: R${:.2f}'.format(vali))
print('Valor final: R${:.2f}'.format(valf))