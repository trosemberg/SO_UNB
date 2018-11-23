TAM_MAX = 1000


class Processos:
    def __init__(self, processo):
        self.t_init = processo[0]
        self.prioridade = processo[1]
        self.t_proc = processo[2]
        self.mem_bloc = processo[3]
        self.impressora = processo[4]
        self.scanner = processo[5]
        self.modem = processo[6]
        self.disco = processo[7]
        self.PID = None
        self.execucao = 0
        self.instruc = []
    
    def __str__(self,flag = "normal"):
        if (flag=="normal"):
            return ("t_init= {}, prio ={}," \
            "id= {} inst= {}".format(self.t_init, self.prioridade,self.PID,self.instruc ))
        elif (flag == "fila"):
            return("|id:{}".format(self.PID))

    def set_inst(self,instructions):
        rest = instructions
        for inst in instructions:
            real_inst = inst.split(',')
            if (self.PID == int(real_inst[0])):
                rest = filter(lambda x : x != inst, rest)
                if (int(real_inst[1])== 0):
                    self.instruc.append([int(real_inst[1]),real_inst[2],real_inst[3]])
                else:
                    self.instruc.append([int(real_inst[1]),real_inst[2]])
        return (rest)

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



