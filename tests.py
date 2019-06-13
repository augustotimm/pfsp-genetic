tasksQuantity =3  #Quantidade de tarefas N
machineQuantity=2 #Quantidade de maquinas M

makeSpanMachineTask =[[0 for x in range(tasksQuantity) ] for y in range(machineQuantity)] #Array bidimensional para salvar o makespan de cada tarefa em cada maquina
orderDefiningVARIABLE =[[0 for x in range(tasksQuantity)] for x in range(tasksQuantity)]#Matriz de decisao para definir a ordem que serao executadas as tarefas

