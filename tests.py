import random
import copy
childrenQuantity =3 #quantidade de filhos por geracao
childrenList = [0 for x in range(childrenQuantity)]

tasksQuantity =5  #Quantidade de tarefas N
machineQuantity=4 #Quantidade de maquinas M
variableColumns = tasksQuantity-1
makeSpanMachineTask =[[x +(y*5)for x in range(tasksQuantity) ]  for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina
orderDefiningVARIABLE =[[0 for x in range(tasksQuantity)] for x in range(tasksQuantity)]#Matriz de decisao para definir a ordem que serao executadas as tarefas

def createRandomChild(seed):
    random.seed(seed)
    childVariables =[[-1 for x in range(tasksQuantity)] for x in range(variableColumns)] #Removida a ultima coluna pois ela nunca será acessada pelo algoritmo
    for x in range(tasksQuantity):
        for y in range(x+1,tasksQuantity):
            newVal = random.randint(0,1)
            childVariables[x][y] = newVal
    return childVariables

#Funcao que fara o crossover
def twoPointCrossOver(parentA, parentB):
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

# Lista de testes
#ex1 = [[-1,0,0,0,0],[-1,-1,0,0,0],[-1,-1,-1,0,0],[-1,-1,-1,-1,0]]
#ex2 = [[-2,1,1,1,1],[-2,-2,1,1,1],[-2,-2,-2,1,1],[-2,-2,-2,-2,1]]
#ex3 = [[-2,0,0,0,0],[-2,-2,1,1,1],[-2,-2,-2,1,1],[-2,-2,-2,-2,1]]
#ex4 = [[-1,1,1,1,1],[-1,-1,0,0,0],[-1,-1,-1,0,0],[-1,-1,-1,-1,0]]
ex5 = [[-2,1,0,1,1],[-2,-2,1,1,1],[-2,-2,-2,1,1],[-2,-2,-2,-2,1]]

#0 i depois de K
#1 k depois de i
def evaluateFactibiltySolution(solution):
    #Cria a Lista de ordem de execucao
    order = createOrderList(solution)
    #Verifica se a ordem é possivel
    for i in range(tasksQuantity):
        for k in range ( i +1, tasksQuantity):
            kIndex = order.index(k)
            iIndex = order.index(i)
            
            if(solution[i][k] == 0):    
                #Se i vem depois de k, mas na lista ordenada está ao contrario, é infactivel
                if(iIndex<kIndex):
                    return []
            else:
                #Se i vem antes de k, mas na lista ordenada está ao contrario, é infactivel
                if(iIndex>kIndex):
                    return []
    
    return order
    


def createOrderList(solution):
    order = []
    #Cria a Lista de ordem de execucao
    for i in range(tasksQuantity):
        for k in range(i+1, tasksQuantity):
            if(i== 0):
                #Se i é 0, todos os elementos vao ser novos na lista
                if( k ==1):
                    if(solution[i][k] == 0):
                        order.insert(0,k)
                        order.insert(1,i)
                    else:
                         order.insert(0,i)
                         order.insert(1,k)
                else:
                    iIndex = order.index(i)
                    if(solution[i][k] == 0):
                        order.insert(iIndex,k)
                    else:
                        order.insert(iIndex+1,k)
            else:
                iIndex = order.index(i)
                kIndex = order.index(k)
                if(solution[i][k] == 0):
                    #se K vem depois de I vai ser necessario trocar a posicao de K
                    if(kIndex > iIndex):
                        order.remove(k)
                        order.insert(iIndex,k)
                else:
                    if(kIndex < iIndex):
                        order.remove(k)
                        order.insert(iIndex,k)
    return order

neworder=evaluateFactibiltySolution(ex5)

def createMakespanTable(solution):
    makespanTable = [[-1 for x in range(tasksQuantity)] for y in range(machineQuantity)]
    for machine in range(machineQuantity):
        lastMakespan =0
        for y in range(tasksQuantity):
            task = solution[y]
            if(machine == 0):
                makespanTable[machine][y] = lastMakespan + makeSpanMachineTask[machine][task]
                lastMakespan = makespanTable[machine][y]
            else:
                lastMachineCurrentTask =makespanTable[machine-1][y]
                lastTaskCurrentMachine =makespanTable[machine][y-1]
                if(lastMachineCurrentTask > lastTaskCurrentMachine):
                    makespanTable[machine][y] = lastMachineCurrentTask + makeSpanMachineTask[machine][task]
                else:
                    makespanTable[machine][y] = lastTaskCurrentMachine + makeSpanMachineTask[machine][task]
    return makespanTable

def getMaxMakespanOfsolution(solution):
    return max(max(createMakespanTable(solution)))

#child = twoPointCrossOver(ex1,ex2)