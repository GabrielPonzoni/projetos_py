def main():
    '''
    Propósito: Main do projeto  
    '''
    cabecalho()
    menu()

def menu():
    """
    Purpose: Abre o menu
    """
    menu_cabecalho = '|MENU|'
    texto_menu = 'Escolha uma das opções abaixo de 1 a 5, sendo que 2, 3 || \n||e 4 só funcionam quando a opção 1 foi preenchida.'
    print(f'||{menu_cabecalho:^31}||'.replace(' ', '-_'))
    print('||',' '*54,'||')
    print('||',f'{texto_menu}',' '*5,'||')
    print('||',' '*54,'||')
    print(f'||','-_'*27,'||')
    print('||',' '*54,'||')
    print('||','1 - Custo por Km rodado;',' '*29,'||')
    print('||','2 - Consultar trecho;',' '*32,'||')
    print('||','3 - Melhor rota;',' '*37,'||')
    print('||','4 - Rota completa;',' '*35,'||')
    print('||','5 - Sair;',' '*44,'||')
    print('||',' '*54,'||')
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

if __name__ == '__main__':
    main()
# end main
