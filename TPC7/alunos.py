### TPC7 - ATP2022 ###

import csv
import string
import matplotlib.pyplot as plt


### ----- Funções ----- ###


# Ler o dataset #

def leDataset(file):

    dados = []
    dataset = open(file, encoding = 'utf-8') 
    dataset.readline()
    csv_reader = csv.reader(dataset, delimiter = ',')

    for row in csv_reader:
        dados.append(tuple(row))

    dataset.close()

    return dados


# Distribuição dos alunos p/ curso (Dicionário) #

def criaDistribCurso(dados):

    distribCurso = {}

    for aluno in dados:

        if aluno[2] not in distribCurso.keys():
            distribCurso[aluno[2]] = 1

        elif aluno[2] in distribCurso.keys():
            distribCurso[aluno[2]] = distribCurso[aluno[2]] + 1

    return distribCurso


# Calcular médias das notas de cada aluno, atualizando os dados #

def medNotas(dados):

    for n in range(0, len(dados)):
        media = str((float(dados[n][3]) + float(dados[n][4]) + float(dados[n][5]) + float(dados[n][6])) / 4)
        aluno = list(dados[n])
        aluno.append(media)
        dados[n] = tuple(aluno)

    return dados


# Adicionar coluna de médias ao dataset #

def insereColMed(dados):

    newfile = open("alunos.csv", "w", encoding = 'utf-8')
    csv_writer = csv.writer(newfile, lineterminator = '\n')
    csv_writer.writerow(['id_aluno', 'nome', 'curso', 'tpc1', 'tpc2', 'tpc3', 'tpc4', 'media'])
    csv_writer.writerows(dados)
    newfile.close()

    return dados


# Determinar escalão de notas de cada aluno, atualizando os dados #

def detEscalao(dados):

    for i in range(0, len(dados)):

        min = 0
        max = 4
        n = 4

        while n >= 0:

            if min <= round(float(dados[i][7])) <= max:
                aluno = list(dados[i])
                aluno.append(string.ascii_uppercase[n])
                dados[i] = tuple(aluno)

            min = max + 1
            max = max + 4
            n = n - 1

    return dados


# Adicionar coluna de escalões de notas ao dataset #

def insereColEsc(dados):

    newfile = open("alunos.csv", "w", encoding = 'utf-8')
    csv_writer = csv.writer(newfile, lineterminator = '\n')
    csv_writer.writerow(['id_aluno', 'nome', 'curso', 'tpc1', 'tpc2', 'tpc3', 'tpc4', 'media', 'escalao'])
    csv_writer.writerows(dados)
    newfile.close()

    return dados


# Distribuição dos alunos p/ escalão de notas #

def criaDistribEsc(dados):

    distribEsc = {}

    for aluno in dados:

        if aluno[8] not in distribEsc.keys():
            distribEsc[aluno[8]] = 1

        elif aluno[8] in distribEsc.keys():
            distribEsc[aluno[8]] = distribEsc[aluno[8]] + 1

    return distribEsc


# Gráfico de linha de uma distribuição #

def criaGraf(distrib):
    
    abcissas = [x for x in range(1, len(distrib) + 1)]
    ordenadas = []

    for key in distrib:
        y = distrib[key]
        ordenadas.append(y)

    plt.plot(abcissas, ordenadas, color = 'lightblue', linewidth = 3, marker = 'o', markerfacecolor='blue', markersize = 10)
    plt.xticks(abcissas, distrib.keys())
    plt.yticks(ordenadas, distrib.values())
    plt.title('Distribuição em Gráfico de Linha')
    plt.ylabel('Número de Alunos')
    plt.show()


# Imprimir tabela de uma distribuição #

def criaTab(distrib):
    
    for key in distrib:
        print(f'| {key:^13} | {distrib[key]:^14} |')
