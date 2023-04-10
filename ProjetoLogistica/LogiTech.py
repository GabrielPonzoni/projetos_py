'''
v1.7 código bruto finalizado
'''
from time import sleep #biblioteca que possui um sys PAUSE por tanto tempo

#variáveis globais, foi preciso inicializar elas em algum lugar, com valores iniciais. 
estoque_produto_1 = 20
estoque_produto_2 = 18
estoque_produto_3 = 23
estoque_produto_4 = 12
estoque_produto_5 = 9
estoque_produto_6 = 4
estoque_produto_7 = 17
estoque_produto_8 = 8
estoque_produto_9 = 3

#declaração de vetores que foram utilizados para fazer o registro de vendas, cada vetor foi chamado a cada venda.
comprador = [] #vetor que determina a lista de compradores 
quantidade_comprada = [] #vetor que armazena a quantidade de itens comprados 
produtos_lista = [] #vetor que armazena o nome do produto comprado
preco_compra_lista = [] #vetor que armazena o valor total do produto 
preco_compra_lista_bruto = [] #vetor que armazena o valor individual do produto 

#função main, dorso do código
def main():
	'''
	Propósito: Temos um meno no qual o usuário pode escolher entre 6 opções: 1 - registrar venda, 2 - 
	repor estoque, 3 - mostrar estoque, 4 - mostrar compras, 5 - maior compra. O código não pode ser 
	finalizado após cada escolha. Deve abrir algo que de continuidade para o processo.
	'''
	fechar_programa = False
	
	while not fechar_programa: #enquanto a var fechar_programa n for True ele não para de rodar o código
		sleep(2)  #função do timer para pausar a leitura do programa em 2 segundos
		clear() #função creada para fazer uma pseudo limpeza do código
		cabecalho()  #cabecalho que irá ficar fixo no topo da tela
		menu()  # puxa um molde do menu

		# input para receber escolha de usuário a respeito de função
		resposta = int(input('Informe um índice do menu para ação desejada: '))
		if resposta == 1:
			clear() #limpa tela
			registrar_venda() #executa função registrar venda casp o input for 1
		elif resposta == 2:
			clear()
			repor_estoque()
		elif resposta == 3:
			clear()
			mostrar_estoque()
		elif resposta == 4:
			clear()
			mostrar_compras()
		elif resposta == 5:
			clear()
			maior_compra()
		elif resposta == 0:
			print('Saindo do menu ..... .. .....')
			sleep(2)
			fechar_programa = True
		else: #se n se enquadrar em nenhum desses valores o programa pede para informar novamente.
			print('Valor informado inválido, tente novamente!') 
			continue 
# end def-main

def clear():
	''' Propósito: código para pseudo limpar a tela. '''
	clear = print('\n'*100) 
	return clear
# end def-clear

def cabecalho():
	'''
	Propósito: é chamado quando queremos puxar a mensagem fixa de cabecalho da empresa
	'''
	print('-=-' * 20)
	print('||          LogiTech Especialistas em lojistica!          ||')
	print('-=-' * 20)
#end def

def menu():
	'''
	Propósito: é chamdo quando queremos puxar a mensagem fixa do menu
	'''
	print('||                        MENU                            ||')
	print('-=-' * 20)
	print('||Informe um número para acessar o item do menu, ou deixe || \n||o espaço em branco pressionando ENTER para sair.        ||')
	print('||                                                        ||')
	print('||(1) Registrar venda', ' ' * 35, '||')
	print('||(2) Repor estoque', ' ' * 37, '||')
	print('||(3) Mostrar estoque', ' ' * 35, '||')
	print('||(4) Mostrar compras', ' ' * 35, '||')
	print('||(5) Maior compra', ' ' * 38, '||')
	print('||(0) Sair', ' ' * 46, '||')
	print('-=-' * 20)
#end def

# funções do item de resposta 1 ao 5


