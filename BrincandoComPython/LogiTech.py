def cabecalho():
  print('-=-' * 20)
  print('||          LogiTech Especialistas em lojistica!          ||')
  print('-=-' * 20)

def menu():
  print('||                        MENU                            ||')
  print('-=-' * 20)
  print('||Informe um número para acessar o item do menu, ou deixe || \n||o espaço em branco pressionando ENTER para sair.        ||')
  print('||                                                        ||')
  print('||() Registrar venda',' '* 37,'||')                                  
  print('||() Repor estoque')
  print('||() Mostrar estoque')
  print('||() Mostrar compras')
  print('||() Maior compra')
  print('||() Sair')
  print('-=-' * 20)

cabecalho()
menu()
resposta = int(input())
