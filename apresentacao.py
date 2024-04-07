from os import system, name

#################################################################

def limpaTela():
    '''
    Limpa a tela de acordo com o sistema operacional
    '''
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

#################################################################        

def MenuPrincipal() -> int :
    '''
    Menu principal

    Retorno
    -------
    Retorna a opção escolhida pelo usuário
    '''
    opcoes= [1, 2, 3, 9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*50)
        print("1. Locação")
        print("2. Cliente")
        print("3. Carro")
        print("9. Sair")
        print("-"*50)
        opcao = int(input("Opcao ->"))
        print("#"*50)
    return opcao

#################################################################

def MenuLocacao() -> int:
    '''
    Menu para locações de carros

    Retorno
    -------
    Retorna opção escolhida pelo usuário
    '''
    opcoes = [1, 2, 3, 9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*50)
        print("1. Cadastrar uma nova locação")
        print("2. Encerrar uma locação")
        print("3. Carros disponíveis para locação")
        print("4. Relatório de carros locados")
        print("9. Sair")
        print("-"*50)
        opcao = int(input("Opcao -> "))
        print("#"*50)
    return opcao

#################################################################

def MenuCliente() -> int:
    '''
    Menu para cliente

    Retorno
    -------
    Retorna a opção escolhida pelo usuário
    '''
    opcoes = [1, 2, 3, 4, 9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*50)
        print("1. Cadastar novo cliente")
        print("2. Atualizar dados de cliente")
        print("3. Excluir dados de cliente")
        print("4. Localizar locações de um cliente")
        print("9. Sair")
        print("-"*50)
        opcao = int(input("Opcao -> "))
        print("#"*50)
    return opcao

#################################################################

def MenuCarro() -> int:
    '''
    Menu para carro

    Retorno
    -------
    Retorna a opção escolhida pelo usuário
    '''
    opcoes = [1, 2, 3, 4, 9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*50)
        print("1. Cadastrar novo carro")
        print("2. Atualizar dados de um carro")
        print("3. Excluir dados de um carro")
        print("4. Carros de carros a venda")
        print("9. Sair")
        print("-"*50)
        opcao = print(input("Opcao -> "))
        print("#"*50)
    return opcao

#################################################################  

def CadastrarCliente() -> dict :
    '''
    Procedimento que mostra os campos para cadastramento de um cliente
    
    Retorno
    -------
    Retorna um dicionário com as informações de um cliente    
    '''
    print("#"*50)
    print("Cadastramento de um novo cliente ")
    l = ["CPF","Nome","Nascimento","Idade","Endereço","Cidade","Estado"]
    cliente = {}
    for campo in l:
        cliente[campo] = input(f"{campo}:")
        print("#"*50)
    return cliente

#################################################################    

def CadastrarCarro() -> dict:
    '''
    Procedimento que mostra os campos para cadastramento de um carro
    
    Retorno
    -------
    Retorna um dicionário com as informações de um carro    
    '''
    print("#"*30)
    print("Cadastramento de um novo carro ")
    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria","Km","Diaria","Seguro","Disponivel"]
    carro = {}
    for campo in l:
        carro[campo] = input(f"{campo}:")
        print("#"*30)
    return carro   