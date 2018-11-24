TAM_MAX = 1000

"""
    Responsavel pela parte de Processos
"""
class Processos:
    def __init__(self, processo):
        self.t_init = processo[0]
        self.prioridade = processo[1]
        self.t_proc = processo[2]
        self.mem_bloc = processo[3]
        self.impressora = processo[4]
        self.scanner = processo[5]
        self.modem = processo[6]
        self.sata = processo[7]
        self.PID = None
        self.pos = None
        self.execucao = 0
        self.prio_changed = False
        self.instruc = []
    
    def __str__(self,flag = "normal"):
        if (flag=="normal"):
            return ("t_init= {}, prio ={}," \
            "id= {} inst= {}".format(self.t_init, self.prioridade,self.PID,self.instruc ))
        elif (flag == "fila"):
            return("|id:{}".format(self.PID))
    """
        Responsavel por receber o vetor de instrucoes  num formato de string
        e associar corretamente ao processo do qual ele vem
        o formato do vetor instrucoes ficou como exemplo
        [[0,'B',2],[0,'D',3]]
    """
    def set_inst(self,instructions):
        rest = instructions
        for inst in instructions:
            real_inst = inst.split(',')
            if (self.PID == int(real_inst[0])):
                rest = filter(lambda x : x != inst, rest)
                if (int(real_inst[1])== 0):
                    self.instruc.append([int(real_inst[1]),real_inst[2][1],int(real_inst[3])])
                else:
                    self.instruc.append([int(real_inst[1]),real_inst[2][1]])
        return (rest)

"""
    Responsavel pelo gerenciamento de processos
"""

class G_Processos:
    def __init__(self, processos):
        self.fila_p0 = []
        self.fila_p1 = []
        self.fila_p2 = []
        self.fila_p3 = []
        self.usuario = []
        self.fora_filas = processos
        self.execu = []

    def __str__(self):
        string = ""
        string+= "p0:"
        for processo in self.fila_p0:
            string += str(processo.__str__("fila"))
        string+="\n"
        string+= "p1:"
        for processo in self.fila_p1:
            string += str(processo.__str__("fila"))
        string+="\n"
        string+= "p2:"
        for processo in self.fila_p2:
            string += str(processo.__str__("fila"))
        string+="\n"
        string+= "p3:"
        for processo in self.fila_p3:
            string += str(processo.__str__("fila"))
        string+="\n"
        string+= "fora:"
        for processo in self.fora_filas:
            string += str(processo.__str__("fila"))
        string+="\n"
        return string
    """
        Responsavel por organizar as filas, setando para os lugares certos os processos
    """
    def org_filas(self,tempo):
        for processo in self.fora_filas:
            if(len(self.fila_p0)+len(self.usuario) >=1000):
                break
            if ((processo.t_init<= tempo)):
                if(processo.prioridade == 0):
                    self.fila_p0.append(processo)
                    self.fora_filas = filter(lambda x : x != processo,self.fora_filas)
                if(processo.prioridade == 1):
                    self.fila_p1.append(processo)
                    self.usuario.append(processo)
                    self.fora_filas = filter(lambda x : x != processo,self.fora_filas)
                if(processo.prioridade == 2):
                    self.fila_p2.append(processo)
                    self.usuario.append(processo)
                    self.fora_filas = filter(lambda x : x != processo,self.fora_filas)
                if(processo.prioridade == 3):
                    self.fila_p3.append(processo)
                    self.usuario.append(processo)
                    self.fora_filas = filter(lambda x : x != processo,self.fora_filas)
    """
        Altera a prioridade dos processos que estiverem a 10 unidades de tempo esperando 
        sem nunca terem sidos executados
    """
    def altera_prioridade(self,tempo):
        for processo in self.fila_p2:
            if((processo.execucao == 0) and (processo.t_init + 9 < tempo) and (not processo.prio_changed)):
                self.fila_p2 = filter(lambda x : x != processo, self.fila_p2) 
                processo.prio_changed = True
                self.fila_p1.append(processo)
            elif((processo.execucao == 0) and (processo.t_init + 19 < tempo) and (processo.prio_changed)):
                self.fila_p2 = filter(lambda x : x != processo, self.fila_p2) 
                self.fila_p1.append(processo)
        for processo in self.fila_p3:
            if((processo.execucao == 0) and (processo.t_init + 9 < tempo) and (not processo.prio_changed)):
                self.fila_p3 = filter(lambda x : x != processo, self.fila_p3)
                processo.prio_changed = True 
                self.fila_p2.append(processo)