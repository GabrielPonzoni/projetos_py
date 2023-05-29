import os  # biblioteca que possui comandos do sistema operacional
from time import sleep  # biblioteca que possui um sys PAUSE por tanto tempo

custo_km_rodado = 0
fechar_programa = False


def main():
    '''
    Propósito: Main do projeto  
    '''
    global custo_km_rodado
    limpa_tela()

    while not fechar_programa:
        # comment:  enquanto fechar_programa for false ele continurá rodando
        cabecalho()
        menu()
        opcoes_menu()
        #só realiza essa parte do código quando escolho 5 no menu
        sleep(1)

    # end while
# end def

def menu():
    """
    Purpose: Mostra as opções do menu
    """
    menu_cabecalho = '|MENU|'
    texto_menu = 'Escolha uma das opções abaixo de 1 a 5, sendo que 2, 3 || \n||e 4 só funcionam quando a opção 1 foi preenchida.'
    print(f'||{menu_cabecalho:^31}||'.replace(' ', '-_'))
    print('||', ' '*54, '||')
    print('||', f'{texto_menu}', ' '*5, '||')
    print('||', ' '*54, '||')
    print(f'||', '-_'*27, '||')
    print('||', ' '*54, '||')
    print('||', '1 - Custo por Km rodado;', ' '*29, '||')
    print('||', '2 - Consultar trecho;', ' '*32, '||')
    print('||', '3 - Melhor rota;', ' '*37, '||')
    print('||', '4 - Rota completa;', ' '*35, '||')
    print('||', '5 - Sair;', ' '*44, '||')
    print('||', ' '*54, '||')
    print('='*60)
# end def


def cabecalho_kmrodado():
    """
    Purpose: Mostra as opções do menu
    """
    titulo_cabecalho = '|Custo|'
    texto_cabecalho = ' Informe o valor a pagar por km rodado, esse valor deve ||\n|| ser em Reais e plausível;'
    print(f'||{titulo_cabecalho:^31}'.replace(' ', '-_'), end='-||')
    print('\n||', ' '*54, '||')
    print(f'||{texto_cabecalho}',' '*28, '||')
    print('||', ' '*54, '||')
    print(f'||', '-_'*27, '||')
    print('||', ' '*54, '||')
    print('='*60)
# end def


def cabecalho():
    '''
    Purpose: Função que mostra o cabecalho
    '''

    nome_empresa = 'Six Pack Logistica ' + chr(169)
    print('='*60)
    print(f'||{nome_empresa:^56}||')
    print('='*60)
# end def


def sair():
    global fechar_programa
    fechar_programa = True
    limpa_tela()
    print(">>> Saindo... :)")
    sleep(2)

# end def

def opcoes_menu():
    global custo_km_rodado #declaração da variável global dentro da função que a altera
    escolha = input("Seleciona a opção desejada: ")
    if escolha == "1":
       custo_km_rodado = add_cust_km(custo_km_rodado)
    elif escolha == "2":
        print('Opção 2')
    elif escolha == "3":
        print('Opção 3')
    elif escolha == "4":
        print('Opção 4')
    elif escolha == "5":
        sair()
    else:
        print('>>> Opção inválida! Tente novamente de 1 a 5 ...')
        sleep(2)
        main()
# end def


def add_cust_km(custo_km_rodado):
    limpa_tela()
    cabecalho()
    cabecalho_kmrodado()
    while True:
        try:
            custo_km_rodado = float(input("Digite o custo por Km rodado: "))
            if custo_km_rodado <= 0:
                # Se o valor inserido for negativo, levanta um ValueError para acionar o bloco except
                raise ValueError
            break  # Se o valor informado for um número, sai do loop
        except ValueError: 
            # Se o usuário digitar algo que não éum número, exibe uma mensagem de erro e continua o loop
            print(">>> Valor inválido! Digite um valor em reias positivo!")
    print(custo_km_rodado)
    sleep(2)
    
    return custo_km_rodado
    # end if


def limpa_tela():
    """
    Purpose: limpar tela
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # vai por cls se sistema operacional for IOS ou se for Windows usa clear


# end def

if __name__ == '__main__':
    main()
# end main
