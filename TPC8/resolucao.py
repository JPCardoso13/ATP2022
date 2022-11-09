### TPC8 - ATP2022 ###


### ----- Questão 1 ----- ###


# tpc1.a) -

def inicDiferente(s1, s2):
    
    res = 0

    for e in s1:

        if e in s2:
            return res

        res += 1
    
    print(len(s1))


# tpc1.b) -

def acimaMedia(n):

    res = 0
    soma = 0
    nums = []

    for i in range(n):
        n = int(input(f"Selecione o {i + 1}º número: "))
        nums.append(n)
        soma += n

    med = soma / len(nums)

    for n in nums:

        if n > med:
            res += 1
    
    return res


# tpc1.c) -

def merge(l1, l2):
        
    l3 = l1 + l2

    for i in range(len(l3)):

        for j in range(i + 1, len(l3)):

            if l3[i] > l3[j]:
                l3[i], l3[j] = l3[j], l3[i]

    return l3


# tpc1.d) -

def figuais(f1, f2):

    with open(f1) as file1, open(f2) as file2:
        content1 = file1.readlines()
        content2 = file2.readlines()
        content1.sort()
        content2.sort()

    return content1 == content2


### ----- Questão 2 ----- ###


# tpc2.a) -

def atores(cinemateca):

    listaAtores = []

    for filme in cinemateca:

        for ator in filme[2]:

            if ator not in listaAtores:
                listaAtores.append(ator)

    listaAtores.sort()

    return listaAtores


# tpc2.b) -

def listarPorGenero(cinemateca, genero):
    
    res = []

    for filme in cinemateca:

        if genero in filme[3]:
            res.append(filme[0])

    res.sort()
    
    return res


# tpc2.c) -

def maiorElenco(cinemateca):
    
    maior = cinemateca[0]
    
    for filme in cinemateca:

        if len(filme[2]) > len(maior[2]):
            maior = filme

    return maior[0]


# tpc2.d) -

def filmePorGenero( cinemateca ):
    
    distribGen = {}

    for filme in cinemateca:

        for genero in filme[3]:

            if genero not in distribGen.keys():
                distribGen[genero] = 1

            else:
                distribGen[genero] += 1

    return distribGen


# tpc2.e) -

import matplotlib.pyplot as plt

def criaGraf(distrib):

    xAxis = [x for x in distrib.keys()]
    yAxis = [y for y in distrib.values()]

    plt.bar(xAxis, yAxis, width = 0.6, color = ['yellow', 'pink', 'lightblue', 'grey'])
    plt.yticks(yAxis)
    plt.title("Distribuição dos Filmes por Género")
    plt.xlabel("Género")
    plt.ylabel("Número de Filmes")
    plt.show()
