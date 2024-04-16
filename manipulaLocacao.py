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
        if(i["Cambio"].lower()==cambio and i["Categoria"].lower() == categoria and i["Disponivel"].lower()=="sim"):
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
    lista={"ID locacao":identificaID(),"ID carro": carroDesejado,"CPF cliente": cpf,
            "Data inicial da locacao": data,"Data final da locacao": '0/0/0 0h',"Km inicial": kmI,
            "Km final": 0,"Seguro": seguro}
    lista1=mcsv.carregarDados("Locacao.csv")
    lista1.append(lista)
    mcsv.gravarDados("Locacao.csv",campos,lista1)
    with open('Carro.csv', 'r', newline='') as arquivo_origem:
            linhas = list(csv.DictReader(arquivo_origem, delimiter=';'))

    with open('Carro.csv', 'w', newline='') as arquivo_destino:
            nomes_colunas = ['Identificacao', 'Modelo', 'Cor', 'AnoFabricacao', 'Placa', 'Cambio', 'Categoria', 'Km', 'Diaria', 'Seguro', 'Disponivel']
            escritor = csv.DictWriter(arquivo_destino, fieldnames=nomes_colunas, delimiter=';')
            escritor.writeheader()
            for linha in linhas:
                if int(linha['Identificacao']) == carroDesejado:
                    linha['Disponivel'] = "nao"
                escritor.writerow(linha)
    arquivo_origem.close()
    arquivo_destino.close()

#################################################################

def identificaID()-> int:
    try:
        arq = open('Locacao.csv', "r")
        listaClientes = csv.DictReader(arq, delimiter=';')
        listaClientes = list(listaClientes)
    except FileNotFoundError:
        print("Arquivo não encontrado Locacao")
        return 0
    j = 0
    for i in listaClientes:
        j=int(i['ID locacao'])
    j+=1
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
                entrada = datetime.datetime.strptime(locacao['Data inicial da locacao'], "%d/%m/%Y %H:%M")
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

    data=input("Insira a data de encerramento da locacao (formato exemplo: 11/04/2024 15:00): ")
    saida = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
    tempo_decorrido = saida - entrada
    if tempo_decorrido.days > 0:
        [dummy, horas] =  str(tempo_decorrido).split(',')
        [horas, minutos, segundos] = horas.split(":")    
    else:
        [horas, minutos, segundos] = str(tempo_decorrido).split(":")

    hhoras=int(horas)/24
    vvalor_d=float(valor_diaria)
    add = 0
    seguro=''
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
                    if(linha['Seguro'].lower()=="sim"):
                        seguro = "sim"
                    campo_alterar_1 = 'Data final da locacao'
                    campo_alterar_2 = 'Km final'
                    linha[campo_alterar_1] = data
                    linha[campo_alterar_2] = quilometragem
                escritor.writerow(linha)
        arq_origem.close()
        arq_destino.close()
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
                    if(seguro=="sim"): 
                        add = float(linha["Seguro"])     
                    linha[campo_alterar] = quilometragem
                    linha['Disponivel'] = 'sim'
                escritor.writerow(linha)
        arquivo_origem.close()
        arquivo_destino.close()
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        return False

    valor_pagar = (tempo_decorrido.days * vvalor_d) + (hhoras * vvalor_d) + add
    print(f"""
          O carro locado tem uma diaria de {valor_diaria} e o tempo locado foi de:
          {tempo_decorrido.days} dias, {horas} horas e a taxa de seguro foi de R${add}
          O valor a pagar é de R${float(valor_pagar):.2f}.""")
    return True

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
            if carro['Categoria'].lower() == categoria_procurar.lower():
                if carro['Disponivel'].lower() == "Sim".lower():
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
    listaLocacao = mcsv.carregarDados("Locacao.csv")
    listaCarros1 = []
    listaLocacao1 = []
    listaClientes1 = []
    tempoDecorrido=[]
    add=[]
    for l1 in listaCarros:
        if(l1['Disponivel'].lower()=='nao'):
            listaCarros1.append([l1['Identificacao'],l1['Modelo'],l1['Placa'],l1['Categoria'],l1['Diaria'],l1['Seguro']])
    for i in listaCarros1:
        for l1 in listaLocacao:
            if(l1['ID carro']==i[0]):
                if(l1['Seguro'].lower()=='sim'):
                    add.append(float(i[5]))
                else:
                    add.append(0)
                listaLocacao1.append([l1['CPF cliente'],l1['Data inicial da locacao']])
                data2 = datetime.datetime.strptime(l1['Data inicial da locacao'], "%d/%m/%Y %H:%M")
                tempo_decorrido=data1-data2
                if tempo_decorrido.days > 0:
                    [dummy, horas] =  str(tempo_decorrido).split(',')
                    [horas, minutos, segundos] = horas.split(":")    
                else:
                    [horas, minutos, segundos] = str(tempo_decorrido).split(":")
                ddias=(int(horas) + tempo_decorrido.days*24)/24
                tempoDecorrido.append(ddias)
                break
    for i in listaLocacao1:
        for l1 in listaClientes:
            if(l1['CPF']==i[0]):
                listaClientes1.append(l1['Nome'])
    #print(f"!!!!!\n{listaLocacao1}: {len(listaLocacao1)}\n{listaClientes1}: {len(listaClientes1)}\n{listaCarros1}: {len(listaCarros1)}")
    for i in range(len(add)): 
    	print(f"""\tCARRO {i+1}:
           CPF: {listaLocacao1[i][0]}
           Nome do cliente: {listaClientes1[i]}
           Data inicial: {listaLocacao1[i][1]}
           Modelo do carro: {listaCarros1[i][1]}
           Categoria do carro: {listaCarros1[i][3]}
           Placa do carro: {listaCarros1[i][2]}
           Valor total a receber até o momento do relatório: R${(tempoDecorrido[i]*float(listaCarros1[i][4])+add[i]):.2f}""")
           