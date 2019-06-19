# -*- coding: utf-8 -*-
import pfsplibrary
import populationlibrary
import argparse
from argparse import ArgumentParser
import sys
import csv

childrenQuantity =3 #quantidade de filhos por geracao
childrenList = [0 for x in range(childrenQuantity)]




def main():
    parser = ArgumentParser()
    parser.add_argument("-if", "--inputfile", dest="filename",
                        help="arquivo csv de entrada com makespan da instancia", metavar="FILE")
    parser.add_argument("-of", "--outputfile", dest="filename",
                        help="arquivo csv de saida solucoes encontradas na execucao e seu resultado", metavar="FILE")
    parser.add_argument("-m", "--machine", dest="machine", 
                        help="quantidade de maquinas para a instancia", metavar ="MACHINE", type = int)
    parser.add_argument("-t", "--task", dest="task", 
                        help="quantidade de tarefas para a instancia", metavar ="TASK",type = int)
    parser.add_argument("-i", "--iteration", dest="iteration", 
                        help="numero maximo de iteracoes a serem executadas", metavar ="ITERATION",type = int, default=20)
    parser.add_argument("-p", "--population", dest="population", 
                        help="tamanho da populacao", metavar ="ITERATION",type = int, default=10)
    parser.add_argument("-s", "--seed", dest="seed", 
                        help="seed para geracao de numeros randomicos", metavar ="ITERATION",type = int, default=132649)
    args = parser.parse_args()

    seed = args.seed
    iteration = args.iteration
    populationSize = args.population
    tasksQuantity =args.task  #Quantidade de tarefas N
    machineQuantity= args.machine #Quantidade de maquinas M
    variableColumns = tasksQuantity-1
    makeSpanMachineTask =[[x +(y*5)for x in range(tasksQuantity) ]  for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina
    orderDefiningVARIABLE =[[0 for x in range(tasksQuantity)] for x in range(tasksQuantity)]#Matriz de decisao para definir a ordem que serao executadas as tarefas
    with open("./in_files/"+args.filename,'rb') as f:
        reader = csv.reader(f)
        makeSpanMachineTask = list(reader)

    population = []
    
    print(population)



    



if __name__ == '__main__':
    main()