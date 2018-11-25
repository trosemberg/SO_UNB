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
        string = "MAPA DOS BLOCOS DO DISCO:\n\t"
        for bloco in self.blocos:
            string += str(bloco)
        string += "|"
        return string

    def executa(self,processo):
        string = ""
        livre = 0
        if processo.execucao <=len(processo.instruc):
            operacao = processo.instruc[processo.execucao -1][0]
            nome_arq = processo.instruc[processo.execucao -1][1]
            #op 0 = criar op 1 = deletar
            if operacao == 0:
                tamanho_arq = processo.instruc[processo.execucao -1][2]
                for i in range(0,self.blocos_total):
                    if(self.blocos[i].name==0):
                        livre +=1
                        if livre == tamanho_arq:
                            pos = i-tamanho_arq+1
                            self.blocos[pos:i+1] = livre * [Arquivos(nome_arq,pos,tamanho_arq,processo.PID)]
                            string = "Sucesso!\n"
                            string += "O processo {} criou o arquivo {}".format(processo.PID,nome_arq)
                            string += "(do bloco {} a {}).".format(pos,pos+tamanho_arq-1)
                            break
                    else: 
                        livre = 0
                        string = "Falha!\n"
                        string += "O processo {} ".format(processo.PID)
                        string += "nao pode criar o arquivo {} (falta de espaco).".format(nome_arq)
                return string
            elif operacao == 1:
                for i in range(0,self.blocos_total):
                    if(self.blocos[i].name == nome_arq):
                        if((processo.PID == self.blocos[i].creator) or processo.prioridade == 0):
                            size = self.blocos[i].size
                            self.blocos[i:i+size] = size*[Arquivos()]
                            string = "Sucesso!\n"
                            string += "O processo {} deletou o arquivo {}.".format(processo.PID,nome_arq)
                            break
                        else:
                            string = "Falha!\n"
                            string+= "O processo {} nao pode deletar o arquivo {}".format(processo.PID,nome_arq)
                    else:
                        string = "Falha!\n"
                        string += "Nao existe o arquivo {}".format(nome_arq)
                return string
            else:
                return "Operacao nao existente"
        else:
            return processo.PID


"""
    Classe que representa um arquivo que sera armazenado em disco (G_Arquivos)
"""
class Arquivos:
    def __init__(self,nome = 0,start = 0,size = 0, creator = None ):
        self.name = nome
        self.start = start
        self.size = size
        self.creator = creator

    def __str__(self):
        return ("| {} ".format(self.name))

