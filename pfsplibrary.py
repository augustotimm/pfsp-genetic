# -*- coding: utf-8 -*-
def createMakespanTable(solution,machineQuantity,tasksQuantity,makeSpanMachineTask):
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


def getMaxMakespanOfsolution(solution,tasksQuantity,machineQuantity,makeSpanMachineTask):
    return max(max(createMakespanTable(solution,tasksQuantity,machineQuantity,makeSpanMachineTask)))
