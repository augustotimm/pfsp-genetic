# -*- coding: utf-8 -*-
import random
import copy

def createRandomChild(tasksQuantity):
    order =  range(tasksQuantity)
    random.shuffle(order)
    return order

#Funcao que fara o crossover
def onePointCrossOver(parentA, parentB,tasksQuantity):
    crossOverPoint = random.randint(0,tasksQuantity-1)
    child = parentA[0:crossOverPoint] + parentB[crossOverPoint:tasksQuantity]
    aPart =parentA[0:crossOverPoint] + [-1 for x in range(crossOverPoint,tasksQuantity)]
    
    if(crossOverPoint != 0 or crossOverPoint != tasksQuantity-1):
        while(  len(child) != len(set(child)) ):
            for iterator in range(crossOverPoint,tasksQuantity):
                bPart = child[iterator] 
                if(bPart in aPart ):
                    if(bPart != parentA[iterator]):
                        child[iterator] = parentA[iterator]
                        #agora esse elemento tambem é herdado do pai A
                        aPart[iterator]=child[iterator]
    return child

def calculateFitness(population, populationSize):
    fitnessSum = sum(1/individual[0] for individual in population )
    for individualIterator in range(populationSize):
        population[individualIterator] = (population[individualIterator][0],population[individualIterator][1], (1/population[individualIterator][0])/fitnessSum)
    return population

def generateOffSpring(parents, tasksQuantity,offSpringQuantity):
   
    offspring = []
    i=0
    while( i < len(parents) and offSpringQuantity> len(offspring) ):
        #print(i)
        offspring.insert(0, onePointCrossOver(parents[i],parents[i+1],tasksQuantity))
        offspring.insert(0, onePointCrossOver(parents[i+1],parents[i],tasksQuantity))
    if(len(offspring) < offSpringQuantity):
        for j in range(len(offspring), offSpringQuantity):
            parentAIndex = random.randint(0, len(parents))
            parentBIndex = random.randint(0, len(parents))
            while( parentAIndex == parentBIndex):
                parentAIndex = random.randint(0, len(parents))
                parentBIndex = random.randint(0, len(parents))
            offspring.insert(0, onePointCrossOver(parents[parentAIndex],parents[parentBIndex],tasksQuantity))
    return offspring

def selectParents(currentPopulation):
    parents = []
    r = random.random()
    chosenSum = 0
    individualNumber = 0
    while(r>chosenSum):
        chosenSum += currentPopulation[individualNumber][2]
        parents.insert(0, currentPopulation[individualNumber][1])
    
    return parents
