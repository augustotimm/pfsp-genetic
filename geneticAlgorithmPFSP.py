# -*- coding: utf-8 -*-
import pfsplibrary
import populationlibrary
import argparse
from argparse import ArgumentParser
import sys
import csv
import random
import time
from functools import wraps






def main():
    parser = ArgumentParser()
    parser.add_argument("-if", "--inputfile", dest="filename",
                        help="arquivo csv de entrada com makespan da instancia", metavar="FILE", default = "ready_VFR10_15_1_Gap")
    parser.add_argument("-rp", "--repeat", dest="repeat",
                        help="Numero de vezes que deve ser rodado o algoritmo por completo", metavar="FILE", default=15)
    parser.add_argument("-i", "--iteration", dest="iteration", 
                        help="numero maximo de iteracoes a serem executadas", metavar ="ITERATION",type = int, default=30)
    parser.add_argument("-u", "--useless", dest="useless", 
                        help="numero maximo de iteracoes sem alterar o valor da solucao", metavar ="USELESS",type = int, default=15)
    parser.add_argument("-p", "--population", dest="population", 
                        help="tamanho da populacao", metavar ="ITERATION",type = int, default=100)
    parser.add_argument("-o", "--offspring", dest="offspring", 
                        help="quantidade de filhos a serem gerados por iteracao", metavar ="OFFSPRING",type = int, default=30)
    parser.add_argument("-s", "--seed", dest="seed", 
                       help="Nome do arquivo com lista de seeds", metavar ="ITERATION",type = str, default="seeds")
    args = parser.parse_args()

    repeatTimes = int(args.repeat)
    
    seedFile = args.seed
    uselessIterations = args.useless
    offSpringQuantity = args.offspring
    iterations = args.iteration
    populationSize = args.population

    
    makeSpanMachineTask =[]
    seedList =[]
    seedListFromFile =[]
    with open("./in_files/"+args.filename+".csv",'rt') as f:
        reader = csv.reader(f)
        makeSpanMachineTaskSTR = list(reader)
    machineQuantity = len(makeSpanMachineTaskSTR[0])
    tasksQuantity = len(makeSpanMachineTaskSTR)
    makeSpanMachineTask=[[0 for i in range(tasksQuantity)] for y in range(machineQuantity)]
    for i in range (machineQuantity):
        for j in range (tasksQuantity):
            makeSpanMachineTask[i][j] = int(makeSpanMachineTaskSTR[j][i])

   

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
    startFile = []
    endFile = []
    for repetition in range(repeatTimes):
        start = time.time()
        random.seed(seedList[repetition])
        if( seedList[ repetition] == 8435970344):
            print(repetition)

        print("Repetiçao numero:"+ str(repetition))
        firstPopulation = [ populationlibrary.createRandomChild(tasksQuantity) for x in range(populationSize)]
        #for i in range(populationSize):
        #   firstPopulation [i]= populationlibrary.createRandomChild(tasksQuantity)
        makeSpanStart = pfsplibrary.getMaxMakespanOfList(firstPopulation,tasksQuantity,machineQuantity,makeSpanMachineTask)
        makeSpanStart.sort(key=lambda tup: tup[0])  
        startFile += [makeSpanStart[0]]

        
            


        currentPopulation = makeSpanStart
        i = 0
        lastValue = makeSpanStart[0][0]
        useless = 0

        while(i < iterations and useless < uselessIterations ):
            i+=1
            currentPopulation = populationlibrary.calculateFitness(currentPopulation,populationSize)        
            parents = populationlibrary.selectParents(currentPopulation)
            while(len(parents)< 3):
                parents = populationlibrary.selectParents(currentPopulation)
            children = populationlibrary.generateOffSpring(parents,tasksQuantity,offSpringQuantity)
            children = pfsplibrary.getMaxMakespanOfList(children,tasksQuantity,machineQuantity,makeSpanMachineTask)
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
        end=time.time() 
        elapsed = end - start
        endFile += [(lastPopulation[0], elapsed)]
    
    with open("./out_files/"+args.filename+"_final_populations.csv",'wt') as csvFile:
        filewriter = csv.writer(csvFile)
        filewriter.writerows(endFile)
    
    with open("./out_files/"+args.filename+"_start_populations.csv",'wt') as csvFile:
            filewriter = csv.writer(csvFile)
            filewriter.writerows(startFile)
    
    



    



if __name__ == '__main__':
    main()