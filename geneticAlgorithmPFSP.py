# -*- coding: utf-8 -*-
import pfsplibrary
import populationlibrary
import argparse
from argparse import ArgumentParser
import sys
import csv
import random
childrenQuantity =3 #quantidade de filhos por geracao
childrenList = [0 for x in range(childrenQuantity)]




def main():
    parser = ArgumentParser()
    parser.add_argument("-if", "--inputfile", dest="filename",
                        help="arquivo csv de entrada com makespan da instancia", metavar="FILE")
    parser.add_argument("-of", "--outputfile", dest="outFilename",
                        help="arquivo csv de saida solucoes encontradas na execucao e seu resultado", metavar="FILE")
    parser.add_argument("-m", "--machine", dest="machine", 
                        help="quantidade de maquinas para a instancia", metavar ="MACHINE", type = int, default = 2)
    parser.add_argument("-t", "--task", dest="task", 
                        help="quantidade de tarefas para a instancia", metavar ="TASK",type = int, default = 3)
    parser.add_argument("-i", "--iteration", dest="iteration", 
                        help="numero maximo de iteracoes a serem executadas", metavar ="ITERATION",type = int, default=20)
    parser.add_argument("-u", "--useless", dest="useless", 
                        help="numero maximo de iteracoes sem alterar o valor da solucao", metavar ="USELESS",type = int, default=10)
    parser.add_argument("-p", "--population", dest="population", 
                        help="tamanho da populacao", metavar ="ITERATION",type = int, default=10)
    parser.add_argument("-o", "--offspring", dest="offspring", 
                        help="quantidade de filhos a serem gerados por iteracao", metavar ="OFFSPRING",type = int, default=10)
    parser.add_argument("-s", "--seed", dest="seed", 
                        help="seed para geracao de numeros randomicos", metavar ="ITERATION",type = int, default=13267849)
    args = parser.parse_args()

    seed = args.seed
    random.seed(seed)
    uselessIterations = args.useless
    offSpringQuantity = args.offspring
    iterations = args.iteration
    populationSize = args.population
    tasksQuantity =args.task  #Quantidade de tarefas N
    machineQuantity= args.machine #Quantidade de maquinas M
    
    makeSpanMachineTask =[[x +(y*5)for x in range(tasksQuantity) ]  for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina
    
    with open("./in_files/"+args.filename,'rb') as f:
        reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
        makeSpanMachineTask = list(reader)
    firstPopulation = [ populationlibrary.createRandomChild(tasksQuantity) for x in range(populationSize)]
    #for i in range(populationSize):
     #   firstPopulation [i]= populationlibrary.createRandomChild(tasksQuantity)
    makeSpanStart = pfsplibrary.getMasxMakespanOfList(firstPopulation,tasksQuantity,machineQuantity,makeSpanMachineTask)
    
    makeSpanStart.sort(key=lambda tup: tup[0])  

    currentPopulation = makeSpanStart
    i = 0
    useless = 0
    while(i < iterations and useless < uselessIterations ):
        print(currentPopulation)
        i+=1
        currentPopulation = populationlibrary.calculateFitness(currentPopulation,populationSize)        
        makeSpanStart.sort(key=lambda tup: tup[2],reverse= True)  
        parents = populationlibrary.selectParents(currentPopulation)
        while(len(parents)< 3):
            parents = populationlibrary.selectParents(currentPopulation)
        children = populationlibrary.generateOffSpring(parents,tasksQuantity,offSpringQuantity)
        children = pfsplibrary.getMasxMakespanOfList(children,tasksQuantity,machineQuantity,makeSpanMachineTask)
        newSolution = currentPopulation + children
        newSolution.sort(key=lambda tup: tup[0])  
        currentPopulation = newSolution[:populationSize]
        
    

    
    



    



if __name__ == '__main__':
    main()