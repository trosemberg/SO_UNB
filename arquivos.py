"""
    Classe responsavel por gerenciar os arquivos em disco
"""

class G_Arquivos:
    #init e a inicializacao do gerenciador de arquivos, onde ja inicializa com as infos passadas
    def __init__(self,vetor):
        self.blocos = []
        self.blocos_total = int(vetor[0])
        for _ in range(0,self.blocos_total):
            self.blocos.append(Arquivos())
        vetor.pop(0)
        for element in vetor:
            temp = element.split(',')
            for i in range(0,len(self.blocos)):
                pos_ini = int(temp[1])
                pos_fim = pos_ini + int(temp[2])-1
                if ((i>=pos_ini )and (i<=pos_fim)):
                    self.blocos[i].start = pos_ini
                    self.blocos[i].name = temp[0]
                    self.blocos[i].size = pos_fim-pos_ini+1
    #classe responsavel por retornar a string q sera printada caso chame print(G_Arquivos)
    def __str__(self):
        string = "MAPA DOS BLOCOS DO DISCO:\n"
        for bloco in self.blocos:
            string += str(bloco)
        string += "|"
        return string

"""
    Classe que representa um arquivo que sera armazenado em disco (G_Arquivos)
"""
class Arquivos:
    def __init__(self,creator = None):
        self.name = 0
        self.start = 0
        self.size = 0
        self.creator = creator

    def __str__(self):
        return ("|{}".format(self.name))

