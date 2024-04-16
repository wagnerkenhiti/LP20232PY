import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaCarros as mcar
import manipulaLocacao as mloc
import apresentacao
# 123.456.789-22
# 07/04/2025 20h

#utilizar continue nas vendas

def main():
    '''
    # exemplo de uso do menu (ainda não faz nada de util, so é exibido)
    opcao = apresentacao.MenuPrincipal()
    print(f'Opção desejada foi {opcao}')
    ###
    print("*"*30)
    print("Exemplo de carregamento de dados de um arquivo csv")
    listaClientes = mcli.carregar()
    print(listaClientes)
    print("*"*30)
    print()
    print("*"*30)
    print("Exemplo de leitura dos campos e armazenamento em um arquivo csv")
    mcli.cadastrar(listaClientes)
    print("*"*30)
    print()
    print("*"*30)
    print("Exemplo de exclusão de um cliente e armazenamento em um arquivo csv")
    cpf = input("Qual cpf do cliente que deseja excluir? ")
    if  mcli.excluir(listaClientes, cpf) == True:
        print("Cliente excluido com sucesso")
    else:
        print("Cliente não encontrado")
    print()
    print("*"*30)
    print("Exemplo de leitura dos campos e armazenamento em um arquivo csv")
    print("*"*30)
    listaCarros = mcar.carregar()
    mcar.cadastrar(listaCarros)
    '''
    opcao = apresentacao.MenuPrincipal()
    while (opcao != 9):
        if opcao == 1:
            opcao1 = apresentacao.MenuLocacao()
            if opcao1 == 1:
                mloc.novaLocacao()
            elif opcao1 == 2:
                mloc.encerraLocacao()
            elif opcao1 == 3:
                categoria_procurar = input("Digite a categoria de carro para procurar: ")
                verifica = mloc.carrosDisponiveis(categoria_procurar)
                if verifica == False:
                    print("Não há carros disponiveis nessa categoria.")
            elif opcao1 == 4:
                #20/04/2024 21:00
                mloc.carrosLocados()
        elif opcao == 2:
            opcao1 = apresentacao.MenuCliente()
            if opcao1 == 1:
                lista0=mcsv.carregarDados("Cliente.csv")
                mcli.cadastrar(lista0)
            elif opcao1 == 2:
                cpf=input("Digite o CPF da pessoa a ter os dados atualizados: ")
                mcli.alterar(cpf)
            elif opcao1 == 3:
                lista0=mcsv.carregarDados("Cliente.csv")
                cpf=input("Digite o CPF da pessoa a ter os dados excluidos: ")
                if(mcli.excluir(lista0,cpf)):
                    print("Excluido com sucesso!")
            elif opcao1 == 4:
                identificacao=input("Digite o nome ou CPF para localizar as locacoes do cliete: ")
                mcli.localizarLocacao(identificacao)
        elif opcao == 3:
            opcao1 = apresentacao.MenuCarro()
            if opcao1 == 1:
                lista1=mcsv.carregarDados("Carro.csv")
                mcar.cadastrar(lista1)
            elif opcao1 == 2:
                placa=input("Digite a placa do carro a ser alterado: ")
                mcar.alterar(placa)
            elif opcao1 == 3:
                placa=input("Digite a placa do carro a ser excluido: ")
                mcar.excluir(placa)
            elif opcao1 == 4:
                mcar.venda()
        opcao = apresentacao.MenuPrincipal()
    
    print("Encerrando o programa.")
    

# Inicio do programa 
if __name__ == "__main__":
    main()