import apresentacao
import datetime
import csv
import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaCarros as mcar

#################################################################

def novaLocacao():
    '''
    Função que cadastra uma nova locação de um carro
    item(4)
    '''
    cpf = input("Digite seu CPF que sera consultado na lista de clientes cadastrados: ")
    lista=mcsv.carregarDados("Cliente.csv")
    encontrou = True
    for llista in lista:
        if (cpf == llista["CPF"]):
            print("CPF encontrado")
            encontrou = False
            break
    if(encontrou):
            print("Cliente nao identificado. Retornado a tela anterior")
            return
    categoria = input("Categoria do carro desejado: ").lower()
    cambio = input("Cambio (Manual/Automatico): ").lower()
    seguro = input("Seguro (Sim/Nao): ").lower()

    lista= mcar.carregar()
    encontrou=True
    cDisp = []
    km=[]
    for i in lista:
        if(i["Cambio"].lower()==cambio and i["Categoria"].lower() == categoria):
            cDisp.append(int(i['Identificacao']))
            encontrou=False
            print(f"ID: {i['Identificacao']}\nModelo: {i['Modelo']}\nCor: {i['Cor']}\nDiaria: R${i['Diaria']}")
            if(seguro =="sim"):
                print(f"Seguro: R${i['Seguro']}")
            print(f"KM atual: {i['Km']}\nPlaca: {i['Placa']}")
            km.append([i['Identificacao'],i['Km']])
    if(encontrou):
        print("Não há carro disponível com essas características")
        return
    carroDesejado = int(input("Insira o ID do carro que deseja alugar: "))
    if not carroDesejado in cDisp:
        print("ID nao listado. retornando a tela anterior")
        return
    for i in km:
        if(int(i[0])==carroDesejado):
            kmI=i[1]
    campos=['ID locacao','ID carro','CPF cliente','Data inicial da locacao',
            'Data final da locacao','Km inicial','Km final','Seguro']
    data=input("Insira a data de locacao (formato exemplo: 11/04/2024 15:00): ")
    lista=[{"ID locacao":identificaID(),"ID carro": carroDesejado,"CPF cliente": cpf,
            "Data inicial da locacao": data,"Data final da locacao": '0/0/0 0h',"Km inicial": kmI,
            "Km final": 0,"Seguro": seguro}]
    mcsv.gravarDados("Locacao.csv",campos,lista)

#################################################################

def identificaID()-> int:
    try:
        arq = open('Locacao.csv', "r")
        listaClientes = csv.DictReader(arq, delimiter=';')
        listaClientes = list(listaClientes)
    except FileNotFoundError:
        print("Arquivo não encontrado Locacao")
        return 0
    j = 1
    for i in listaClientes:
        j=int(i['ID locacao'])
    return j

#################################################################
    
