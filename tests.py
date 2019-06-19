import random
import copy
childrenQuantity =3 #quantidade de filhos por geracao
childrenList = [0 for x in range(childrenQuantity)]

tasksQuantity =4  #Quantidade de tarefas N
machineQuantity=2 #Quantidade de maquinas M

makeSpanMachineTask =[[1 for x in range(tasksQuantity) ]  for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina

orderList = []

def createRandomChild():
    order =  (range(tasksQuantity))
    random.shuffle(order)
    return order
child1 = createRandomChild()
child2 = createRandomChild()

#Funcao que fara o crossover
def onePointCrossOver(parentA, parentB):
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
child3 = onePointCrossOver(child1,child2)

def createMakespanTable(solution):
    makespanTable = [[-1 for x in range(tasksQuantity)] for y in range(machineQuantity)]
    for machine in range(machineQuantity):
        lastMakespan =0
        for taskIterator in range(0,len(solution)):
            currentTask = solution[ taskIterator]
            previousTask = solution[taskIterator-1]
            if(machine == 0):
                makespanTable[machine][currentTask] = lastMakespan + makeSpanMachineTask[machine][currentTask]
                lastMakespan = makespanTable[machine][currentTask]
            else:
                lastMachineCurrentTask =makespanTable[machine-1][currentTask]
                lastTaskCurrentMachine =makespanTable[machine][previousTask]
                if(lastMachineCurrentTask > lastTaskCurrentMachine or taskIterator == 0):
                    makespanTable[machine][currentTask] = lastMachineCurrentTask + makeSpanMachineTask[machine][currentTask]
                else:
                    makespanTable[machine][currentTask] = lastTaskCurrentMachine + makeSpanMachineTask[machine][currentTask]
    return makespanTable
result = createMakespanTable(child1)


def getMaxMakespanOfsolution(solution):
    return max(max(createMakespanTable(solution)))

#child = twoPointCrossOver(ex1,ex2)