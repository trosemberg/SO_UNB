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
    
    def __str__(self):
        return ("t_init= {}, prio ={}," \
        "id= {} inst= {}".format(self.t_init, self.prioridade,self.PID,self.instruc ))

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