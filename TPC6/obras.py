# Importar Dataset #


import csv

def readDataset(fnome):

    f = open(fnome, encoding = 'utf-8')
    f.readline()
    csv_reader = csv.reader(f, delimiter = ';')
    obras = []

    for row in csv_reader:
        obras.append(tuple(row))

    return obras


# Contar o Número de Obras no Dataset #


def contaObras(obras):

    nobras = 0
    
    for o in obras:
        nobras = nobras + 1

    print(f"Estão catalogadas {nobras} obras nesta base de dados.")


# Pretty Print das Obras #


def pp(obras):

    print("                                Título da Obra                                |     Período     |            Compositor            |  Ano  ")
    print("===========================================================================================================================================")
    for obra in obras:
        print(f"{obra[0][:77]:^77} | {obra[3][:15]:^15} | {obra[4][:32]:^32} | {obra[2][:6]:^6}")


# Escolher Elemento do Tuplo #


def ordTit(t):
    return t[0]

def ordAno(t):
    return t[1]


# Lista de tuplos (título, ano) ordenada alfabeticamente por título #


def listaTituloAno(obras):

    res = []

    for nome, _, ano, *_ in obras:
        res.append((nome, ano))

    res.sort(key = ordTit)

    return res


# Lista de tuplos (título, ano) ordenada crescentemente por ano #


def listaAnoTitulo(obras):

    res = []

    for obra in obras:
        res.append((obra[0], obra[2]))

    res.sort(key = ordAno)

    return res


# Dicionário de anos com títulos associados ao respetivo ano #


def titPorAno(obras):

    res = {}

    for nome, _, ano, *_ in obras:

        if ano in res.keys():
            res[ano].append(nome)
        
        else:
            res[ano] = [nome]

    return res 


# Lista Ordenada dos Compositores #


def listaCompositores(obras):

    compositores = []

    for obra in obras:

        if obra[4] not in compositores:
            compositores.append(obra[4])

    compositores.sort()

    return compositores


# Distribuição das Obras por Período #


def distribPeriodo(obras):

    dicPeriodo = {}

    for obra in obras:

        if obra[3] in dicPeriodo.keys():
            dicPeriodo[obra[3]] = dicPeriodo[obra[3]] + 1

        elif obra[3] not in dicPeriodo.keys():
            dicPeriodo[obra[3]] = 1

    return dicPeriodo


# Distribuição das Obras por Ano #


def distribAno(obras):

    dicAno = {}

    for obra in obras:

        if obra[2] in dicAno.keys():
            dicAno[obra[2]] = dicAno[obra[2]] + 1

        elif obra[2] not in dicAno.keys():
            dicAno[obra[2]] = 1

    return dicAno


# Distribuição das Obras por Compositor #


def distribCompositor(obras):

    dicComp = {}

    for obra in obras:

        if obra[4] in dicComp.keys():
            dicComp[obra[4]] = dicComp[obra[4]] + 1

        elif obra[4] not in dicComp.keys():
            dicComp[obra[4]] = 1

    return dicComp


# Gráfico das Distribuições #


import matplotlib.pyplot as plt

def criaGraf(distrib):

    plt.bar(distrib.keys(), distrib.values(), color = ['lightblue', 'lightgreen', 'yellow', 'orange', 'pink', 'blue', 'red'], width = 0.8)
    plt.xticks([n for n in range(0, len(distrib.keys()))], distrib.keys(), rotation = 'vertical')
    plt.show()


# Dicionário de compositores com as obras associadas ao respetivo compositor #


def obrasPorComp(obras):

    res = {}

    for o in obras:

        if o[4] in res.keys() and o[0] not in res[o[4]]:
            res[o[4]].append(o[0])

        elif o[4] not in res.keys():
            res[o[4]] = []
            res[o[4]].append(o[0])

    return res  


# Visualizar a estrutura de dados anterior #


def verObrasPorComp(dic):

    print("           Compositor           |                                         Lista de Obras do Compositor                                          ")
    print("================================================================================================================================================")

    for key in dic:
        obrasComp = list(dic.get(key, 0))
        print(f"{key[:31]:^31} | {obrasComp}")