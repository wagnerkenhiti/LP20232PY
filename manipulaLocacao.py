import apresentacao
import csv
import datetime

#################################################################

def novaLocacao():
    '''
    Função que cadastra uma nova locação de um carro
    item(4)
    '''

#################################################################

def encerraLocacao() -> bool:
    '''
    Função que encerra a locação de um carro

    Retorno
    -------
    Retorna True se a locação foi encerrado corretamente
    '''
    #Número de identificação da locação
    identificacao = input("Identificação da locação: ")

    #Procurar o valor da diária do carro no Carros.csv
    try:
        arq = open("Carro.csv")
        listaCarros = csv.DictReader(arq, delimiter=";")
        for carro in listaCarros:
            if carro['Identificacao'] == identificacao:
                valor_diaria = carro['Diaria']
        arq.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False

    #Procurar data de início da locação em Locacoes.csv

    #Data de encerramento da locação
    saida = input("Data da devolução (dia/mes/ano): ")
    horario_saida = input("Horário de devolução (hh:mm): ")
    saida = saida + " " + horario_saida
    data_saida = datetime.datetime.strptime(saida)

    #Calculo da quantidade de tempo decorrido
    tempo_decorrido = data_saida - data_entrada
    print(tempo_decorrido)
    if tempo_decorrido.days > 0:
        [dummy, horas] =  str(tempo_decorrido).split(',')
        [horas, minutos, segundos] = horas.split(":")    
    else:
        [horas, minutos, segundos] = str(tempo_decorrido).split(":")

    #Exibindo horas e minutos utilizados, conferir se o calculo foi feito corretamente (tirar depois)
    dias = tempo_decorrido.days
    print(f"{dias} dias e {horas} horas utilizadas" )

    #Calculo do valor da locação
    valor_pagar = (dias * valor_diaria) + (horas/24 * valor_diaria)

    #Quilometragem do carro no momento da entrega
    quilometragem = float(input("Quilometragem do carro: "))

    #Atualizar dados em Locacoes.csv
    
    #Atualizar dados em Carros.csv
    try:
        arq = open("Carro.csv")
        listaCarros = csv.DictReader(arq, delimiter=";")
        for carro in listaCarros:
            if carro['Identificacao'] == identificacao:
                carro['Disponivel'] = "Sim"
                carro['Km'] = quilometragem
        arq.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False

#################################################################

def carrosDisponiveis(categoria_procurar) -> bool:
    '''
    Função que mostra quais carros de determinada categoria estão disponiveis para locação

    Parâmetros
    ----------
    categoria_procurar: string com o nome da categoria

    Retorno
    -------
    Retorna True se o arquivo Carros.csv foi aberto com sucesso
    Retorna False se o arquivo Carros.csv não foi encontrado
    '''
    try:
        arq = open("Carro.csv")
        listaCarros = csv.DictReader(arq, delimiter=";")
        for carro in listaCarros:
            if carro['Categoria'] == categoria_procurar:
                if carro['Disponivel'] == "Sim":
                    print("-"*50)
                    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria","Km","Diaria","Seguro","Disponivel"]
                    for campo in l:
                        print(f"{campo}: {carro[campo]}")
                    print("-"*50)
        arq.close()
        return True
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False

#################################################################

def carrosLocados():
    '''
    Função que mostra quais carros estão locados
    item(10)
    '''