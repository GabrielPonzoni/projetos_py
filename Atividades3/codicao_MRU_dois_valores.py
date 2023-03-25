'''
Nome do programa: VELOCIDADE, TEMPO E DISTANCIA 
Descrição: Este programa recolhe apenas 2 valores de 3 tendo essas duas varíaveis na mão ele escolhe em qual equação o problema 
se encaixa
Autor: Gabriel Ponzoni
Data de criação: 25 de março de 2023
Versão: 1.0
Instruções de uso: Informe apenas dois valores aquele que não quiser informar precione a tecla 'ENTER'.
Restrições de uso: None
'''

#7. Utilizando a equação do MRU (distanciaância = velocidadeocidade * tempo), desenvolva um programa que
#solicite os 3 dados, mas receba apenas 2 e calcule o terceiro. Os dados devem ser números
#fracionários, e o dado a ser calculado deve ser informado como vazio, apenas pressionando
#ENTER.

print('Informe *dois* valores, dentre eles: a velocidadeocidade, o tempo e a distanciância! ')

#programa solicita 3 valores sendo um deles esperado '';
velocidade = input('Velocidade: ') 
tempo = input('Tempo(horas): ') 
distancia = input('Distancia(quilometros): ') 

if velocidade == '':
    tempo_float = float(tempo)
    distancia_float = float(distancia)
    
    print('Valor: Velocidade(?)'.format(velocidade))
    print('Valor: Tempo({:.2f})'.format(tempo_float))
    print('Valor: Distância({:.2f})'.format(distancia_float))
    
    velocidade = distancia_float/tempo_float
    velocidade_float = float(velocidade)
    print('A velocidadeocidade média é de: {:.2f} km/h'.format(velocidade_float))
    #primeira validação se velocidade for == '' ele executa esse bloco de código;
elif tempo == '':
    distancia_float = float(distancia)
    velocidade_float = float(velocidade)
    
    print('Valor: Velocidade({:.2f})'.format(velocidade_float))
    print('Valor: Tempo(?)'.format(tempo))
    print('Valor: Distância({:.2f})'.format(distancia_float))
    
    tempo = distancia_float/velocidade_float
    tempo_float = float(tempo)
    print('O tempo do trajeto é de: {:.2f} hora(s)'.format(tempo_float))
    #segunda validação se tempo for == '' ele executa esse outro bloco;
elif distancia == '':
    velocidade_float = float(velocidade)
    tempo_float = float(tempo)
    
    print('Valor: Velocidade({:.2f})'.format(velocidade_float))
    print('Valor: Tempo({:.2f})'.format(tempo_float))
    print('Valor: Distância(?)')
    
    distancia = velocidade_float * tempo_float
    distancia_float = float(distancia)
    print('A distanciância do trajeto é de: {:.2f} quilometros'.format(distancia_float))
    #ultima possível validação é utilizar verificar se a distãncia foi o vaziu 
else:
    print('Valores informados inválidos tente novamente!')
    #caso todos valores forem informados ou nenhum for informado ele entra nesse else.
    
#Esse código foi escrito por Gabriel Ponzoni, se copiar grande parte dele por favor lembre de dar créditos
#Versão do Código: v1.0
