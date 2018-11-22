import sys
# import processos as gproc
import memoria as gmem
import recursos as ges
import arquivos as garq
from input_output import gera_processos,gera_arquivos

"""
    Os imports estao sendo feitos como g+primeira letra do import pois e gerenciador de...
    es = entrada e saida
"""

def start():
    processos = []
    fileProc = "processes.txt"
    fileFiles = "files.txt"
    #checa se teve como entrada o nome dos arquivos a serem lidos, se sim seta pra eles a leitura
    if (len(sys.argv) == 3):
        fileProc = sys.argv[1]
        fileFiles = sys.argv[2]
    #abre o arquivo a ser lido e gera um vetor de processos.
    processos = gera_processos(fileProc)
    [disco,instructions] = gera_arquivos(fileFiles)
    for processo in processos:
        processo.set_inst(instructions)
        print ("processo = {}".format(processo))

    
if __name__ == '__main__':
    start()