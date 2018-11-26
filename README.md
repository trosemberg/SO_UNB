# SO_UNB

Trabalho de Sistemas Operacionais

Prof Aletéia UNB 2/2018

**Tomás Rosário Rosemberg 14/0087567**

**Kevin Masinda 13/0058866**

**Hichemm Khalyd 12/0012928**

## Especificações do Projeto a seguir:

&nbsp;&nbsp;&nbsp;&nbsp;O projeto especifica o quantum do trabalho como sendo de **1(UM)**
desta forma, a cada iteração as seguintes coisas devem ocorrer, checa se lista de processos está
lotada (1000 processos), se  não estiver e estiver processos para entrar(tempo de inicialização
menor ou igual ao tempo atual, colocar do menor tempo de inicialização para o maior) na lista
colocar ele no final da fila de prioridade adequada, se estiver lotada continua o código.

&nbsp;&nbsp;&nbsp;&nbsp;Após a checagem, coloca os processos que forem possiveis na memória,
checando a possibilidade de entrarem na memória a disponibilidade de drivers de IO,
caso o processo esteja na fila e não caiba na memória ou o IO esta ocupado, passa para checar o
próximo e mantém ele na mesma posição, desta forma não temos que nos preocupar com bloqueio de processo nem
nada do genêro.

&nbsp;&nbsp;&nbsp;&nbsp;Execute os processos todos após alocar todos os possiveis em memória.

&nbsp;&nbsp;&nbsp;&nbsp;Cheque se algum processo terminou a execução, se sim acabe com ele.
Os processos que ainda restarem execuções a serem feitas retornam ao final da sua devida fila de
prioridade e depois incrementa-se o tempo. Repete-se tudo.

Trabalho realizado com exito, professora gostou muito e disse que estava tudo certo
postarei depois a nota recebida pelo trabalho



 
