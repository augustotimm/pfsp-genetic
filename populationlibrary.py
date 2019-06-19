# -*- coding: utf-8 -*-
import random
import copy

def createRandomChild(seed,tasksQuantity):
    random.seed(seed)
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
