# -*- coding: utf-8 -*-
def createMakespanTable(solution,machineQuantity,tasksQuantity,makeSpanMachineTask):
    makespanTable = [[-1 for x in range(tasksQuantity)] for y in range(machineQuantity)]

    for machine in range(machineQuantity):
        lastMakespan =0
        for taskIterator in range(0,len(solution)):
            currentTask = solution[ taskIterator]
            previousTask = solution[taskIterator-1]
            currentMakespan = makeSpanMachineTask[machine][currentTask]
            if(machine == 0):
                makespanTable[machine][currentTask] = lastMakespan + currentMakespan
                lastMakespan = makespanTable[machine][currentTask]
            else:
                lastMachineMakespan =makespanTable[machine-1][currentTask]
                lastTaskMakespan =makespanTable[machine][previousTask]
                if(lastMachineMakespan < lastTaskMakespan and taskIterator == 0):
                    print(lastMachineMakespan)
                if(lastMachineMakespan > lastTaskMakespan or taskIterator == 0):
                    makespanTable[machine][currentTask] = lastMachineMakespan + currentMakespan
                else:
                    makespanTable[machine][currentTask] = lastTaskMakespan + currentMakespan
    return makespanTable


def getMaxMakespanOfsolution(solution,tasksQuantity,machineQuantity,makeSpanMachineTask):
    return max(max(createMakespanTable(solution,tasksQuantity,machineQuantity,makeSpanMachineTask)))

def getMaxMakespanOfList(solutionList,tasksQuantity,machineQuantity,makeSpanMachineTask):
    newSolution =[]
    for solution in solutionList:
        currentSolutionValue = getMaxMakespanOfsolution(solution,machineQuantity,tasksQuantity,makeSpanMachineTask)
        newSolution.insert(0, (currentSolutionValue,solution) )
    return newSolution