def registrar_venda():
	'''
	Função: criar venda (venda_realizada), coleta o nome_cliente depois pede o código_produto e a quantidade 
	desejada, caso não preenche os requisitos nao registra e começa de novo o registro.
	'''

	cabecalho()
	print('||                        MENU                            ||')
	print('-=-' * 20)
	print('||                   REGISTRAR VENDA                      ||')
	print('||                                                        ||')

	venda_realizada = False


	while not venda_realizada: #enquanto não sair de todos os laços e chegar na ultima linha o bool n muda
		nome_comprador = input('||Informe o nome do cliente: ')
		
		#código criado para debugar outras funções, achei interessante deixar escondido
		# if nome_comprador == 'ADMIN':
		# 	print(' -- COMANDO DE ADMIN DO SISTEMA! PRECIONE 0 PARA DEBUGAR --')
		# 	comprador.extend(['Teste1','Teste2','Teste3','Teste4'])
		# 	quantidade_comprada.extend([1,2,3,4])
		# 	produtos_lista.extend(['Calça','Camisa','Bermuda','Saia'])
		# 	preco_compra_lista.extend([112.00,190.00,149.7,676.00])
		# 	preco_compra_lista_bruto.extend([112.00,95.00,49.00,169.00])

		#condição para ver se código do produto está sendo informado corretamente
		while True: #repete até que vire false e saia do laço 
			codigo_produto = input('||Informe o código do produto: ')
			if codigo_produto.isnumeric(): #confere se valores informados são números
				codigo_produto = int(codigo_produto)
				break
			else:
				print('Informe um código válido')

		#confere se o número esta dentro das 9 possíveis opções 
		if codigo_produto > 0 and codigo_produto <= 9:
			
			#verificando se a quantidade é valor do tipo inteiro 
			while True: 
				quantidade = input('||Quantidade desejada desse produto: ')
				if quantidade.isnumeric():
					quantidade = int(quantidade)
					if quantidade >= 0:
						break
				else:
					print('Informe um número inteiro positivo!')
			
			quanti_prod = vendas(codigo_produto,quantidade) #puxa função que realiza o decréscimo de um estoque vendas
			quanti_estoque = estoque(codigo_produto,0) # puxa função que realida o acréscimo de um estoque de produtos adicionados
			nome, valor = produto(codigo_produto) #banco de dados que possui o nome e o valor do produto a partir do código do mesmo

			#verificando as condições retornadas do vendas() no sentido de ser possível ou não realizar a venda
			if quanti_prod == None:
				print('||>>> Não há estoque suficiente <<<')
			elif quantidade == 0: #se faziamos uma venda de 0 produtos ele acabava criando um registro de uma venda de 0 produtos
				print('Não posso fazer uma venda de 0 produtos!')
			#caso estivesse tudo ok, a venda era realizada com sucesso!
			else:
				print('Venda realizada com sucesso!')
				print(f'Estoque do produto {nome} está com {quanti_estoque}') #estoque atualizado da compra
				#armazenar compra:
				comprador.append(nome_comprador)
				quantidade_comprada.append(quantidade)
				produtos_lista.append(nome)
				#tratamento de valores do produto:
				valor_compra = quantidade * valor
				preco_compra_lista.append(valor_compra)
				preco_compra_lista_bruto.append(valor)
		
		#caso o código fosse 0 volta para o menu 
		elif codigo_produto == 0:
			venda_realizada = True #quebra o laço do while venda_realizada
			print('Fechando a conta.. ... ..') 
		else:
			print('||>>> Codigo do produto inválido! <<<') # se informar 10 ou maior o if fecha aki 
		
def produto(codigo_produto):
	'''
	Propósito: Banco de dados que retorna nome e valor de cada produto. 
	'''
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
		return None, 0 #0 porque valor é nemérico e não aceita retornar None
	
	return nome,valor

		

def vendas(codigo_produto, quantidade): #1,10
	'''
	Propósito: Atualiza as variáveis globais que foram iniciadas no início do programa, 
	realiza o decréscimo das mesmas de acrodo com o código e a quantidade informada.
	'''
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
	'''
	Propósito: Atualiza as variáveis globais que foram iniciadas no início do programa, 
	realiza o acréscimo das mesmas de acrodo com o código e a quantidade informada.
	'''
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
		return estoque_produto_4
	elif codigo_produto == 5:
		estoque_produto_5 += quantidade
		return estoque_produto_5
	elif codigo_produto == 6:
		estoque_produto_6 += quantidade
		return estoque_produto_6
	elif codigo_produto == 7:
		estoque_produto_7 += quantidade
		return estoque_produto_7
	elif codigo_produto == 8:
		estoque_produto_8 += quantidade
		return estoque_produto_8
	elif codigo_produto == 9:
		estoque_produto_9 += quantidade
		return estoque_produto_9
	else:
		print('Produto não encontrado')

def repor_estoque():
    """
    Purpose: ao contrário do vendas essa função incrementa no estoque e não salva no nome do usuário
    que realizou a ação. 
    """ 
    cabecalho()  
    estoque_realizado = False
    while not estoque_realizado:
        while True:
            codigo_produto = input('||Informe o código do produto: ')
            if codigo_produto.isnumeric():
                codigo_produto = int(codigo_produto)
                if codigo_produto >= 0:
                    break  
            else:
                print('Informe um código válido')

		#realizamos mesma série de verificação que foi feita no vendas        
        if codigo_produto > 0 and codigo_produto <= 9:
            estoque_nome = produto(codigo_produto)
            estoque_quant = vendas(codigo_produto, 0)
            print(f'Estoque atual de {estoque_nome[0]}: {estoque_quant}') #ele extrai o print de apenas o nome no vetor 
            while True:
                quantidade = input('||Quantidade para colocar no estoque: ')
                if quantidade.isnumeric():
                    quantidade = int(quantidade)
                    if quantidade >= 0:
                        break
                    else:
                        print('Informe um número inteiro positivo!')
                else:
                    print('Informe um número inteiro positivo!')
            
            novo_estoque_quant = estoque(codigo_produto, quantidade) #quantidade atualizada do estoque
            print(f'Agora {estoque_nome[0]} tem um estoque de {novo_estoque_quant}')
            while True:
                resposta = input('Deseja colocar mais estoque? S/N ') #escolha do usuário para continuar registrando masi produtos
                if resposta.upper() == 'S':
                    print('Vamos registrar mais um produto')
                    break
                elif resposta.upper() == 'N':
                    estoque_realizado = True
                    break
                else:
                    print('Não entendi...')
                    continue
