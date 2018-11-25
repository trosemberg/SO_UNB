REAL_SIZE = 64
USER_SIZE = 960
"""
    Unidade responsavel pelo gerenciamento da memoria 
"""
class G_Memoria:
    def __init__(self):
        self.memoria = [None for _ in range(0, REAL_SIZE+USER_SIZE)]
    """
        aloca o processo na parte correta da memoria e retorna True se foi possivel alocar e
        False se nao foi possivel alocar
    """
    def aloca_processo(self,processo):
        livre = 0
        if (processo.prioridade == 0):
            inicio = 0
            fim = REAL_SIZE
        else:
            inicio = REAL_SIZE
            fim = REAL_SIZE+USER_SIZE
        for i in range(inicio,fim):
            if(self.memoria[i] == None):
                livre +=1
                if(livre == processo.mem_bloc):
                    processo.pos = i- processo.mem_bloc + 1
                    self.memoria[processo.pos:processo.pos + livre] = livre * [processo.PID]
                    return True
            else:
                livre = 0
        return False
    """
        Funcao responsavel por retirar o processo que 
        ja tiver terminado
    """     
    def retira_processo(self,processo):
        self.memoria[processo.pos:processo.pos + processo.mem_bloc] = [None]*processo.mem_bloc

    """
        Funcao responsavel por limpar a memoria de usuario 
    """
    def limpa_memoria_usuario(self):
        self.memoria[REAL_SIZE:] =  USER_SIZE * [None]
    