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
    memoria = gmem.G_Memoria()
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
    while(tempo < 15):
        g_processos.org_filas(tempo)
        print("tempo:{}\n{}".format(tempo,g_processos))
        tempo+=1

    
if __name__ == '__main__':
    start()