# end def

def mostrar_estoque():
	"""
	Purpose: Mostrar o estoque dos produtos 
	"""
	cabecalho()
	print('||                         ESTOQUE                        ||')
	print('||                                                        ||')
	print('-=-' * 20)

	#vetores para administrar os estoques de acordo com código
	calca = [1, 'Calça', estoque_produto_1, 112.00, estoque_produto_1 * 112.00]
	camisa = [2, "Camisa", estoque_produto_2, 95.00, estoque_produto_2 * 95.00]
	bermuda = [3, "Bermuda", estoque_produto_3, 49.90, estoque_produto_3 * 49.90]
	saia = [4, "Saia", estoque_produto_4, 169.00, estoque_produto_4 * 169.00]
	blusa = [5, "Blusa", estoque_produto_5, 120.00, estoque_produto_5 * 120.00]
	moletom = [6, "Moletom", estoque_produto_6, 135.00, estoque_produto_6 * 135.00]
	meia = [7, "Meia", estoque_produto_7, 12.99, estoque_produto_7 * 12.99]
	tenis = [8, "Tenis", estoque_produto_8, 183.00, estoque_produto_8 * 183.00]
	bota = [9, "Bota", estoque_produto_9, 219.90, estoque_produto_9 * 219.90]
	
	print("||Deseja ver o estoque? [s/n]                             ||")
	mostrarEstoque = input('||')
	if mostrarEstoque == "n":
		return main()
	elif mostrarEstoque == "s":
		print("||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(calca [0],calca [1],calca [2], calca [3], calca[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(camisa [0],camisa [1],camisa [2], camisa[3], camisa[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(bermuda [0],bermuda [1],bermuda [2], bermuda[3], bermuda[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(saia [0],saia [1],saia [2],saia [3],saia [4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(blusa [0],blusa [1],blusa [2], blusa [3], blusa[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(moletom [0],moletom [1],moletom [2], moletom[3], moletom[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(meia [0],meia [1],meia [2], meia[3], meia[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(tenis [0],tenis [1],tenis [2], tenis[3], tenis[4]))
		print('-=-' * 20)
		print("||\n||Código do produto: {}\n||Item: {}\n||Quantidade no estoque: {}\n||Valor unitário: {}\n||Valor total: {}".format(bota [0],bota [1],bota [2], bota [3], bota[4]))
		print('-=-' * 20)
		print('||Pressione ENTER para voltar ao menu!')
		input()
		main()
# end def

def mostrar_compras():
	"""
	Propósito: Mostrar as compras realizadas
	"""
	cabecalho()
	print('-=-' * 20)
	print('||                Produtos Comprados                      ||')
	print('||                                                        ||')
	print('-=-' * 20)
	for i in range(len(produtos_lista)): #o for executa até chegar no final do vetor
		print('||                                                        ||')
		#quantidade comprada() - gerado quando o usuário comprou x itens, produtos_lista imprime de acordo com a ordem de item 
		print(f'||{i+1}ª compra foi de {quantidade_comprada[i]}x {produtos_lista[i]} sendo 1x valendo R$ {preco_compra_lista_bruto[i]:.2f}    ||')
		print(f'||	O valor dessa compra deu: R$ {preco_compra_lista[i]:.2f}               ||') #valor gerado pela mutliplicação de quantidade por preço bruto 
	print('||                                                        ||')
	print('-=-' * 20)
	print('||                FIM DA LISTA DE PRODUTOS                ||')
	soma = sum(preco_compra_lista) #função para somar todos valores 
	print(f'||     Total da compra................: R${soma}          ||')
	print('||                                                        ||')
	print('-=-' * 20)
	print("Pressione Enter para continuar...")
	input()
	main()
# end def

def maior_compra():
	'''
	Propósito: Encontrar a maior compra realizada por um usuário, usando o índice de valor maior com o pressuposto 
	índice do usuário
	'''
	global comprador, preco_compra_lista

	cabecalho()
	print('||                        MENU                            ||')
	print('-=-' * 20)
	print('||                   MAIOR COMPRA                        ||')
	print('||                                                        ||')

	if not comprador:
		print('Nenhuma compra registrada ainda.')
		return

	maior_valor = max(preco_compra_lista)  # Encontra o maior valor na lista de preços
	index_maior_valor = preco_compra_lista.index(maior_valor)  # Encontra o índice do maior valor
	nome_comprador = comprador[index_maior_valor]  # Obtém o nome do comprador correspondente ao maior valor
	valor_compra = preco_compra_lista_bruto[index_maior_valor]  # Obtém o valor bruto da compra correspondente ao maior valor

	print(f'O maior valor de compra foi de {nome_comprador}, com o valor de R${maior_valor:.2f}.')
	print(f'Valor bruto da compra: R${valor_compra:.2f}.')
# end def

#fim das funções do menu

if __name__ == "__main__": #código para gerar a main no programa principal.
	main()
# end main
