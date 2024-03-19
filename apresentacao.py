from os import system, name

#################################################################
def limpaTela():
    '''
    Limpa a tela de acordo com o systema operacional
    '''
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

#################################################################        

def MenuPrincipal() -> str :
    '''
    Exemplo de Menu principal para o sistema
    
    Retorno    
    -------
    Retorna válida escolhida

    '''
    opcoes = [1,2,3,9]
    opcao = 10
    while opcao not in opcoes:
        limpaTela()
        print("#"*20)
        print("1.Locações\n2.Clientes\n3.Carros\n9.Sair")    
        print('#'*20)
        opcao = int(input("Opção -> "))            
    return opcao

#################################################################    

def CadastrarCliente() -> dict :
    '''
    Procedimento que mostra os campos para cadastramento de um cliente
    
    Retorno
    -------
    Retorna um dicionário com as informações de um cliente    
    '''
    print("#"*30)
    print("Cadastramento de um novo cliente ")
    l = ["CPF","Nome","Nascimento","Idade","Endereço","Cidade","Estado"]
    cliente = {}
    for campo in l:
        cliente[campo] = input(f"{campo}:")
        print("#"*30)
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
    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria", "Km", "Diaria", "Seguro", "Disponivel"]
    carro = {}
    for campo in l:
        carro[campo] = input(f"{campo}:")
        print("#"*30)
    return carro   
