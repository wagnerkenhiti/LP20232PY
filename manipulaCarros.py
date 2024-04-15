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
    listaClientes: Lista atual dos carros

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

def alterar( placa : str) -> bool:
    linhas = []
    try:
        with open('carros.csv', 'r', newline='') as arquivo_origem:
            linhas = list(csv.DictReader(arquivo_origem, delimiter=';'))

        with open('carros.csv', 'w', newline='') as arquivo_destino:
            nomes_colunas = ['Identificacao', 'Modelo', 'Cor', 'AnoFabricacao', 'Placa', 'Cambio', 'Categoria', 'Km', 'Diaria', 'Seguro', 'Disponivel']
            escritor = csv.DictWriter(arquivo_destino, fieldnames=nomes_colunas, delimiter=';')
            escritor.writeheader()

            for linha in linhas:
                if linha['Placa'] == placa:
                    campo_alterar = input('Qual campo do carro você deseja alterar? (Identificacao;Modelo;Cor;AnoFabricacao;Placa;Cambio;Categoria;Km;Diaria;Seguro;Disponivel): ')
                    
                    # Verificando se o campo inserido é válido
                    while campo_alterar not in nomes_colunas:
                        print('Campo inválido. Por favor, insira um campo válido.')
                        campo_alterar = input('Qual campo do carro você deseja alterar? (Identificacao;Modelo;Cor;AnoFabricacao;Placa;Cambio;Categoria;Km;Diaria;Seguro;Disponivel): ')
                    
                    novo_valor = input(f'Informe o novo valor para {campo_alterar}: ')
                    linha[campo_alterar] = novo_valor

                escritor.writerow(linha)
        
        return True
    except FileNotFoundError:
        print('Arquivo não encontrado. Retornando False.')
        return False

#################################################################

def excluir(placa : str) -> bool:
    linhas = []
    try:
        with open('Carro.csv' , 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if linha['Placa'] != placa:
                    linhas.append(linha)
        with open('Carro.csv', 'w', newline='') as arquivo:
            nomes_colunas = ['Identificacao', 'Modelo', 'Cor', 'AnoFabricacao', 'Placa', 'Cambio', 'Categoria', 'Km', 'Diaria', 'Seguro', 'Disponivel']
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
        if(2024-int(i['AnoFabricacao'])>=3 or int(i['Km'])>60000):
            mcsv.gravarDados("vendas.csv",camposCliente,[i])