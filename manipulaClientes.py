import manipulaCSV as mcsv
import datetime
import manipulaCarros as mcar
import manipulaLocacao as mloc
import csv

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
    

def cadastrar(listaClientes : list) -> bool:
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
    return mcsv.gravarDados('Cliente.csv', camposCliente, listaClientes )

def alterar(cpf : str):
    '''
    Rotina para alterar dados de um cliente

    Parãmetro
    ---------
    cpf: CPF do cliente que se deseja alterar os dados
    '''
    flag = False 
    clientes = [] 
     
    with open('Cliente.csv', 'r', newline='') as arquivo_origem:
        clientes = list(csv.DictReader(arquivo_origem, delimiter=';'))

    with open('Cliente.csv', 'w', newline='') as arquivo_destino:
        nomes_colunas = ['CPF','Nome','Nascimento','Idade','Endereço','Cidade','Estado']
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


def excluir(listaClientes : list, cpf : str) -> bool:
    '''
    Excluir um cliente da lista de clientes e atualiza o arquivo CSV

    Parâmetros
    ----------
    listaClientes: 
    cpf: CPF do cliente que deseja excluir os dados

    Rteorno
    -------
    Retorna True caso foi excluido com sucesso
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

def localizarLocacao(identificacao: str)-> bool:
    '''
    identificacao: CPF ou nome do cliente
    Retorna verdadeiro se conseguiu concluir a localizacao
    Falso caso contrario
    '''
    listaCarros = mcar.carregar()
    listaLocacao = mcsv.carregarDados("Locacao.csv")
    listaCarros1 = []
    for l1 in listaCarros:
        listaCarros1.append([l1['Identificacao'],l1['Modelo'],l1['Placa'],l1['Categoria'],l1['Diaria'],l1['Seguro']])
    for i in listaCarros1:
        for l1 in listaLocacao:
            print(l1['CPF cliente'],identificacao)
            if(l1['ID carro']==i[0] and float(l1['Km final'])!=0 and l1['CPF cliente']==identificacao):
                data2 = datetime.datetime.strptime(l1['Data inicial da locacao'], "%d/%m/%Y %H:%M")
                data1 = datetime.datetime.strptime(l1['Data final da locacao'], "%d/%m/%Y %H:%M")
                tempo_decorrido=data1-data2
                if tempo_decorrido.days > 0:
                    [dummy, horas] =  str(tempo_decorrido).split(',')
                    [horas, minutos, segundos] = horas.split(":")    
                else:
                    [horas, minutos, segundos] = str(tempo_decorrido).split(":")
                seguro =0
                if (l1['Seguro'].lower()=='sim'):
                    seguro = float(i[5])
                ddias=(int(horas) + tempo_decorrido.days*24)/24
                print(f"""
           Placa do carro: {i[2]}
           Data inicial: {l1['Data inicial da locacao']}
           Data final: {l1['Data final da locacao']}
           Km percorrida: {float(l1['Km final'])-float(l1['Km inicial'])}
           Valor total a receber: R${(ddias*float(i[4]) + seguro):.2f}""")
                break
   