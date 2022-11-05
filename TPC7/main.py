### TPC7 - ATP2022 ###

import alunos


### ----- Menus da Aplicação ----- ###


# Listas de Opções e Títulos dos Menus e Tabelas #

opcPreMenu = ['Sair', 'Carregar dataset']
opcMainMenu = ['Sair', 'Distribuição dos alunos por curso (Dicionário)', 'Adicionar coluna de médias ao dataset', 'Adicionar coluna de escalões de notas ao dataset', 'Distribuição dos alunos por escalão (Dicionário)', 'Criar gráfico de linha de uma distribuição', 'Criar tabela de uma distribuição']
opcMenuGrafTab = ['Retroceder', 'Distribuição dos alunos por curso', 'Distribuição dos alunos por escalão']
titulos = ['MENU', 'Menu de Gráficos', 'Menu de Tabelas', 'Alunos por curso (Tabela)', 'Alunos por escalão']
extra = ['=', ' ', '_']


# Pré-Menu #

def preMenu():

    print(f'|{titulos[0]:=^30}|')

    for o in opcPreMenu:
        print(f'| > ({opcPreMenu.index(o)}) : {o:20} |')

    print(f'|{extra[0]*30}|')


# Menu Principal #

def mainMenu():

    print(f'|{titulos[0]:=^60}|')
    
    for opcao in opcMainMenu:
        print(f'| > ({opcMainMenu.index(opcao)}) : {opcao:50} |')

    print(f'|{extra[0]*60}|')


# Menu de Gráficos #

def menuGraf():

    print(f'|{extra[0]*50}|')
    print(f'|{titulos[1]:^50}|')
    print(f'|{extra[0]*50}|')

    for o in opcMenuGrafTab:
        print(f'| > ({opcMenuGrafTab.index(o)}) : {o:40} |')

    print(f'|{extra[0]*50}|')


# Menu de Tabelas #

def menuTab():

    print(f'|{extra[0]*50}|')
    print(f'|{titulos[2]:^50}|')
    print(f'|{extra[0]*50}|')

    for o in opcMenuGrafTab:
        print(f'| > ({opcMenuGrafTab.index(o)}) : {o:40} |')

    print(f'|{extra[0]*50}|')


### ----- Corpo da Aplicação ----- ###


def main():

    flag1 = True
    flag2 = True
    mainMenu()
    escolha = input("Selecione a opção desejada: ")

    while escolha != "0":

        if escolha == "1":
            print("Distribuição dos alunos por curso (Dicionário):")
            print(alunos.criaDistribCurso(dados))
            
        elif escolha == "2":

            if flag1:
                alunos.insereColMed(alunos.medNotas(dados))
                flag1 = False
                print("Coluna adicionada ao dataset.")

            else:
                print("Já adicionou essa coluna ao dataset.")

        elif escolha == "3":

            if not flag1 and flag2:
                alunos.insereColEsc(alunos.detEscalao(dados))
                flag2 = False
                print("Coluna adicionada ao dataset.")

            elif flag1:
                print("Adicione as médias dos alunos ao dataset antes de efetuar essa operação.")

            else:
                print("Já adicionou essa coluna ao dataset.")
            
        elif escolha == "4":

            if not flag2:
                print("Distribuição dos alunos por escalão (Dicionário):")
                print(alunos.criaDistribEsc(dados))

            else:
                print("Adicione os escalões dos alunos ao dataset antes de efetuar essa operação.")

        elif escolha == "5":

            menuGraf()
            escolhaGraf = input("Selecione a opção desejada: ")

            while escolhaGraf != "0":

                if escolhaGraf == "1":
                    alunos.criaGraf(alunos.criaDistribCurso(dados))

                elif escolhaGraf == "2":

                    if not flag2:
                        alunos.criaGraf(alunos.criaDistribEsc(dados))

                    else:
                        print("Adicione os escalões dos alunos ao dataset antes de efetuar essa operação.")

                else:
                    print("Opção inválida. Tem de selecionar uma das opções do menu.")

                menuGraf()
                escolhaGraf = input("Selecione a opção desejada: ")
            
        elif escolha == "6":

            menuTab()
            escolhaTab = input("Selecione a opção desejada: ")

            while escolhaTab != "0":

                if escolhaTab == "1":
                    print(f"> > > {titulos[3]}:")
                    print(f"|{extra[0]*32}|")
                    print("|     Curso     |     Alunos     |")
                    print(f"|{extra[0]*15}|{extra[0]*16}|")
                    alunos.criaTab(alunos.criaDistribCurso(dados))
                    print(f"|{extra[0]*32}|")

                elif escolhaTab == "2":

                    if not flag2:
                        print(f"> > > {titulos[4]}:")
                        print(f"|{extra[0]*32}|")
                        print("|    Escalão    |     Alunos     |")
                        print(f"|{extra[0]*15}|{extra[0]*16}|")
                        alunos.criaTab(alunos.criaDistribEsc(dados))
                        print(f"|{extra[0]*32}|")
                    
                    else:
                        print("Adicione os escalões dos alunos ao dataset antes de efetuar essa operação.")

                else:
                    print("Opção inválida. Tem de selecionar uma das opções do menu.")

                menuTab()
                escolhaTab = input("Selecione a opção desejada: ")
      
        else:
            print("Opção inválida. Tem de selecionar uma das opções do menu.")

        mainMenu()
        escolha = input("Selecione a opção desejada: ")


### ----- Aplicação ----- ###


print("Bem-vindo! Por favor carregue o dataset antes de proceder.")
preMenu()
preEscolha = input("Selecione a opção desejada: ")

while preEscolha != "0":

    if preEscolha == "1":
        dados = alunos.leDataset("alunos.csv")
        print("Dataset carregado com sucesso.")
        main()
        break

    else:
        print("Opção inválida. Tem de selecionar uma das opções do menu.")

    preMenu()
    preEscolha = input("Selecione a opção desejada: ")

print("Obrigado por utilizar a aplicação.")
