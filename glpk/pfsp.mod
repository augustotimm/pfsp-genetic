# Conjunto de tarefas
set N;

# Conjunto de maquinas
set M;



#Parametro de makespan de cada tarefa i em cada maquina j
set T {i in N, r in M};

#Constante infinitamente grande
set P;

#Variavel de decisao que indica a ordem de execucao dos processos
# 1 se processo i vem depois do processo k
# 0 caso contrario
var D  {i in N, k in N} binary;


#Variavel com o resultado de makespan de cada tarefa i em cada maquina j
var C {i in N, r in M};

var Cmax;

# Função objetivo.
# Minimiza o makespan maximo
minimize makespan: Cmax;

# calcula o makespan minimo para cada tarefa na maquina 1
s.t. rest1 {i in N} : C[i,1]  >= T[i,1];

# calcula o makespan da maquina 1 para todas as tarefas
s.t. rest2 {i in N, r in M : r > 1}: C[r,i] - C[r-1,i] >= T[r,i];

# 
s.t. rest3 {k in N, i in N, r in M : k > 1 and i < k}: C[r,i] -C[r,k]  + P * D[i,k] >= T[k,r];

# 
s.t. rest4 {k in N, i in N, r in M : k > 1 and i < k}: C[r,i] -C[r,k]  + P * D[i,k] <= P - T[k,r];

# 
s.t. rest5 {i in N}: Cmax >= C[i,M];

# 
s.t. maquina6: xir in C >= 0;


