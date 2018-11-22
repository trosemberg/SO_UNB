import sys
import processos as gproc
import memoria as gmem
import es as ges
import arquivos as garq
"""
    Os imports estão sendo feitos como g+primeira letra do import pois é gerenciador de...
    es = entrada e saida
"""

def start():
    fileProc = "processes.txt"
    fileFiles = "files.txt"
    if (len(sys.argv) == 3):
        fileProc = sys.argv[1]
        fileFiles = sys.argv[2]
    process = open(fileProc,"r")
    files = open(fileFiles, "r")
    
if __name__ == '__main__':
    start()