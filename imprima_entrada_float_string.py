#9. Solicite ao usuário que ele informe um caractere representando uma moeda e em seguida 
#solicite um número fracionário representando um valor. Mostre na tela a moeda + $ + valor com 
#2 casas decimais

#valor da moeda informada
moeda = input("Usuário, informe um caractere representando uma moeda...\n")

#valor do valor_moeda informada
valor = float(input("Usuário, qual o número fraconário que representa o valor da moeda: "))
print("Moeda final: {}${:.2f}".format(moeda,valor))