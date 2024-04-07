import manipulaCSV as mcsv
import apresentacao

#################################################################

def carregar() -> list:
    '''
    Carrega o arquivo de Carro.csv numa lista
    
    Retorno
    -------
    Retorna uma lista vazia caso o arquivo não exista ou 
    uma lista de dicionários contendo os dados dos clientes
    '''
    lista = mcsv.carregarDados("Carro.csv")
    return lista

#################################################################

def cadastrar( listaCarros : list ) -> bool:
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
    return mcsv.gravarDados('Carro.csv', camposCliente, listaCarros)

#################################################################

def alterar():
    '''
    Função para alterar dados de um carro
    item(2)
    '''

#################################################################

def excluir():
    '''
    Função para excluir dados de um carro
    item(2)
    '''

#################################################################

def venda():
    '''
    Função para listar carros a venda
    item(9)
    '''