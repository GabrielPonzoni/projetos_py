'''
v1.5 Terminar de configurar o banco de dados
'''
from time import sleep
import os

#variáveis globais
estoque_produto_1 = 20
estoque_produto_2 = 18
estoque_produto_3 = 23
estoque_produto_4 = 12
estoque_produto_5 = 9
estoque_produto_6 = 4
estoque_produto_7 = 17
estoque_produto_8 = 8
estoque_produto_9 = 3

calca = [1, 'Calça', 20, 112.00]
camisa = [2, "Camisa", 18, 95.00]
bermuda = [3, "Bermuda", 23, 49.90]
saia = [4, "Saia", 12, 169.00]
blusa = [5, "Blusa", 9, 120.00]
moletom = [6, "Moletom", 4, 135.00]
meia = [7, "Meia", 17, 12.99]
tenis = [8, "Tenis", 8, 183.00]
bota = [9, "Bota", 3, 219.90]

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
	global estoque_produto_1

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
		
		if codigo_produto > 0 and codigo_produto <= 9:
			
			while True:
				quantidade = input('||Quantidade desejada desse produto: ')
				if quantidade.isnumeric():
					quantidade = int(quantidade)
					if quantidade >= 0:
						break
				else:
					print('Informe um número inteiro positivo!')
			
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
	global estoque_produto_1, estoque_produto_2, estoque_produto_3, estoque_produto_4, estoque_produto_5, estoque_produto_6, estoque_produto_7, estoque_produto_8, estoque_produto_9

	if codigo_produto == 1:
		if estoque_produto_1 >= quantidade:
			estoque_produto_1 -= quantidade
			return estoque_produto_1
		else:
			return None
	elif codigo_produto == 2:
		if estoque_produto_2 >= quantidade:
			estoque_produto_2 -= quantidade
			return estoque_produto_2
		else:
			return None
	elif codigo_produto == 3:
		if estoque_produto_3 >= quantidade:
			estoque_produto_3 -= quantidade
			return estoque_produto_3
		else:
			return None
	elif codigo_produto == 4:
		if estoque_produto_4 >= quantidade:
			estoque_produto_4 -= quantidade
			return estoque_produto_4
		else:
			return None
	elif codigo_produto == 5:
		if estoque_produto_5 >= quantidade:
			estoque_produto_5 -= quantidade
			return estoque_produto_5
		else:
			return None
	elif codigo_produto == 6:
		if estoque_produto_6 >= quantidade:
			estoque_produto_6 -= quantidade
			return estoque_produto_6
		else:
			return None
	elif codigo_produto == 7:
		if estoque_produto_7 >= quantidade:
			estoque_produto_7 -= quantidade
			return estoque_produto_7
		else:
			return None
	elif codigo_produto == 8:
		if estoque_produto_8 >= quantidade:
			estoque_produto_8 -= quantidade
			return estoque_produto_8
	elif codigo_produto == 9:
		if estoque_produto_9 >= quantidade:
			estoque_produto_9 -= quantidade
			return estoque_produto_9
	else:
		print('Código de produto não encontrado! ')

def estoque(codigo_produto, quantidade):
	global estoque_produto_1, estoque_produto_2, estoque_produto_3, estoque_produto_4, estoque_produto_5, estoque_produto_6, estoque_produto_7, estoque_produto_8, estoque_produto_9

	if codigo_produto == 1:
		estoque_produto_1 += quantidade
		return estoque_produto_1
	elif codigo_produto == 2:
		estoque_produto_2 += quantidade
		return estoque_produto_2
	elif codigo_produto == 3:
		estoque_produto_3 += quantidade
		return estoque_produto_3
	elif codigo_produto == 4:
		estoque_produto_4 += quantidade
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
	Purpose: Mostrar o estoque dos produtos
	"""
	cabecalho()
	mostrarEstoque = input("Deseja ver o estoque? [s/n]")
  
	if mostrarEstoque == "n":
		return menu()
	elif mostrarEstoque == "s":
		print("Código do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(calca [0],calca [1],calca [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(camisa [0],camisa [1],camisa [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(bermuda [0],bermuda [1],bermuda [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(saia [0],saia [1],saia [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(blusa [0],blusa [1],blusa [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(moletom [0],moletom [1],moletom [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(meia [0],meia [1],meia [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(tenis [0],tenis [1],tenis [2]))
		print("\nCódigo do produto: {}\nItem: {}\nQuantidade no estoque: {}".format(bota [0],bota [1],bota [2]))
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
		print(f'||{i+1}ª compra foi de {quantidade_comprada[i]}x {produtos_lista[i]} sendo 1x valendo R$ {preco_compra_lista_bruto[i]:.2f}    ||')
		print(f'||	O valor dessa compra deu: R$ {preco_compra_lista[i]:.2f}               ||')
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
