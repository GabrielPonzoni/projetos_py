#7. Utilizando a equação do MRU (distância = velocidade * tempo), desenvolva um programa que
#solicite os 3 dados, mas receba apenas 2 e calcule o terceiro. Os dados devem ser números
#fracionários, e o dado a ser calculado deve ser informado como vazio, apenas pressionando
#ENTER.
print('Informe a velocidade, o tempo para calcularmos a distância!')
vel = float(input('Informe a velocidade: '))
time = float(input('Informe o tempo: '))
dist = input('ENTER')
dist = vel * time
print(f'A distância percorrida foi de {dist} km/h.')
