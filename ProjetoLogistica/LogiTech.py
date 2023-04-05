
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
    print('||(1) Registrar venda', ' ' * 35, '||')
    print('||(2) Repor estoque')
    print('||(3) Mostrar estoque')
    print('||(4) Mostrar compras')
    print('||(5) Maior compra')
    print('||(0) Sair')
    print('-=-' * 20)

#funções do 1 ao 5
def registrar_venda():
    """
    Purpose: 
    """ 
# end def

def repor_estoque():
    """
    Purpose: 
    """   
# end def

def mostrar_estoque():
    """
    Purpose: 
    """
# end def

def mostrar_compras():
    """
    Purpose: 
    """
# end def

def maior_compra():
    """
    Purpose: 
    """
# end def

def sair():
    """
    Purpose: 
    """
# end def

#fim das funções do menu

if __name__ == "__main__": #1.1º criei a main
	main()
# end main
