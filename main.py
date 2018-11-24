import sys
import processos as gproc
import memoria as gmem
import recursos as ges
import arquivos as garq
from input_output import gera_processos,gera_arquivos

"""
    Os imports estao sendo feitos como g+primeira letra do import pois e gerenciador de...
    es = entrada e saida
"""

def start():
    """
        variavel memoria e responsavel pelo gerenciamento de memoria,
        variavel drivers e responsavel pelo gerenciamento dos drivers
        variavel disco e responsavel pelo gerenciamento dos arquivos em disco
        variavel g_processos e responsavel pelo gerenciamento de processos
    """
    memoria = gmem.G_Memoria()
    drivers = ges.G_Drivers()
    processos = []
    fileProc = "processes.txt"
    fileFiles = "files.txt"
    #checa se teve como entrada o nome dos arquivos a serem lidos, se sim seta pra eles a leitura
    if (len(sys.argv) == 3):
        fileProc = sys.argv[1]
        fileFiles = sys.argv[2]
    #abre o arquivo a ser lido e gera um vetor de processos.
    processos = gera_processos(fileProc)
    [vetor,instructions] = gera_arquivos(fileFiles)
    disco = garq.G_Arquivos(vetor)
    print(disco)
    for processo in processos:
        instructions = processo.set_inst(instructions)
        print ("processo: {}".format(processo))
    print("instrucao sem processo para ser executada {}".format(instructions))
    g_processos = gproc.G_Processos(processos)
    tempo = 0
    while((g_processos.fora_filas or g_processos.usuario or g_processos.fila_p0 )and tempo<20 ):
        g_processos.org_filas(tempo)
        g_processos.altera_prioridade(tempo)
        print("tempo:{}\n{}".format(tempo,g_processos))
        drivers.free_drives()
        tempo+=1

    
if __name__ == '__main__':
    start()