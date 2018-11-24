REAL_SIZE = 64
USER_SIZE = 960

class G_Memoria:
    def __init__(self):
        self.memoria = [0 for _ in range(0, REAL_SIZE+USER_SIZE)]

    def aloca_processo(self,processo):
        livre = 0
        if (processo.prioridade == 0):
            inicio = 0
            fim = REAL_SIZE
        else:
            inicio = REAL_SIZE
            fim = REAL_SIZE+USER_SIZE
        for i in range(inicio,fim):
            if(self.memoria[i] == 0):
                livre +=1
                if(livre == processo.mem_bloc):
                    processo.pos = i- processo.mem_bloc + 1
                    self.memoria[processo.pos:processo.pos + livre] = livre * [processo.PID]
                    return True
            else:
                livre = 0
        return False
            
    def retira_processo(self,processo):
        self.memoria[processo.pos:processo.pos + processo.mem_bloc] = [0]*processo.mem_bloc


    def limpa_memoria_usuario(self,processo):
        self.memoria[REAL_SIZE:] =  USER_SIZE * [0]
    