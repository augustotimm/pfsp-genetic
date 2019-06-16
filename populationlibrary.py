# -*- coding: utf-8 -*-
import random
import copy

def createRandomChild(seed,tasksQuantity):
    random.seed(seed)
    variableColumns = tasksQuantity-1
    childVariables =[[-1 for x in range(tasksQuantity)] for x in range(variableColumns)] #Removida a ultima coluna pois ela nunca será acessada pelo algoritmo
    for x in range(tasksQuantity):
        for y in range(x+1,tasksQuantity):
            newVal = random.randint(0,1)
            childVariables[x][y] = newVal
    return childVariables

#Funcao que fara o crossover
def twoPointCrossOver(parentA, parentB, tasksQuantity):
    variableColumns = tasksQuantity -1
    newChild = copy.deepcopy( parentA)
    pointAX = random.randint(1,variableColumns) 
    pointAY = random.randint(pointAX ,tasksQuantity) 
    pointBX = random.randint(pointAX ,variableColumns) 
    if(pointBX ==pointAX ):
        pointBY = random.randint(pointAY ,tasksQuantity) 
    else:
        pointBY = random.randint(pointBX ,tasksQuantity) 
    #Verifica se vai ser necessario alterar mais de uma linha
    if(pointAX == pointBX):
        #verificar se sera mais de um elemento
            if(pointAY == pointBY):
                #se x e y sao iguais, é alterado apenas um elemento
                newChild[pointAX-1][pointAY-1] = parentB[pointAX-1][pointAY-1]
            else:
                #alterado apenas o intervalo entre AY e BY
                for y in range(pointAY-1,pointBY):
                    newChild[pointAX-1][y] = parentB[pointAX-1][y]
    #Mais de uma linha alterada                    
    else:
        #percorrerá todas as linhas alteradas
        for x in range(pointAX-1,pointBX):
            if(x == pointAX-1):
                #A linha do elemento A nao deve ser copiada por inteira, apenas os elementos herdados
                if( pointAY == tasksQuantity):
                    #se AY é for a ultima coluna é herdado apenas um elemento da linha
                    newChild[x][pointAY-1] = parentB[x][pointAY-1]
                else:
                    #caso contrario é necessario percorrer os elementos no intervalo apó AY
                    for y in range(pointAY-1,tasksQuantity):
                        newChild[x][y] = parentB[x][y]
            elif(x==pointBX-1):
                if(pointBY == x+1):
                    newChild[x][pointBY-1] = parentB[x][pointBY-1]
                #A linha do elemento B nao deve ser herdada inteira, apenas até BY
                else:
                    for y in range(x+1,pointBY):
                        newChild[x][y] = parentB[x][y]
            else:
                for y in range(x+1,tasksQuantity):
                    newChild[x][y] = parentB[x][y]
    return newChild
