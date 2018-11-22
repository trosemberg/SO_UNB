import processos as gproc
def gera_processos(fileProc):
    id = 0
    processos= []
    with open(fileProc,"r") as input_proc:
        for linha in input_proc:
            processos.append(gproc.Processos([int(x) for x in linha.split(',')]))
    #arruma o vetor de processo de menor tempo a maior tempo de inicializacao
    processos.sort(key = lambda x:x.t_init,reverse = False)
    #arruma o id de cada processo com base no tempo de inicializacao.
    for processo in processos:
        processo.PID = id
        id+=1
    return processos