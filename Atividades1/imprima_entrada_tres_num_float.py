#8. Solicite ao usuário que ele informe um número fracionário e o imprima como um número inteiro 
#e depois como um número fracionário com três casas decimais

num_frac = float(input("Informe um número fracionário: "))

#transformo o str/fraçao em inteiro
num_int = int(num_frac)
print("Número fracionado formatado para inteiro: " ,num_int)

#transformando num número fracionado com 3 casas decimais
print("Número fracionado com 3 casas depoois da vírgula: {:.3f}".format(num_frac))