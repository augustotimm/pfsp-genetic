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
                        help="arquivo csv de entrada com makespan da instancia", metavar="FILE", default = "VFR10_15_1_Gap")
    parser.add_argument("-rp", "--repeat", dest="repeat",
                        help="Numero de vezes que deve ser rodado o algoritmo por completo", metavar="FILE", default=15)
    parser.add_argument("-m", "--machine", dest="machine", 
                        help="quantidade de maquinas para a instancia", metavar ="MACHINE", type = int, default = 10)
    parser.add_argument("-t", "--task", dest="task", 
                        help="quantidade de tarefas para a instancia", metavar ="TASK",type = int, default = 30)
    parser.add_argument("-i", "--iteration", dest="iteration", 
                        help="numero maximo de iteracoes a serem executadas", metavar ="ITERATION",type = int, default=20)
    parser.add_argument("-u", "--useless", dest="useless", 
                        help="numero maximo de iteracoes sem alterar o valor da solucao", metavar ="USELESS",type = int, default=10)
    parser.add_argument("-p", "--population", dest="population", 
                        help="tamanho da populacao", metavar ="ITERATION",type = int, default=10)
    parser.add_argument("-o", "--offspring", dest="offspring", 
                        help="quantidade de filhos a serem gerados por iteracao", metavar ="OFFSPRING",type = int, default=10)
    parser.add_argument("-s", "--seed", dest="seed", 
                       help="Nome do arquivo com lista de seeds", metavar ="ITERATION",type = str, default="seeds")
    args = parser.parse_args()

    repeatTimes = int(args.repeat)
    
    seedFile = args.seed
    uselessIterations = args.useless
    offSpringQuantity = args.offspring
    iterations = args.iteration
    populationSize = args.population
    tasksQuantity =args.task  #Quantidade de tarefas N
    machineQuantity= args.machine #Quantidade de maquinas M
    
    makeSpanMachineTask =[]
    seedList =[]
    seedListFromFile =[]
    with open("./in_files/"+args.filename+".csv",'rt') as f:
        reader = csv.reader(f)
        makeSpanMachineTask = list(reader)
    for i in range (machineQuantity):
        for j in range (tasksQuantity):
            makeSpanMachineTask[i][j] = int(makeSpanMachineTask[i][j])
    
    with open("./"+seedFile+".csv",'rt') as f:
        reader = csv.reader(f)
        seedListFromFile = list(reader)
    for i in range (len(seedListFromFile[0])):
        seedList.insert(len(seedList), int(seedListFromFile[0][i]))
    
    if(repeatTimes >= len(seedList)):
        repeatTimes = len(seedList)



    #Comeco do algoritmo
    #
    #
    for repetition in range(repeatTimes):
        random.seed(seedList[repetition])

        print("Repetiçao numero:"+ str(repetition))
        firstPopulation = [ populationlibrary.createRandomChild(tasksQuantity) for x in range(populationSize)]
        #for i in range(populationSize):
        #   firstPopulation [i]= populationlibrary.createRandomChild(tasksQuantity)
        makeSpanStart = pfsplibrary.getMasxMakespanOfList(firstPopulation,tasksQuantity,machineQuantity,makeSpanMachineTask)
        makeSpanStart.sort(key=lambda tup: tup[0])  

        with open("./out_files/"+args.filename+"_start_population_seed_"+str(seedList[repetition])+"repetition"+str(repetition)+".csv",'wt') as csvFile:
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
        isUseless = useless >= uselessIterations
        for individual in currentPopulation:
            lastPopulation.insert(0,(individual[0],individual[1], isUseless))
        lastPopulation.sort(key=lambda tup: tup[0])  
        with open("./out_files/"+args.filename+"_final_population_seed_"+str(seedList[repetition])+"repetition"+str(repetition)+".csv",'wt') as csvFile:
            filewriter = csv.writer(csvFile)
            filewriter.writerows(lastPopulation)

    
    



    



if __name__ == '__main__':
    main()