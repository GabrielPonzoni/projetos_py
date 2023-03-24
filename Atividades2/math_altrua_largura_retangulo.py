#6. Desenvolva um programa que solicite ao usuário a altura e a largura de um 
#retângulo e exiba o perímetro e a área deste retângulo na tela

print('Informe a altura (h) e a largura (l) do retângulo:')
h, l= float(input()), float(input())
perimetro = h + l + h + l
area = h * l
print(f'O perímetro dessa figura é {perimetro:.2f}m e a sua área é {area:.2f}m\u00b2')
