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
        self.intruc = []
    
    def __str__(self):
        return ("t_init= {}, prio ={}, id= {}".format(self.t_init, self.prioridade,self.PID ))