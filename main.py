import sys
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