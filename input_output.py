import processos as gproc
import arquivos
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

def gera_arquivos(fileFiles):
    vetor = []
    with open (fileFiles,"r") as input_file:
        temporario = input_file.read().splitlines()
    vetor.append(int( temporario[0]))
    i = int(temporario[1])
    for it in range(2, i+2):
        vetor.append(temporario[it])
    disco = arquivos.G_Arquivos(vetor)
    instructions = []
    for it in range(i+2,len(temporario)):
        instructions.append(temporario[it])
    print(disco)
    print(instructions)
    return [disco,instructions]