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
                        help="numero maximo de iteracoes a serem executadas", metavar ="ITERATION",type = int)

    args = parser.parse_args()

    iteration = args.iteration
    tasksQuantity =args.task  #Quantidade de tarefas N
    machineQuantity= args.machine #Quantidade de maquinas M
    variableColumns = tasksQuantity-1
    makeSpanMachineTask =[[x +(y*5)for x in range(tasksQuantity) ]  for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina
    with open("./in_files/"+args.filename,'rb') as f:
        reader = csv.reader(f)
        makeSpanMachineTask = list(reader)
    orderDefiningVARIABLE =[[0 for x in range(tasksQuantity)] for x in range(tasksQuantity)]#Matriz de decisao para definir a ordem que serao executadas as tarefas

    print (makeSpanMachineTask)
    print("args:")
    print(args.filename)
    print(args.task)


if __name__ == '__main__':
    main()