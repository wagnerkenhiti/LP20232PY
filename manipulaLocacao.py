import apresentacao
import csv

def novaLocacao():
    '''
    Função que cadastra uma nova locação de um carro
    item(4)
    '''

def encerraLocacao():
    '''
    Função que encerra a locação de um carro
    item(5)
    '''

def carrosDisponiveis(categoria_procurar) -> bool:
    '''
    Função que mostra quais carros estão disponiveis para locação
    item(8)
    '''
    try:
        arq = open("Carros.csv")
        listaCarros = csv.DictReader(arq, delimiter=";")
        for carro in listaCarros:
            if carro['Categoria'] == categoria_procurar:
                if carro['Disponivel'] == "Sim":
                    print("-"*50)
                    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria","Km","Diaria","Seguro","Disponivel"]
                    for campo in l:
                        carro[campo] = print(f"{campo}: {carro[campo]}")
                    print("-"*50)
        arq.close()
        return True
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False

def carrosLocados():
    '''
    Função que mostra quais carros estão locados
    item(10)
    '''