import apresentacao
import datetime
import csv
import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaCarros as mcar


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


def identificaID()-> int:
    try:
        arq = open('Locacao.csv', "r")
        listaClientes = csv.DictReader(arq, delimiter=';')
        listaClientes = list(listaClientes)
    except FileNotFoundError:
        print("Arquivo não encontrado Locacao")
        return 0
    j=1
    for i in listaClientes:
        j=int(i['ID locacao'])
    return j
    
def encerraLocacao():
    '''
    Função que encerra a locação de um carro
    item(5)
    '''

def carrosDisponiveis():
    '''
    Função que mostra quais carros estão disponiveis para locação
    item(8)
    '''

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