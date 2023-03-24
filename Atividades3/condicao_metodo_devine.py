#8. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule
#seu peso ideal, utilizando as seguintes fórmulas:
#• Para homens: (72.7*h) - 58 (h = altura)
#• Para mulheres: (62.1*h) - 44.7 (h = altura)
#• Após calcular o peso ideal para a pessoa, solicite o seu peso e informe se ela está dentro da
#faixa ideal (peso +/- 5%), acima ou abaixo do peso ideal.

h = float(input('Informe a altura de uma pessoa: '))
s = input('Informe o sexo de uma pessoa: ')

s_low = s.casefold().strip()

confirma = False

while(confirma is False):
  if(s_low == 'homem'):
    confirma = True
  elif(s_low == 'mulher'):
    confirma = True
  else:
    print('Informe um valor válido para sexo (Homem ou Mulher)')
    s = input('Informe o sexo de uma pessoa: ')
    s_low = s.casefold().strip()


if(s_low == 'homem'):
  peso_ideal_H = (72.7 * h) - 58 #metodo Devine
elif(s_low == 'mulher'):
  peso_ideal_M = (62.1 * h) - 44.7 #metodo Devine
else:
  print('Dados informados inválidos')
  
peso_ideal_min_h = abs((peso_ideal_H * 0.05) - peso_ideal_H)
peso_ideal_min_m = abs((peso_ideal_M * 0.05) - peso_ideal_M)

peso_ideal_max_h = (peso_ideal_H * 0.05) + peso_ideal_H
peso_ideal_max_m = (peso_ideal_M * 0.05) + peso_ideal_M

#print('Homem',peso_ideal_min_h)
#print('Homem',peso_ideal_H)
#print('Homem',peso_ideal_max_h)

#print('Mulher',peso_ideal_min_m)
#print('Mulher',peso_ideal_M)
#print('Mulher',peso_ideal_max_m)

peso = float(input('Informe seu peso: '))

peso_acima_h = peso > peso_ideal_max_h
peso_acima_m = peso > peso_ideal_max_m

peso_dentro_h = peso >= peso_ideal_min_h and peso <= peso_ideal_max_h
peso_dentro_m = peso >= peso_ideal_min_m and peso <= peso_ideal_max_m

peso_abaixo_h = peso < peso_ideal_min_h
peso_abaixo_m = peso < peso_ideal_min_m

#tenta usar if(s_low == 'homem') se for verdadeiro continua caso contrario sai do laço

if(s_low == 'homem' and peso_acima_h):
  print('Seu peso está acima do limite de {:.2f} e {:.2f} sendo ele: {:.2f} kg'.format(peso_ideal_min_h, peso_ideal_max_h, peso))
elif(s_low == 'homem' and peso_dentro_h):
  print('Seu peso está dentro do limite de {:.2f} e {:.2f} sendo ele: {:.2f} kg'.format(peso_ideal_min_h, peso_ideal_max_h, peso))
elif(s_low == 'homem' and peso_abaixo_h):
  print('Seu peso está abaixo do limite de {:.2f} e {:.2f} sendo ele: {:.2f} kg'.format(peso_ideal_min_h, peso_ideal_max_h, peso))
elif(s_low == 'mulher' and peso_acima_m):
  print('Seu peso está acima do limite de {:.2f} e {:.2f} sendo ele: {:.2f} kg'.format(peso_ideal_min_m, peso_ideal_max_m, peso))
elif(s_low == 'mulher' and peso_dentro_m):
  print('Seu peso está dentro do limite de {:.2f} e {:.2f} sendo ele: {:.2f} kg'.format(peso_ideal_min_m, peso_ideal_max_m, peso))
elif(s_low == 'mulher' and peso_abaixo_m):
  print('Seu peso está abaixo do limite de {:.2f} e {:.2f} sendo ele: {:.2f} kg'.format(peso_ideal_min_m, peso_ideal_max_m, peso))
else:
  print('Algo deu errado!')