def encerraLocacao() -> bool:
    '''
    Função que encerra a locação de um carro
    '''
    #Número de identificação da locação
    identificacao_locacao = input("Identificação da locação: ")

    #Procurar data de início da locação e ID do carro em Locacoes.csv
    try:
        arq = open("Locacao.csv", "r")
        listaLocacao = csv.DictReader(arq, delimiter=";")
        for locacao in listaLocacao:
            if locacao['ID locacao'] == identificacao_locacao:
                identificacao_carro = locacao['ID carro']
                entrada = locacao['Data inicial da locacao']
        arq.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False

    #Procurar o valor da diária e a placa do carro no Carros.csv
    try:
        arq = open("Carro.csv", "r")
        listaCarros = csv.DictReader(arq, delimiter=";")
        for carro in listaCarros:
            if carro['Identificacao'] == identificacao_carro:
                valor_diaria = carro['Diaria']
                placa_carro = carro['Placa']
        arq.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False

    #Data de encerramento da locação
    data_saida = input("Data da devolução (dia/mes/ano): ")
    horario_saida = input("Horário de devolução (hh:mm): ")
    data_saida = data_saida + " " + horario_saida
    saida = datetime.datetime.strptime(data_saida, "%d/%m/%Y %H:%M")

    #Calculo da quantidade de tempo decorrido
    tempo_decorrido = saida - entrada
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
    if dias == 0:
        valor_pagar = valor_diaria
    else:
        valor_pagar = (dias * valor_diaria) + (horas/24 * valor_diaria)

    #Quilometragem do carro no momento da entrega
    quilometragem = float(input("Quilometragem do carro: "))

    #Atualizar dados em Locacoes.csv
    linhas = []
    try:
        with open('Locacao.csv', 'r', newline='') as arq_origem:
            linhas = list(csv.DictReader(arq_origem, delimiter=';'))
        with open('Locacao.csv', 'w', newline='') as arq_destino:
            nomes_colunas = ['ID locacao','ID carro','CPF cliente','Data inicial da locacao','Data final da locacao','Km inicial','Km final','Seguro']
            escritor = csv.DictWriter(arq_destino, fieldnames=nomes_colunas, delimiter=';')
            escritor.writeheader()
            for linha in linhas:
                if linha['ID locacao'] == identificacao_locacao:
                    campo_alterar_1 = 'Data final da locacao'
                    campo_alterar_2 = 'Km final'
                    linha[campo_alterar_1] = tempo_decorrido
                    linha[campo_alterar_2] = quilometragem
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return False
    
    #Atualizar dados em Carros.csv
    linhas = []
    try:
        with open('Carro.csv', 'r', newline='') as arquivo_origem:
            linhas = list(csv.DictReader(arquivo_origem, delimiter=';'))
        with open('Carro.csv', 'w', newline='') as arquivo_destino:
            nomes_colunas = ['Identificacao', 'Modelo', 'Cor', 'AnoFabricacao', 'Placa', 'Cambio', 'Categoria', 'Km', 'Diaria', 'Seguro', 'Disponivel']
            escritor = csv.DictWriter(arquivo_destino, fieldnames=nomes_colunas, delimiter=';')
            escritor.writeheader()
            for linha in linhas:
                if linha['Placa'] == placa_carro:
                    campo_alterar = 'Km'                    
                    linha[campo_alterar] = quilometragem
                escritor.writerow(linha)
    except FileNotFoundError:
        print('Arquivo não encontrado.')
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
    Retorna True se o arquivo Carros.csv foi aberto com sucesso e há carros disponiveis em tal categoria
    Retorna False se o arquivo Carros.csv não foi encontrado ou não carros disponiveis em tal categoria
    '''
    verifica = False
    try:
        arq = open("Carro.csv")
        listaCarros = csv.DictReader(arq, delimiter=";")
        for carro in listaCarros:
            if carro['Categoria'] == categoria_procurar:
                if carro['Disponivel'] == "Sim":
                    verifica = True
                    print("-"*50)
                    l = ["Identificacao","Modelo","Cor","AnoFabricacao","Placa","Cambio","Categoria","Km","Diaria","Seguro","Disponivel"]
                    for campo in l:
                        print(f"{campo}: {carro[campo]}")
                    print("-"*50)
        arq.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return verifica

#################################################################

def carrosLocados():
    '''
    Função que mostra quais carros estão locados
    item(10)
    '''
    data1=input("Digite a data e hora atual (formato: dd/mm/aaaa hh:mm): ")
    data1 = datetime.datetime.strptime(data1, "%d/%m/%Y %H:%M")
    listaCarros = mcar.carregar()
    listaClientes= mcli.carregar()
    listaLocacao = lista=mcsv.carregarDados("Locacao.csv")
    listaCarros1 = []
    listaLocacao1 = []
    listaClientes1 = []
    tempoDecorrido=[]
    for l1 in listaCarros:
        if(l1['Disponivel'].lower()=='nao'):
            listaCarros1.append([l1['Identificacao'],l1['Modelo'],l1['Placa'],l1['Categoria']])
    for i in listaCarros1:
        for l1 in listaLocacao:
            if(l1['ID carro']==i[0]):
                listaLocacao1.append([l1['CPF cliente'],l1['Data inicial da locacao']])
                data2 = datetime.datetime.strptime(l1['Data inicial da locacao'], "%d/%m/%Y %H:%M")
                temp=data1-data2
                if((data1-data2).seconds > 0):
                    dias = temp.days + 1
                else:
                    dias = temp.days
                tempoDecorrido.append([dias])
                break
    for i in listaLocacao1:
        for l1 in listaClientes:
            if(l1['CPF']==i[0]):
                listaClientes1.append([l1['Nome']])
    print(f"{listaLocacao1}\n{listaCarros1}\n{listaClientes1}\n{tempoDecorrido}")