'''
v1.334543454 COMO VOU TRABALHAR COM OS PREÇOS DO PRODUTO!? 
'''
from time import sleep
import os

#variáveis globais
estoque_produto_1 = 20

comprador = []
quantidade_comprada = []
produtos_lista = []
preco_compra_lista = []
preco_compra_lista_bruto = []

def main():
	global comprador, quantidade_comprada, produtos_lista, preco_compra_lista, preco_compra_lista_bruto

	fechar_programa = False
	
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

def clear():
	clear = lambda: print('\n'*100)
	return clear()
# end def-clear

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
	global estoque_produto_1, valor_produto_1

	cabecalho()
	print('||                        MENU                            ||')
	print('-=-' * 20)
	print('||                   REGISTRAR VENDA                      ||')
	print('||                                                        ||')

	venda_realizada = False


	while not venda_realizada:
		nome_comprador = input('||Informe o nome do cliente: ')
		if nome_comprador == 'ADMIN':
			print(' -- COMANDO DE ADMIN DO SISTEMA! PRECIONE 0 PARA DEBUGAR --')
			comprador.extend(['Teste1','Teste2','Teste3','Teste4'])
			quantidade_comprada.extend([1,2,3,4])
			produtos_lista.extend(['Calça','Camisa','Bermuda','Saia'])
			preco_compra_lista.extend([112.00,190.00,149.7,676.00])
			preco_compra_lista_bruto.extend([112.00,95.00,49.00,169.00])

		while True:
			codigo_produto = input('||Informe o código do produto: ')
			if codigo_produto.isnumeric():
				codigo_produto = int(codigo_produto)
				break
			else:
				print('Informe um código válido')
		
		if codigo_produto > 0 and codigo_produto < 9:
			quantidade = int(input('||Quantidade desejada desse produto: '))
			quanti_prod = vendas(codigo_produto,quantidade) 
			quanti_estoque = estoque(codigo_produto,0)
			nome, valor = produto(codigo_produto)

			if quanti_prod == None:
				print('||>>> Não há estoque suficiente <<<')
			elif quantidade == 0:
				print('Não posso fazer uma venda de 0 produtos!')
			else:
				print('Venda realizada com sucesso!')
				print(f'Estoque do produto {nome} está com {quanti_estoque}')
				#armazenar compra:
				comprador.append(nome_comprador)
				quantidade_comprada.append(quantidade)
				produtos_lista.append(nome)
				#preços >aki<
				valor_compra = quantidade * valor
				preco_compra_lista.append(valor_compra)
				preco_compra_lista_bruto.append(valor)
		elif codigo_produto == 0:
			venda_realizada = True
			print('Fechando a conta.. ... ..')
		else:
			print('||>>> Codigo do produto inválido! <<<')
		
def produto(codigo_produto):
	if codigo_produto == 1:
		nome = 'Calça'
		valor = 112.00
	elif codigo_produto == 2:
		nome = 'Camisa'
		valor = 95.00
	elif codigo_produto == 3:
		nome = 'Bermuda'
		valor = 49.00
	elif codigo_produto == 4:
		nome = 'Saia'
		valor = 169.00
	elif codigo_produto == 5:
		nome = 'Blusa'
		valor = 120.00
	elif codigo_produto == 6:
		nome = 'Moletom'
		valor = 135.00
	elif codigo_produto == 7:
		nome = 'Meia'
		valor = 12.99
	elif codigo_produto == 8:
		nome = 'Tênis'
		valor = 183.00
	elif codigo_produto == 9:
		nome = 'Bota'
		valor = 219.90
	else:
		print('Codigo não encontrado para >nome< do produto!')
		return None, 0
	
	return nome,valor

		

def vendas(codigo_produto, quantidade): #1,10
	global estoque_produto_1

	if codigo_produto == 1:
		if estoque_produto_1 >= quantidade:
			estoque_produto_1 -= quantidade
			return estoque_produto_1
		else:
			return None
	else:
		print('Código de produto não encontrado! ')

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
	Purpose: Mostrar as compras realizadas
	"""
	cabecalho()
	print('-=-' * 20)
	print('||                Produtos Comprados                      ||')
	print('||                                                        ||')
	print('-=-' * 20)
	for i in range(len(produtos_lista)):
		print('||                                                        ||')
		print(f'||{i+1}ª compra foi de {quantidade_comprada[i]}x {produtos_lista[i]} sendo 1x valendo R$ {preco_compra_lista_bruto[i]:.2f}')
		print(f'||	O valor dessa compra deu: R$ {preco_compra_lista[i]:.2f}          ||')
	print('||                                                        ||')
	print('-=-' * 20)
	print('||                FIM DA LISTA DE PRODUTOS                ||')
	soma = sum(preco_compra_lista)
	print(f'||     Total da compra................: R${soma}          ||')
	print('||                                                        ||')
	print('-=-' * 20)
	print("Pressione Enter para continuar...")
	input()
	main()
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
