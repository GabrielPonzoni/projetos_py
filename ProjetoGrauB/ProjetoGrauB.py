def main():
    """
    Propósito: Main do projeto  
    """
    cabecalho()

    # end def

def cabecalho():
    """
    Purpose: Função que mostra o cabecalho
    """
    
    nome_empresa = "Six Pack Logistica " + chr(169)
    print('='*60)
    print(f'||{nome_empresa:^56}||')
    print('='*60)
# end def

if __name__ == "__main__":
    main()
# end main
