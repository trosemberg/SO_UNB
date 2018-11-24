"""
    Classe responsavel pelo gerenciamento dos drivers a serem utilizados
"""
class G_Drivers:
    def __init__(self):
        self.scanner = [None]
        self.impressora = [None]
        self.modem = [None]
        self.sata = [None,None]
    """
        Funcao responsavel por alocar o driver pro processo e retornar True
        caso algo tenha sido alocado que foi pedido, True se nada foi pedido pra ser
        alocado e False caso nao tenha sido possivel alocar o requisitado
    """
    def get_drivers(self,processo):
        is_driver_free = True
        if (processo.scanner == 1) and (self.scanner[0] is not None):
            is_driver_free = False
        if (processo.impressora == 1) and (self.impressora[0] is not None):
            is_driver_free = False
        if (processo.modem == 1) and (self.modem[0] is not None):
            is_driver_free = False
        if (processo.sata == 1) and (self.sata[0] is not None):
            is_driver_free = False
        if (processo.sata == 2) and (self.sata[1] is not None):
            is_driver_free = False
        if is_driver_free:
            if(processo.scanner == 1):
                self.scanner[0] = True
            if(processo.impressora == 1):
                self.impressora[0] = True
            if(processo.modem == 1):
                self.modem[0] = True
            if(processo.sata == 1):
                self.sata[0] = True
            if(processo.sata == 2):
                self.sata[1] = True
        return is_driver_free

    """
        Funcao responsavel por liberar todos os drivers , deve ser usada apos o termino do quantum
        libera todos os drivers independente do processo pois os processos de tempo_real
        nao podem acessar driver e os de usuario duram um quantum sendo usado, logo
        eles alocam, executam as instrucoes e desalocam.
    """
    def free_drives(self):
        self.scanner = [None]
        self.impressora = [None]
        self.modem = [None]
        self.sata = [None,None]
