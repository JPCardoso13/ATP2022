import obras


# Menus para a aplicação #


def preMenu():

    print("""
MENU:
> (1) - Carregar a base de dados
> (0) - Fechar a aplicação
""")


def menuPrincipal():

    print("""
MENU:
> (1) - Contar obras na base de dados
> (2) - Criar lista ordenada de compositores
> (3) - Visualizar uma tabela
> (4) - Produzir lista de tuplos (título, ano)
> (5) - Criar dicionário
> (6) - Calcular distribuição
> (7) - Criar gráfico de distribuição
> (0) - Fechar a aplicação
""")


def menuTabelas():

    print("""
Tabelas Disponíveis:
> (1) - Tabela com: Título | Período | Compositor | Ano
> (2) - Tabela de compositores e das obras associadas a cada compositor
> (0) - Retroceder
""")


def menuTuplos():

    print("""
Listas de Tuplos Disponíveis:
> (1) - Lista de tuplos (título, ano) ordenada alfabeticamente por título
> (2) - Lista de tuplos (título, ano) ordenada crescentemente por ano
> (0) - Retroceder
""")


def menuDicionarios():

    print("""
Dicionários Disponíveis:
> (1) - Dicionário de anos com títulos associados ao respetivo ano
> (2) - Dicionário de compositores com as obras associadas ao respetivo compositor
> (0) - Retroceder
""")


def menuDistrib():
   
    print("""
Distribuições Disponíveis:
> (1) - Distribuição das obras por período
> (2) - Distribuição das obras por ano
> (3) - Distribuição das obras por compositor
> (0) - Retroceder
""")


def menuGraficos():

        print("""
Gráficos Disponíveis:
> (1) - Distribuição das obras por período
> (2) - Distribuição das obras por ano
> (3) - Distribuição das obras por compositor
> (0) - Retroceder
""")


# Escolhas na aplicação encapsuladas #


def escolha3(dic):

    menuTabelas()
    tabelaEscolha = input("Selecione a opção desejada: ")

    while tabelaEscolha != "0":
                
        if tabelaEscolha == "1":
            obras.pp(myObras)

        elif tabelaEscolha == "2":
            
            if dic != {}:
                obras.verObrasPorComp(dic)

            else:
                print("Crie o dicionário de compositores com as obras associadas ao respetivo compositor antes de usar esta opção.")

        else:
            print("Opção inválida. Por favor selecione uma das opções disponíveis.")

        menuTabelas()
        tabelaEscolha = input("Selecione a opção desejada: ")


def escolha4():

    menuTuplos()
    tuploEscolha = input("Selecione a opção desejada: ")

    while tuploEscolha != "0":

        if tuploEscolha == "1":
            listaTitulos = obras.listaTituloAno(myObras)
            print("Lista de tuplos (título, ano) ordenada alfabeticamente por título:")
            print(listaTitulos)

        elif tuploEscolha == "2":
            listaAno = obras.listaAnoTitulo(myObras)
            print("Lista de tuplos (título, ano) ordenada crescentemente por ano:")
            print(listaAno)

        else:
            print("Opção inválida. Por favor selecione uma das opções disponíveis.")

        menuTuplos()
        tuploEscolha = input("Selecione a opção desejada: ")


def escolha5(dic):

    menuDicionarios()
    dicEscolha = input("Selecione a opção desejada: ")

    while dicEscolha != "0":

        if dicEscolha == "1":
            titulosPorAno = obras.titPorAno(myObras)
            print("Dicionário de anos com títulos associados ao respetivo ano:")
            print(titulosPorAno)

        elif dicEscolha == "2":
            obraPorComp = obras.obrasPorComp(myObras)
            print("Dicionário de compositores com as obras associadas ao respetivo compositor:")
            print(obraPorComp)
            dic.update(obraPorComp)

        else:
            print("Opção inválida. Por favor selecione uma das opções disponíveis.")

        menuDicionarios()
        dicEscolha = input("Selecione a opção desejada: ")
    

def escolha6(distrib1, distrib2, distrib3):

    menuDistrib()
    distribEscolha = input("Selecione a opção desejada: ")
    
    while distribEscolha != "0":

        if distribEscolha == "1":
            d1 = obras.distribPeriodo(myObras)
            print("Distribuição das obras por período:")
            print(d1)
            distrib1.update(d1)

        elif distribEscolha == "2":
            d2 = obras.distribAno(myObras)
            print("Distribuição das obras por ano:")
            print(d2)
            distrib2.update(d2)

        elif distribEscolha == "3":
            d3 = obras.distribCompositor(myObras)
            print("Distribuição das obras por compositor:")
            print(d3)
            distrib3.update(d3)

        else:
            print("Opção inválida. Por favor selecione uma das opções disponíveis.")

        menuDistrib()
        distribEscolha = input("Selecione a opção desejada: ")


def escolha7(distrib1, distrib2, distrib3):
    
    menuGraficos()
    grafEscolha = input("Selecione a opção desejada: ")
    
    while grafEscolha != "0":

        if grafEscolha == "1":
            
            if distrib1 != {}:
                obras.criaGraf(distrib1)

            else:
                print("Calcule a distribuição correspondente antes de usar esta função.")

        elif grafEscolha == "2":

            if distrib2 != {}:
                obras.criaGraf(distrib2)

            else:
                print("Calcule a distribuição correspondente antes de usar esta função.")

        elif grafEscolha == "3":
            
            if distrib3 != {}:
                obras.criaGraf(distrib3)

            else:
                print("Calcule a distribuição correspondente antes de usar esta função.")

        else:
            print("Opção inválida. Por favor selecione uma das opções disponíveis.")

        menuGraficos()
        grafEscolha = input("Selecione a opção desejada: ")


# Corpo da Aplicação #


def main():
    
    dic = {}
    distrib1 = {}
    distrib2 = {}
    distrib3 = {}
    menuPrincipal()
    escolha2 = input("Selecione a opção desejada: ")

    while escolha2 != "0":

        if escolha2 == "1":
            obras.contaObras(myObras)
        
        elif escolha2 == "2":
            compositores = obras.listaCompositores(myObras)
            print("Foi criada a seguinte lista ordenada de compositores da base de dados:")
            print(compositores)

        elif escolha2 == "3":
            escolha3(dic)

        elif escolha2 == "4":
            escolha4()

        elif escolha2 == "5":
            escolha5(dic)

        elif escolha2 == "6":
            escolha6(distrib1, distrib2, distrib3)

        elif escolha2 == "7":
            escolha7(distrib1, distrib2, distrib3)
           
        else:
            print("Opção inválida. Por favor selecione uma das opções disponíveis.")

        menuPrincipal()
        escolha2 = input("Selecione a opção desejada: ")

    print("Obrigado por utilizar a aplicação.")


# Aplicação #


print("Bem-vindo! Por favor carregue a base de dados antes de proceder.")
preMenu()
escolha1 = input("Selecione a opção desejada: ")

while escolha1 != "0":

    if escolha1 == "1":
        myObras = obras.readDataset("obras.csv")
        print("Base de dados carregada com sucesso. Por favor selcione a opção desejada.")
        main()
        break
    else:
        print("Opção inválida. Por favor selecione uma das opções disponíveis.")
        escolha1 = input("Selecione a opção desejada: ")

if escolha1 == "0":
    print("Obrigado por utilizar a aplicação.")