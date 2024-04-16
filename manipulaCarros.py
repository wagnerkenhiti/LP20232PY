import csv
import manipulaCSV as mcsv
import manipulaLocacao as mloc
import apresentacao

#################################################################

def carregar() -> list:
    '''
    Carrega o arquivo de Carro.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos carros
    '''
    lista = mcsv.carregarDados("Carro.csv")
    return lista

#################################################################

def cadastrar(listaCarros : list) -> bool:
    '''
    Rotina para cadastrar um carro

    Parâmetros
    ----------
    listaClientes: lista atual dos carros

    Retorno
    -------
    Retorna True se o carro foi cadastrado com sucesso
    '''
    camposCliente =  ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria","Km","Diaria","Seguro","Disponivel"]
    cliente = apresentacao.CadastrarCarro()
    listaCarros.append(cliente)
    print(listaCarros)
    return mcsv.gravarDados('Carro.csv', camposCliente, listaCarros )

#################################################################

def alterar(placa : str) -> bool:
    '''
    Função para alterar dados de um carro

    Parâmetro
    ---------
    placa: placa do carro que se deseja alterar

    Retorno
    -------
    Retorna True caso foi alterado com sucesso
    '''
    carros = []
    try:
        with open('Carros.csv', 'r', newline='') as arquivo_origem:
            carros = csv.DictReader(arquivo_origem, delimiter=';')

        with open('Carros.csv', 'w', newline='') as arquivo_destino:
            nomes_colunas = ['Identificacao','Modelo','Cor','AnoFabricacao','Placa','Cambio','Categoria','Km','Diaria','Seguro','Disponivel']
            escritor = csv.DictWriter(arquivo_destino, fieldnames=nomes_colunas, delimiter=';')
            escritor.writeheader()

            for carro in carros:
                if carro['Placa'] == placa:
                    campo_alterar = int(input('Qual campo do carro você deseja alterar?\n1 - Identificacao\n2 - Modelo\n3 - Cor\n4 - AnoFabricacao\n5 - Placa\n6 - Cambio\n7 - Categoria\n8 - Km\n9 - Diaria\n10 - Seguro\n11 - Disponivel: '))
                    
                    while campo_alterar < 1 or campo_alterar > 11:
                        print('Número inválido. Por favor, insira um número válido de 1 a 11.')
                        campo_alterar = int(input('Qual campo do carro você deseja alterar?\n1 - Identificacao\n2 - Modelo\n3 - Cor\n4 - AnoFabricacao\n5 - Placa\n6 - Cambio\n7 - Categoria\n8 - Km\n9 - Diaria\n10 - Seguro\n11 - Disponivel: '))
                    
                novo_valor = input(f'Informe o novo valor para {nomes_colunas[campo_alterar - 1]}: ')
                carro[nomes_colunas[campo_alterar - 1]] = novo_valor
                escritor.writerow(carro)
        
        return True
    except FileNotFoundError:
        print('Arquivo não encontrado. Retornando False.')
        return False

#################################################################

def excluir(placa : str) -> bool:
    '''
    Excluir um carro da lista de carros e atualiza o arquivo CSV

    Parâmetros
    ----------
    placa: placa do carro que se deseja excluir

    Retorno
    -------
    Retorna True caso foi excluido com sucesso
    '''
    linhas = []
    try:
        with open('Carro.csv' , 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha['Placa'] != placa:
                    linhas.append(linha)
        with open('Carro.csv', 'w', newline='') as arquivo:
            nomes_colunas = ['Identificacao','Modelo','Cor','AnoFabricacao','Placa','Cambio','Categoria','Km','Diaria','Seguro','Disponivel']
            escritor = csv.DictWriter(arquivo, fieldnames=nomes_colunas)
            escritor.writeheader()
            escritor.writerows(linhas)
        return True
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        return False
    
#################################################################

def venda():
    lista = carregar()
    camposCliente =  ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria","Km","Diaria","Seguro","Disponivel"]
    for i in lista:
        if((2024-int(i['AnoFabricacao'])>=3 or int(i['Km'])>60000) and i["Disponivel"].lower()=="sim"):
            mcsv.gravarDados("vendas.csv",camposCliente,[i])
            