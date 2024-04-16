import manipulaCSV as mcsv


def carregar() -> list: 
    '''
    Carrega o arquivo de Cliente.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Cliente.csv")
    return lista
    

def cadastrar( listaClientes : list ) -> bool:
    '''
    Rotina para cadastrar um cliente

    Parâmetros
    ----------
    listaClientes: Lista atual dos clientes

    Retorno
    -------
    Retorna True se o cliente foi cadastrado com sucesso
    '''
    camposCliente = ["CPF","Nome","Nascimento","Idade","Endereço","Cidade","Estado"]
    cliente = {}
    for i in camposCliente:
        cliente[i] = input(f"{i}:")
    listaClientes.append(cliente)
    print(listaClientes)
    return mcsv.gravarDados('Cliente.csv', camposCliente, listaClientes )

import csv

def alterar(cpf: str):
    flag = False 
    clientes = [] 
    
        
    with open('Cliente.csv', 'r', newline='') as arquivo_origem:
        clientes = list(csv.DictReader(arquivo_origem, delimiter=';'))

    with open('Cliente.csv', 'w', newline='') as arquivo_destino:
        nomes_colunas = ['CPF', 'Nome', 'Nascimento', 'Idade', 'Endereço', 'Cidade', 'Estado']
        escritor = csv.DictWriter(arquivo_destino, fieldnames=nomes_colunas, delimiter=';')
        escritor.writeheader()

        for cliente in clientes:
            if cliente['CPF'] == cpf:
                campo_alterar = int(input('Digite o número correspondente ao campo que deseja alterar:\n1 - CPF\n2 - Nome\n3 - Nascimento\n4 - Idade\n5 - Endereço\n6 - Cidade\n7 - Estado\n'))
                while campo_alterar < 1 or campo_alterar > 7:
                    print('Número inválido. Por favor, insira um número válido de 1 a 7.')
                    campo_alterar = int(input('Digite o número correspondente ao campo que deseja alterar:\n1 - CPF\n2 - Nome\n3 - Nascimento\n4 - Idade\n5 - Endereço\n6 - Cidade\n7 - Estado\n'))
                    
                novo_valor = input(f'Informe o novo valor para {nomes_colunas[campo_alterar - 1]}: ')
                cliente[nomes_colunas[campo_alterar - 1]] = novo_valor
                flag = True 

            escritor.writerow(cliente)
        
    if flag:
        print("Sucesso")    
    else:
        print("Erro")

def excluir(listaClientes : list, cpf : str ) -> bool:
    '''
    Excluir um cliente da lista de clientes e atualiza o arquivo CSV
    '''
    flag = False
    camposCliente = list(listaClientes[0].keys())
    for i,cliente in enumerate(listaClientes):
        if cliente['CPF'] ==  cpf :
            flag = True
            listaClientes.pop(i)
    #print(listaClientes)
    if flag:
        mcsv.gravarDados("Cliente.csv", camposCliente, listaClientes)
    return flag

def localizarLocacao():
    '''
    Função para localizar locações de um cliente
    item(7)
    '''

