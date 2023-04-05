
def main():
    
	cabecalho() #1ºprimeiro passo foi criar o cabecalho que irá ficar fixo no topo da tela
	menu() #2ºoutro passo importante é o menu 
	resposta = int(input()) #3ºrecebendo valores	
# end def-main

def cabecalho():
    
	print('-=-' * 20)
	print('||          LogiTech Especialistas em lojistica!||')
	print('-=-' * 20)


def menu():

    print('||                        MENU                            ||')
    print('-=-' * 20)
    print('||Informe um número para acessar o item do menu, ou deixe || \n||o espaço em branco pressionando ENTER para sair.        ||')
    print('||                                                        ||') 
    print('||() Registrar venda', ' ' * 37, '||')
    print('||() Repor estoque')
    print('||() Mostrar estoque')
    print('||() Mostrar compras')
    print('||() Maior compra')
    print('||() Sair')
    print('-=-' * 20)

if __name__ == "__main__": #1.1º criei a main
	main()
# end main
