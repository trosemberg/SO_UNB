import sys
import processo as gproc
import memoria as gmem
import recursos as ges
import arquivos as garq
from input_output import gera_processos,gera_arquivos, Output

"""
    Os imports estao sendo feitos como g+primeira letra do import pois e gerenciador de...
    es = entrada e saida
"""

def start():
    """
        variavel memoria e responsavel pelo gerenciamento de memoria,
        variavel drivers e responsavel pelo gerenciamento dos drivers
        variavel disco e responsavel pelo gerenciamento dos arquivos em disco
        variavel g_proc e responsavel pelo gerenciamento de processos
        variavel saida e responsavel pro printar na tela as saidas do programa
    """
    memoria = gmem.G_Memoria()
    drivers = ges.G_Drivers()
    saida = Output()
    processos = []
    fileProc = "processes.txt"
    fileFiles = "files.txt"
    #checa se teve como entrada o nome dos arquivos a serem lidos, se sim seta pra eles a leitura
    if (len(sys.argv) == 3):
        fileProc = sys.argv[1]
        fileFiles = sys.argv[2]
    #abre o arquivo a ser lido e gera um vetor de processos.
    processos = gera_processos(fileProc)
    [vetor,instructions] = gera_arquivos(fileFiles)
    disco = garq.G_Arquivos(vetor)
    for processo in processos:
        instructions = processo.set_inst(instructions)
    #cria o gerenciador de processos
    g_proc = gproc.G_Processos(processos)
    tempo = 0
    #enquanto houver processos a serem para entrarem nas filas ou processos de usuarios ou processos
    #de tempo real de tempo real sendo executados (nao precisa testar se tem processo
    # de usuario sendo executado, visto que nao tem nenhum sendo no momento da checagem) 
    while(g_proc.fora_filas or g_proc.usuario or g_proc.fila_p0 or g_proc.exec_real):
        # checa se chegou processo no tempo e encaminha a fila certa
        g_proc.org_filas(tempo)
        # altera prioridade de processos que estao esperando a muito tempo sem ser executado
        g_proc.altera_prioridade(tempo)
        #varre fila de tempo real e se for possivel alocar processo, tira da fila de tempo real
        # coloca na fila de execucao
        for processo in g_proc.fila_p0:
            if memoria.aloca_processo(processo):
                g_proc.exec_real.append(processo)
                g_proc.fila_p0 = filter(lambda x: x!= processo,g_proc.fila_p0)
                saida.print_dispatcher(processo)
        #varre fila de prioridade 1 e se for possivel alocar processo, tira da fila
        # e coloca na fila de execucao de processos de usuario        
        for processo in g_proc.fila_p1:
            if(drivers.get_drivers(processo)):
                if memoria.aloca_processo(processo):
                    g_proc.exec_user.append(processo)
                    g_proc.fila_p1 = filter(lambda x: x!= processo,g_proc.fila_p1)
                    g_proc.usuario = filter(lambda x: x!= processo,g_proc.usuario)
                    saida.print_dispatcher(processo)
        #varre fila de prioridade 2 e se for possivel alocar processo, tira da fila
        # e coloca na fila de execucao de processos de usuario 
        for processo in g_proc.fila_p2:
            if(drivers.get_drivers(processo)):
                if memoria.aloca_processo(processo):
                    g_proc.exec_user.append(processo)
                    g_proc.fila_p2 = filter(lambda x: x!= processo,g_proc.fila_p2)
                    g_proc.usuario = filter(lambda x: x!= processo,g_proc.usuario)
                    saida.print_dispatcher(processo)
        #varre fila de prioridade 3 e se for possivel alocar processo, tira da fila
        # e coloca na fila de execucao de processos de usuario 
        for processo in g_proc.fila_p3:
            if(drivers.get_drivers(processo)):
                if memoria.aloca_processo(processo):
                    g_proc.exec_user.append(processo)
                    g_proc.fila_p3 = filter(lambda x: x!= processo,g_proc.fila_p3)
                    g_proc.usuario = filter(lambda x: x!= processo,g_proc.usuario)
                    saida.print_dispatcher(processo)
        #executa as instrucoes comeca aqui
        result = ""
        for processo in g_proc.exec_real:
            processo.execucao +=1
            #so executa se tiver instrucoes a serem executadas
            if (processo.execucao<=len(processo.instruc)):
                saida.print_instructions(processo)
                result = disco.executa(processo)
                saida.log_instrucoes.append(result)
            #retira processo se ja executou as vezes necessarias
            if processo.execucao>=processo.t_proc:
                memoria.retira_processo(processo)         
        result = ""
        for processo in g_proc.exec_user:
            processo.execucao +=1
            #executa as instrucoes equivalente ao tempo de processamento
            if (processo.execucao<=len(processo.instruc)):
                saida.print_instructions(processo)
                result = disco.executa(processo)
                saida.log_instrucoes.append(result)

        #fim da execucao
        #devolve ao final da fila os processos de usuario que foram executados menos vezes do 
        #que o tempo de processamento do processo
        g_proc.limpa_fila_exec_real()
        g_proc.proc_user_fila()
        #limpa a memoria de processos de usuario
        memoria.limpa_memoria_usuario()
        #libera os drivers que foram alocados
        drivers.free_drives()
        #vai para o proximo tempo
        tempo+=1
    #printa o log de processos
    saida.print_log()
    #printa o mapa de disco
    saida.print_disco(disco)
    print("instrucao sem processo para ser executada {}".format(instructions))   
if __name__ == '__main__':
    start()