import manipulaCSV as mcsv
import manipulaClientes as mcli
import manipulaCarros as mcar
import manipulaLocacao as mloc
import apresentacao
# 123.456.789-22
# 07/04/2025 20h

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
                mloc.carrosLocados()
        elif opcao == 2:
            opcao1 = apresentacao.MenuCliente()
            if opcao1 == 1:
                mcli.cadastrar()
            elif opcao1 == 2:
                mcli.alterar()
            elif opcao1 == 3:
                mcli.excluir()
            elif opcao1 == 4:
                mcli.localizarLocacao()
        elif opcao == 3:
            opcao1 = apresentacao.MenuCarro()
            if opcao1 == 1:
                mcar.cadastrar()
            elif opcao1 == 2:
                mcar.alterar()
            elif opcao1 == 3:
                mcar.excluir()
            elif opcao1 == 4:
                mcar.venda()
        opcao = apresentacao.MenuPrincipal()
    
    print("Encerrando o programa.")

# Inicio do programa 
if __name__ == "__main__":
    main()