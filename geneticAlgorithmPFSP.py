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
    parser.add_argument("-rp", "--repeat", dest="repeat",
                        help="Numero de vezes que deve ser rodado o algoritmo por completo", metavar="FILE", default=1)
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

    repeatTimes = int(args.repeat)
    
    seed = args.seed
    random.seed(seed)
    uselessIterations = args.useless
    offSpringQuantity = args.offspring
    iterations = args.iteration
    populationSize = args.population
    tasksQuantity =args.task  #Quantidade de tarefas N
    machineQuantity= args.machine #Quantidade de maquinas M
    
    makeSpanMachineTask =[[x +(y*5)for x in range(tasksQuantity) ]  for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina
    filepathe = "./in_files/"+args.filename+".csv"
    with open(filepathe,'rt') as f:
        reader = csv.reader(f)
        makeSpanMachineTask = list(reader)
    makeSpanMachineTask = [ [int(i) for i in y] for y in makeSpanMachineTask]
   
    for repetition in range(repeatTimes):
        print("Repetiçao numero:"+ str(repetition))
        firstPopulation = [ populationlibrary.createRandomChild(tasksQuantity) for x in range(populationSize)]
        #for i in range(populationSize):
        #   firstPopulation [i]= populationlibrary.createRandomChild(tasksQuantity)
        makeSpanStart = pfsplibrary.getMasxMakespanOfList(firstPopulation,tasksQuantity,machineQuantity,makeSpanMachineTask)
        makeSpanStart.sort(key=lambda tup: tup[0])  

        with open("./out_files/"+args.filename+"_start_population"+str(repetition)+".csv",'wb') as csvFile:
            filewriter = csv.writer(csvFile)
            filewriter.writerows(makeSpanStart)
            


        currentPopulation = makeSpanStart
        i = 0
        lastValue = makeSpanStart[0][0]
        useless = 0

        while(i < iterations and useless < uselessIterations ):
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
            if(currentPopulation[0][0] == lastValue):
                useless += 1
            else:
                useless = 0
        lastPopulation = []
        for individual in currentPopulation:
            lastPopulation.insert(0,(individual[0],individual[1]))
        lastPopulation.sort(key=lambda tup: tup[0])  
        with open("./out_files/"+args.filename+"_final_population"+str(repetition)+".csv",'wb') as csvFile:
            filewriter = csv.writer(csvFile)
            filewriter.writerows(lastPopulation)

    
    



    



if __name__ == '__main__':
    main()