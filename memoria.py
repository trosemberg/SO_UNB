REAL_SIZE = 64
USER_SIZE = 960

class G_Memoria:
    def __init__(self):
        self.memoria = [0 for _ in range(0, REAL_SIZE+USER_SIZE)]
    def aloca_processo(self,processo):
    
    # def retira_processo(self,processo):
    
    def limpa_memoria_usuario(self,processo):
        self.memoria[REAL_SIZE:] =  USER_SIZE * [0]
    