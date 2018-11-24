import processo as gproc
"""
    Arquivo responsavel pelas funcoes que farao a leitura dos arquivos de entrada
    e pela saida do programa.
"""

"""
    Gera os processos a partir do primeiro arquivo
"""
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

"""
    Responsavel por ler o segundo arquivo e retornar um vetor que sera usado para a criacao
    da memoria de arquivos e as instrucoes para serem colocadas nos processos 
"""
def gera_arquivos(fileFiles):
    vetor = []
    with open (fileFiles,"r") as input_file:
        temporario = input_file.read().splitlines()
    vetor.append(int( temporario[0]))
    i = int(temporario[1])
    for it in range(2, i+2):
        vetor.append(temporario[it])
    instructions = []
    for it in range(i+2,len(temporario)):
        instructions.append(temporario[it])
    return [vetor,instructions]
