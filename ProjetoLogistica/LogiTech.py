from time import sleep
import os

#variáveis globais
estoque_produto_1 = 20
venda_produto_1 = 0

def main():
	fechar_programa = False
	clear = lambda: print('\n'*100)
	
	while not fechar_programa:
		sleep(2)
		clear()
		cabecalho()  # 1ºprimeiro passo foi criar o cabecalho que irá ficar fixo no topo da tela
		menu()  # 2ºoutro passo importante é o menu
		# 3ºrecebendo valores
		resposta = int(input('Informe um índice do menu para ação desejada: '))
		if resposta == 1:
			registrar_venda()
		elif resposta == 2:
			repor_estoque()
		elif resposta == 3:
			mostrar_estoque()
		elif resposta == 4:
			mostrar_compras()
		elif resposta == 5:
			maior_compra()
		elif resposta == 0:
			return True
		else:
			print('Valor informado inválido, tente novamente!')
			continue 
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

# funções do 1 ao 5


def registrar_venda():
	'''
	Função: criar venda (venda_realizada), coleta o nome_cliente depois pede o código_produto e a quantidade desejada,
	if false nao registra e imprime uma mensagem 
	'''
	global estoque_produto_1
	cabecalho()
	print('||                        MENU                            ||')
	print('-=-' * 20)
	print('||                   REGISTRAR VENDA                      ||')
	print('||                                                        ||')
	quantidade_validada = False
	produto_validado = False
	venda_realizada = False

	while not produto_validado and not quantidade_validada:

		nome_comprador = input('||Informe o nome do cliente: ')
		codigo_produto = int(input('||Informe o código do produto: '))
		quantidade = int(input('||Quantidade desejada desse produto: '))
		quanti_prod = vendas(codigo_produto,quantidade) 
		print(quanti_prod)

		quantidade = int(input('QUantidade pra por no estoque: '))
		quanti_prod = estoque(codigo_produto,quantidade)
		print(quanti_prod)

		# if total_produto >= 0:
		# 	produto_validado = True
		# 	quantidade_validada = True
		# else:
		# 	continue
		

def vendas(codigo_produto, quantidade): #1,10
	global estoque_produto_1, venda_produto_1

	if codigo_produto == 1:
		if estoque_produto_1 >= quantidade:
			estoque_produto_1 -= quantidade
			venda_produto_1 += quantidade
			return estoque_produto_1
		else:
			print('Não há estoque suficiente')

def estoque(codigo_produto, quantidade):
	global estoque_produto_1

	if codigo_produto == 1:
		estoque_produto_1 += quantidade
		return estoque_produto_1
	else:
		print('Produto não encontrado')


def repor_estoque():
	"""
	Purpose: 
	""" 
	cabecalho()  
	print('Repor estoque...')
# end def

def mostrar_estoque():
	"""
	Purpose: 
	"""
	cabecalho()
	print('mostrar estoque')
# end def

def mostrar_compras():
	"""
	Purpose: 
	"""
	cabecalho()
# end def

def maior_compra():
	"""
	Purpose: 
	"""
	cabecalho()
# end def

def sair():
	"""
	Purpose: 
	"""
	cabecalho()
# end def

#fim das funções do menu

if __name__ == "__main__": #1.1º criei a main
	main()
# end main
