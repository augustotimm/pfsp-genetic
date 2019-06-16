# -*- coding: utf-8 -*-
#0 i depois de K
#1 k depois de i
def getOrderedSolutionArray(solution,tasksQuantity):
    #Cria a Lista de ordem de execucao
    order = createOrderList(solution,tasksQuantity)
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
    

def createOrderList(solution,tasksQuantity):
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

#Cria tabela com o makespan de cada problema em cada maquina para uma instancia especifica do problema
def createMakespanTable(solution,tasksQuantity,machineQuantity,makeSpanMachineTask):
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


def getMaxMakespanOfsolution(solution,tasksQuantity,machineQuantity,makeSpanMachineTask):
    return max(max(createMakespanTable(solution,tasksQuantity,machineQuantity,makeSpanMachineTask)))
