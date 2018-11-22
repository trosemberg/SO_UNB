class G_Arquivos:
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

    def __str__(self):
        string = ""
        for bloco in self.blocos:
            string = string + str(bloco)
        return string


class Arquivos:
    def __init__(self,creator = None):
        self.name = ""
        self.start = 0
        self.size = 0
        self.creator = creator

    def __str__(self):
        return ("name={},start={},size={}  ".format(self.name,self.start,self.size))

