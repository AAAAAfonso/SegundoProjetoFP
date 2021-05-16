#Afonso Freitas | 99173
def acumula (fn, lst):
    ##funcao x lista --> universal 
    """
    Devolve um valor resultante da acumulacao de todos os elementos de uma lista
    a acumulacao e defenida com base base no argumento fn
    """
    if lst == []:
        raise ValueError('acumula: lista vazia')
    else:
        res = lst[0]
        for i in range(1,len(lst)):
            res = fn(res, lst[i])
        return res
    
#R[posicao] = [0 < int < 10] 
def cria_posicao(c,l):
    ##str x str --> posicao 
    """
    recebe duas cadeias de carateres correspondentes a coluna c e 
    a linha de uma posicao e devolve a posicao correspondente.  
    A funcao cria_posicao verifica a validade dos seus argumentos,
    gerando um ValueError com a mensagem
    'criaposicao: argumentos invalidos' caso os seus argumentos
    nao sejam validos.
    """
    if c not in ('a','b','c') or l not in ('1','2','3'):
        raise ValueError ('cria_posicao: argumentos invalidos')
    c = ('a','b','c').index(c)
    l = ('1','2','3').index(l)
    return [c+1 + l*3]
     
def cria_copia_posicao(p):
    ##posicao --> posicao
    """
    recebe uma posicao e devolve uma copia nova da posicao.
    """
    return list(p)

def obter_pos_c(p):
    ##posicao --> str
    """
    devolve a componente coluna da posicao p.
    """
    return ('a','b','c')[(p[0]-1)%3]

def obter_pos_l(p):
    ##posicao --> str
    """
    devolve a componente linha da posicao p.
    """
    return ('1','2','3')[(p[0]-1)//3]

def eh_posicao(p):
    ##universal --> booleano
    """
    devolve True caso o seu argumento seja um TAD posicao e False caso
    contrario.
    """
    return type(p) == list and len(p) == 1 and type(p[0]) == int and 0<p[0]<10

def posicoes_iguais(p1,p2):
    ##posicao x posicao --> booleano
    """
    devolve True caso os seus argumentos sejam TAD's posicoes iguais e False
    caso contrario.
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2 

def posicao_para_str(p):
    ##posicao --> str
    """
    devolve uma representacao na forma ab onde 'a' corresponde componente 
    coluna da posicao p e 'b' a componente linha da posicao p.
    """
    return obter_pos_c(p) + obter_pos_l(p)          
           
def obter_posicoes_adjacentes(p):
    ##posicao --> tuplo de posicoes
    """
    devolve um tuplo com as posicoes adjacentes a posicao p
    de acordo com a ordem de leitura do tabuleiro.
    """
    adjacentes_laterais_v = adjacentes_laterais(p)              #coloca em adjacentes_laterais as posicoes a esquerda e direita de p
    adjacentes_verticais_v = adjacentes_verticais(p)            #coloca em adjacentes_verticais as posicoes a cima e a baixo de p
    adjacentes = adjacentes_laterais_v + adjacentes_verticais_v #coloca em adjacentes as adjacentes_laterais e adjacentes_verticais
     
    if (('a','b','c').index(obter_pos_c(p))%2 == 0\
    and ('1','2','3').index(obter_pos_l(p))%2 == 0) or\
    posicoes_iguais(p,cria_posicao('b','2')):                   #se a posicao p for um canto ou o centro executa o codigo abaixo
        if posicoes_iguais(p,cria_posicao('b','2')):
            adjacentes = adjacentes +\
            [cria_posicao('a','1'),cria_posicao('c','1'),\
            cria_posicao('a','3'),cria_posicao('c','3')]        #se a posicao p for o centro adiciona a variavel adjacentes todos os cantos 
            
        else:
            adjacentes = adjacentes + \
            [cria_posicao('b','2')]                             #senao adiciona a adjacentes a posicao central 
            
    lista_res = ordena_posicoes(adjacentes)                     
    return tuple(lista_res)                                     #ordena a lista de posicoes adjacentes e devolve o tuplo da lista equivalente 

def adjacentes_laterais(p):
    ##posicao --> lista de posicoes
    """
    devolve as adjacentes laterais de uma poiscao
    """
    lat = ('a','b','c').index(obter_pos_c(p))
    
    if lat == 0:
        return [cria_posicao(('a','b','c')\
        [lat + 1],obter_pos_l(p))]
              
    if lat == 2:
        return [cria_posicao(('a','b','c')\
        [lat - 1],obter_pos_l(p))]
    
    else:
        return [cria_posicao(('a','b','c')[lat - 1],\
        obter_pos_l(p)),cria_posicao(('a','b','c')[lat + 1],\
        obter_pos_l(p))]
    
def adjacentes_verticais(p):
    ##posicao --> lista de posicoes
    """
    devolve as adjacentes verticais de uma poiscao
    """
    vet = ('1','2','3').index(obter_pos_l(p))
    
    if vet == 0:
        return [cria_posicao(obter_pos_c(p),('1','2','3')[vet + 1])]   
           
    if vet == 2:
        return [cria_posicao(obter_pos_c(p),('1','2','3')[vet - 1])]
    
    else:
        return [cria_posicao(obter_pos_c(p),\
        ('1','2','3')[vet - 1]),cria_posicao(obter_pos_c(p),\
        ('1','2','3')[vet + 1])]
    
def ordena_posicoes(lst_p):
    ##lista de poiscoes --> lista de posicoes
    """
    devolve o transformado da lista de posicoes lst_p ordenado com base na
    ordem de leitura do tabuleiro
    """
    nao_ordenado = 1 
    while nao_ordenado != 0:  #variavel de controlo que indica se a lista esta ordenada
        nao_ordenado = 0
        if len(lst_p) > 1:
            for r in range(len(lst_p)-1):
                if ord(obter_pos_l(lst_p[r])) > ord(obter_pos_l(lst_p[r+1]))\
                or (ord(obter_pos_l(lst_p[r])) == ord(obter_pos_l(lst_p[r+1]))\
                and ord(obter_pos_c(lst_p[r])) > ord(obter_pos_c(lst_p[r+1]))): # se entre duas posicoes, 2 linhas nao estam ordenadas ou 
                    lst_p[r],lst_p[r+1] = lst_p[r+1],lst_p[r]                   # 2 linhas estam ordenadas mas nao as colunas entao
                    nao_ordenado = 1                                            # essas trocam de posicoes e altera-se o nao_oredenado para 1               
    return lst_p

def todas_as_posicoes():
    ##{} --> tuplo de posicoes
    """
    devolve todas as posicoes num tuplo.
    """
    res = ()
    for posicao in ('1','2','3'):
        for posicao2 in ('a','b','c'):
            cria = cria_posicao(posicao2,posicao)
            res += (cria,)      
    return res

#R[peca] = [str in ('X','O',' ')]
def cria_peca(s):
    ##str --> peca
    """
    recebe uma cadeia de carateres correspondente ao identificador de um dos
    dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a peca
    correspondente. O  construtor  verifica  a  validade  dos  seus  argumentos,
    gerando um ValueError com a mensagem 'cria_peca: argumento invalido' caso
    o seu argumento nao seja valido.
    """
    if type(s) != str or len(s) != 1 or s not in ('X','O',' '):
        raise ValueError ('cria_peca: argumento invalido')
    
    else:
        return [s]

def cria_copia_peca(j):
    ##peca --> peca
    """
    recebe uma peca j e devolve uma copia nova da peca j.
    """
    return list(j)

def eh_peca(j):
    ##universal --> booleano
    """
    devolve True caso o seu argumento seja um TAD peca e False caso contrario.
    """
    return type(j) == list and len(j) == 1 and j[0] in ('X','O',' ')

def pecas_iguais(j1,j2):
    ##peca x peca --> booleano
    """
    devolve True apenas se p1 e p2 sao pecas e sao iguais.
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

def peca_para_str(j):
    ##peca --> str
    """
    devolve a cadeia de caracteres que representa o jogador dono da peca, isto
    e, '[X]', '[O]' ou '[ ]'.
    """
    return '['+j[0] +']'

def peca_para_inteiro(j):
    ##peca --> int
    """
    devolve um inteiro valor 1, -1 ou 0, dependendo se a peca e do jogador 'X',
    'O' ou livre, respetivamente.
    """
    return 1 if peca_para_str(j) == '[X]'\
    else -1 if peca_para_str(j) == '[O]' \
    else 0 
    
def conta_peca(tup,peca):
    ##tuplo/lista de pecas x peca --> inteiro
    """
    recebe um tuplo de pecas ou uma lista de pecas e uma peca peca e 
    conta quantas vezes a peca aparece no tuplo ou lista
    """
    cp = 0
    for pe in tup:
        if pecas_iguais(pe,peca): #analisa se cada posicao do tuplo e igual a peca dada se sim incrementa a variavel cp (inicialmente a zero)
            cp += 1
    return cp

#R[tabuleiro] = [peca]*9 
def cria_tabuleiro():
    ## {} --> tabuleiro
    """
    devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes ocupadas 
    por pecas de jogador
    """
    return [cria_peca(' ')]*9

def cria_copia_tabuleiro(t):
    ## tabuleiro --> tabuleiro
    """
    recebe um tabuleiro e devolve uma copia nova do tabuleiro.
    """
    return list(t)

def obter_peca(t,p):
    ## tabuleiro x posicao --> peca
    """
    devolve a peca na posicao p do tabuleiro. Se a posicao nao estiver ocupada,
    devolve uma peca livre.
    """
    return t[posicao_para_ind(p)]

def obter_vetor(t,vetor):
    ## tabuleiro x str --> tuplo de pecas
    """
    devolve todas as pecas da linha ou coluna especificada pelo seu argumento.
    """
    if vetor in ('1','2','3'): #obtem uma coluna no caso do argumento vetor corresponda a uma coluna
        return tuple(t[('1','2','3').index(vetor)*3:\
        ('1','2','3').index(vetor)*3+3])
    
    else:                      #obtem uma linha no caso do argumento vetor nao corresponda a uma coluna
        return (t[('a','b','c').index(vetor)],\
        t[('a','b','c').index(vetor)+3],\
        t[('a','b','c').index(vetor)+6])

def coloca_peca(t,j,p):
    ## tabuleiro x peca x posicao --> tabuleiro
    """
    modifica destrutivamente o tabuleiro t colocando a peca j na posicao p, 
    e devolve o proprio tabuleiro.
    """
    t[posicao_para_ind(p)] = j
    return t

def remove_peca(t,p):
    ## tabuleiro x posicao --> tabuleiro
    """
    modifica destrutivamente o tabuleiro t removendo a peca da posicao p, e
    devolve o proprio tabuleiro.
    """
    return coloca_peca(t,cria_peca(' '),p)
    
def move_peca(t,p1,p2):
    ##tabuleiro x posicao x posicao --> tabuleiro
    """
    modifica destrutivamente o tabuleiro t movendo a peca que se encontra na
    posicao p1 para a posicao p2, e devolve o proprio tabuleiro.
    """
    j_nova = cria_copia_peca(obter_peca(t,p1))
    remove_peca(t,p1)
    return coloca_peca(t,j_nova,p2)

def ha_mais_X_dq_O(u):
    ##universal --> booleano
    """
    verifica se a quantidade de pecas e a forma como essas estao distribuidas
    numa lista forma um tabuleiro valido do jogo do moinho
    """
    if list(filter(lambda x: eh_peca(x),u)) == u:
        pO = conta_peca(u,cria_peca('O'))
        pX = conta_peca(u,cria_peca('X'))
        q_de_p = abs(pX - pO) <= 1 and pX <=3 and pO <= 3
        if pX ==3 and pO == 3:
            return q_de_p and menos_2_vencedores(u)
        return q_de_p
    else: 
        return False
        

def menos_2_vencedores(t):
    #lista de pecas --> booleano
    """
    Retorna False caso num possivel tabuleiro valido existam dois 
    vencedores possiveis e True caso caso contrario
    """
    res = 0
    for i in range(6):                                       
        t_vetor = obter_vetor(t,('a','b','c','1','2','3')[i])
        if pecas_iguais((t_vetor[0]),(t_vetor[1])) \
        and pecas_iguais((t_vetor[2]),(t_vetor[1])) \
        and not pecas_iguais((t_vetor[0]),cria_peca(' ')):   #verifica se algum dos vetores apresenta um ganhador
            res += 1
    return res <2
    
    
def eh_tabuleiro(t):
    ##universal --> booleano
    """
    devolve True caso o seu argumento seja um TAD tabuleiro e False caso
    contrario. Um tabuleiro valido pode ter um maximo de 3 pecas de cada
    jogador, nao pode conter mais de 1 peca mais de um jogador que do contrario,
    e apenas pode haver um ganhador em simultaneo.
    """
    return type(t) == list and len(t) == 9 and ha_mais_X_dq_O(t)
    
def eh_posicao_livre(t,p):
    ##tabuleiro X posicao --> booleano
    """
    devolve True apenas no caso da posicao p do tabuleiro corresponder a uma
    posicao livre.
    """
    return pecas_iguais(t[posicao_para_ind(p)],cria_peca(' '))

def iguais_tab(t1,t2):
    ##tabuleiro X tabuleiro --> booleano
    """
    verifica se em 2 tabuleiros todas as mesmas posicoes tem a mesma peca.
    Se isso se verificar devolve True senao devolve False
    """
    for pe in range(9):
        if not pecas_iguais(t1[pe],t2[pe]):
            return False
    return True

def tabuleiros_iguais(t1,t2):
    ##tabuleiro X tabuleiro --> booleano
    """
    devolve True apenas se t1 e t2 sao tabuleiros e sao iguais
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and iguais_tab(t1,t2) 

def tabuleiro_para_str(t):
    ##tabuleiro --> str
    """
    devolve uma str que representa o tabuleiro graficamente
    """
    return '   a   b   c\n1 '+\
    peca_para_str(obter_peca(t,cria_posicao('a','1')))\
    +'-'+peca_para_str(obter_peca(t,cria_posicao('b','1')))\
    +'-'+peca_para_str(obter_peca(t,cria_posicao('c','1')))\
    +'\n   | \\ | / |\n2 '+\
    peca_para_str(obter_peca(t,cria_posicao('a','2')))\
    +'-'+peca_para_str(obter_peca(t,cria_posicao('b','2')))\
    +'-'+peca_para_str(obter_peca(t,cria_posicao('c','2')))\
    +'\n   | / | \\ |\n3 '+\
    peca_para_str(obter_peca(t,cria_posicao('a','3')))\
    +'-'+peca_para_str(obter_peca(t,cria_posicao('b','3')))\
    +'-'+peca_para_str(obter_peca(t,cria_posicao('c','3')))

def tuplo_para_tabuleiro(tup):
    ##tuplo --> tabuleiro
    """
    devolve o tabuleiro que e representado  pelo tuplo tup com 3 tuplos, cada um
    deles contendo 3 valores inteiros iguais a 1, -1 ou 0,tal como no primeiro
    projeto, senao retorna o tuplo
    """
    if len(tup) == len(tup[0])==len(tup[1])==len(tup[2])==3:
        return [inteiro_para_peca(tup[0][0]),\
                inteiro_para_peca(tup[0][1]),\
                inteiro_para_peca(tup[0][2]),\
                inteiro_para_peca(tup[1][0]),\
                inteiro_para_peca(tup[1][1]),\
                inteiro_para_peca(tup[1][2]),\
                inteiro_para_peca(tup[2][0]),\
                inteiro_para_peca(tup[2][1]),\
                inteiro_para_peca(tup[2][2])]  
    else:
        return tup

def posicao_para_ind(p):
    ##posicao --> inteiro
    """
    transforma uma posicao em inteiro, esse inteiro representa
    o indice na representacao interna do tabuleiro
    """
    c = ('a','b','c').index(obter_pos_c(p))
    l = ('1','2','3').index(obter_pos_l(p))
    return c + l*3

def obter_ganhador(t):
    ##tabuleiro --> peca
    """
    devolve uma peca do jogador que tenha as suas 3 pecas em linha na vertical
    ou na horizontal no tabuleiro. Se nao existir nenhum ganhador, devolve uma
    peca livre
    """
    for i in range(3):                           
        #precorre todos os vetores do tabuleiro
        t_c = obter_vetor(t,('a','b','c')[i])
        t_l = obter_vetor(t,('1','2','3')[i])
        
        if pecas_iguais((t_c[0]),(t_c[1])) and pecas_iguais((t_c[2]),(t_c[1]))\
        and not pecas_iguais((t_c[0]),cria_peca(' ')):   #verifica se numa coluna todos os elementos sao iguais e diferentes de uma posicao livre
            return cria_copia_peca(t_c[0])
        
        if pecas_iguais((t_l[0]),(t_l[1])) and pecas_iguais((t_l[2]),(t_l[1]))\
        and not pecas_iguais((t_l[0]),cria_peca(' ')):   #verifica se numa linha todos os elementos sao iguais e diferentes de uma posicao livre
            return cria_copia_peca(t_l[0])
        
    return cria_peca(' ')                                #se nao exister ganhador devolve uma peca livre
        
def obter_posicoes_livres(t):
    ##tabuleiro --> tuplo de posicoes
    """
    devolve um tuplo com as posicoes nao ocupadas pelas pecas de qualquer um dos
    dois jogadores na ordem de leitura do tabuleiro.
    """
    res = ()
    todas_p = todas_as_posicoes()
    for p in todas_p:
        if eh_posicao_livre(t,p):    #verifica se em cada posicao do tabuleiro existe uma posicao livre, se sim adiciona a uma variavel res
            res = res + (p,)   
    return res

def obter_posicoes_jogador(t, j):
    ##tabuleiro x peca --> tuplo de posicoes
    """
    devolve um tuplo com as posicoes ocupadas pelas pecas j de um dos dois
    jogadores na ordem de leitura do tabuleiro.
    """
    res = ()
    todas_p = todas_as_posicoes()
    for p in todas_p:
        if pecas_iguais(obter_peca(t,p),j) and\
        not pecas_iguais(j,cria_peca(' ')):  #verifica se em cada posicao do tabuleiro existe uma posicao correspondete a peca j, se sim adiciona a variavel res
            res = res + (p,)
    return res

def posicao_nao_adjacente(p1,p2):
    ##posicao x posicao --> booleano
    """
    devolve True caso a posicao p2 e uma adjacente de p1 e False caso contrario
    """
    for pa in obter_posicoes_adjacentes(p1):
        if posicoes_iguais(pa,p2):
            return True
    return False 

def posicoes_jogaveis(t,j):
    ##tabuleiro x peca --> lista de posicoes
    """
    devolve uma lista com todas as posicoes onde possa exisitir um 
    destino de um movimento de um jogador j num tabuleiro t
    """
    return list(filter(lambda x :eh_posicao_livre(t,x),acumula(lambda x,y: x+y,\
    [obter_posicoes_adjacentes(i) for i in obter_posicoes_jogador(t,j)])))
    
def obter_movimento_aux(t,j):
    ##tabuleiro x peca --> tuplo de posicoes
    """
    funcao auxiliar que recebe um tabuleiro e uma peca de um jogador, e devolve
    duas posicoes que representam um movimento introduzido manualmente pelo
    jogador.  
    e executa ValueError 'obter_movimento_manual: escolha invalida' se o input
    introduzido nao for valido
    """
    l= str(input('Turno do jogador. Escolha um movimento: ')) 
    if len(l)!= 4 or l[0] not in ('a','b','c') or l[2] not in ('a','b','c') \
    or l[1] not in ('1','2','3') or l[3] not in ('1','2','3'):  #verifica se o movimento introduzido pelo jogador, corresponde a
                                                                #um jogavel na fase de movimentos das pecas com base no tabuleiro e no input
        raise ValueError('obter_movimento_manual: escolha invalida')        
    l = (l[0:2],l[2:4])
    a = str_para_posicao(l[0])
    b = str_para_posicao(l[1])
    if posicoes_jogaveis(t,j):                                  #se for possivel movimentar uma peca executa o codigo abaixo
        if not eh_posicao_livre(t,b) or not pecas_iguais(obter_peca(t,a),j) or\
        not posicao_nao_adjacente(a,b):
            raise ValueError('obter_movimento_manual: escolha invalida')
        else:
            return (a,b)
    else:                                                        #senao verifica se o input introduzido e o pretendido
        if posicoes_iguais(a,b) and pecas_iguais(obter_peca(t,a),j):
            return (a,b)
        else:
            raise ValueError('obter_movimento_manual: escolha invalida')
        
def obter_movimento_manual(t,j):
    ##tabuleiro x peca --> tuplo de posicoes
    """
    recebe  um  tabuleiro e uma peca de um jogador, e devolve um tuplo com uma
    ou duas posicoes que representam uma posicao ou um movimento introduzido
    manualmente pelo jogador.  
    """
    pl = obter_posicoes_livres(t)
    if len(pl) == 3: #se o tabuleiro se encontrar na fase de movimento executa a funcao auxiliar obter_movimento_aux
        vetor_pos = obter_movimento_aux(t,j)
        return vetor_pos
    else:            #senao verifica se a posicao introduzida pelo jogador corresponde a uma jogavel na fase de colocacao e 
                     #se possivel retorna o um tuplo com indice unico com o transformado do input em posicao
        l= str(input('Turno do jogador. Escolha uma posicao: '))
        if len(l) == 2 and l[0] in ('a','b','c') and l[1] in ('1','2','3')\
        and eh_posicao_livre(t,str_para_posicao(l)):
            return(str_para_posicao(l),)
        else:
            raise ValueError('obter_movimento_manual: escolha invalida')
        
def inteiro_para_peca(p_int):
    ##inteiro --> peca
    """
    recebe um argumento universal e se o argumento for 1, -1 ou 0 transforma
    numa peca, senao retorna o argumento    
    """
    return cria_peca((' ','X','O')[p_int]) \
    if type(p_int) == int and p_int in (1,-1,0) else p_int

def facil(t,j):
    ##tabuleiro x peca --> tuplo de posicoes
    """
    funcao auxiliar recebe um tabuleiro e uma peca e devolve a posicao a
    movimentar (que ocupa a primeira posicao em ordem de leitura do tabuleiro)
    que tenha alguma posicao adjacente livre. A posicao de destino e a 
    primeira posicao adjacente livre (em ordem de leitura do tabuleiro)
    """
    for posicao in obter_posicoes_jogador(t,j):
        for posicao2 in obter_posicoes_adjacentes(posicao): 
            if eh_posicao_livre(t,posicao2):
                return posicao,posicao2
               
def index_peca_vazia(tup):
    ##tuplo de peca ou lista de pecas --> inteiro
    """
    devolve o indice de uma peca livre num tuplo/lista de pecas
    """
    ind = 0
    for peca in tup:
        if pecas_iguais(peca,cria_peca(' ')):    #precorre todos os indices de um tuplo/lista e devolve a primeira posicoes com peca livre
            return ind
        else:
            ind += 1                          
    raise ValueError('index_peca_vazia: argumentos invalidos')
                
def vitoria(t,j):
    ##tabuleiro x peca --> posicao
    """
    recebe um tabuleiro t e uma peca j e devolve a posicao livre caso seja
    possivel uma vitoria na jogada seguinte    
    """
    lst = []
    for i in range(0,3):
        coluna = obter_vetor(t,('a','b','c')[i])  #obtem todas as colunas possiveis         
        if conta_peca(coluna,j) == 2 and conta_peca(coluna,cria_peca(' ')) == 1:#se em uma dessas colunas existerem duas posicoes com a peca representativa
                                                                                #do jogador j e uma posicao livre adiciona a lista, a posicao livre
            lst = [cria_posicao(('a','b','c')[i],\
            ('1','2','3')[index_peca_vazia(coluna)])] + lst 
                  
        linha = obter_vetor(t,('1','2','3')[i])   #obtem todas as linhas possiveis
        if conta_peca(linha,j) == 2 and conta_peca(linha,cria_peca(' ')) == 1:   #se em uma dessas linhas existerem duas posicoes com a peca representativa
                                                                                 #do jogador j e uma posicao livre adiciona a lista, a posicao livre 
            lst =  [cria_posicao(('a','b','c')[index_peca_vazia(linha)],\
            ('1','2','3')[i])] + lst   
               
    return  ordena_posicoes(lst)

def centro_canto_lateral(t):
    ##tabuleiro --> posicao
    """
    recebe um tabuleiro t e devolve uma posicao livre, respeitando a
    ordem de leitura do tabuleiro e a de jogada(centro, canto e lateral)    
    """
    if eh_posicao_livre(t,cria_posicao('b','2')):
        return cria_posicao('b','2') #se o centro estiver livre, retorna a sua posicao
                     
    for pos in (cria_posicao('a','1'),cria_posicao('c','1'),\
                cria_posicao('a','3'),cria_posicao('c','3')):                    
        if eh_posicao_livre(t,pos): 
            return pos               #se algum dos cantos estiver livre, retorna a sua posicao
                   
    for pos2 in (cria_posicao('b','1'),cria_posicao('a','2'),\
                 cria_posicao('c','2'),cria_posicao('b','3')):
        if eh_posicao_livre(t,pos): 
            return pos               #se alguma das laterais estiver livre, retorna a sua posicao
        
def posicao_auto_sem_mov(t,j):
    ##tabuleiro x peca --> posicao
    """
    recebe um tabuleiro t e uma peca j correspondente ao jogador j e devolve
    a melhor jogada na fase de colocao de peca no jogo do moinho
    """ 
    if vitoria(t,j):                                          #se der vitoria na proxima jogada retorna a posicao da funcao vitoria            
        return vitoria(t,j)[0]
    
    elif vitoria(t,inteiro_para_peca(-peca_para_inteiro(j))): #se der vitoria na proxima jogada para o openente executa a funcao vitoria como o oponente
        return vitoria(t,inteiro_para_peca(-peca_para_inteiro(j)))[0]
    
    return centro_canto_lateral(t)                            #devolve a funcao centro_canto_lateral
      
def obter_movimento_auto(t,j,dif):
    ##tabuleiro x peca x str --> tuplo de posicoes
    """
    recebe um tabuleiro e uma peca do jogador computador, e devolve um tuplo com
    uma ou duas posicoes que representam uma posicao ou um movimento escolhido 
    pelo computador
    """
    if len(obter_posicoes_livres(t)) != 3:    #se o tabuleiro estiver na fase de colocacao de pecas retorna a funcao posicao_auto_sem_mov num tuplo com unico indice
        return ((posicao_auto_sem_mov(t,j)),)
    
    if not posicoes_jogaveis(t,j):        #se nao for possivel jogar, pois todas as posicoes estao bloqueadas retorna um tuplo com duas posicoes iguais
        repete = obter_posicoes_jogador(t, j)
        return repete[0],repete[0]   
                
    elif dif == 'facil':      #se o argumento dif corresponder a string 'facil' retorna o tuplo das posicoes correspondentes ao modo facil              
        return facil(t,j)
    
    elif dif == 'normal':     #se o argumento dif corresponder a string 'normal' retorna o tuplo das posicoes correspondentes ao modo normal              
        r = minimax(t, j, 1, ())
        return r[1][0],r[1][1]
    
    elif dif == 'dificil':    #se o argumento corresponder a string 'dificil' retorna o tuplo das posicoes correspondentes ao modo dificil             
        r = minimax(t, j, 5, ())
        return r[1][0],r[1][1]

def minimax(t, j, profundidade, seq_movimentos):
    ##tabuleiro x peca x int x tuplo --> tuplo
    """
    recebe  um  tabuleiro e uma peca de um jogador, e devolve o melhor resultado
    obtido e a melhor sequencia de movimentos possiveis de acordo com o
    tabuleiro t, a peca j e a profundidade e a sequencia de movimentos dada
    """
    melhor_seq_movimentos = ()
    j_ganhador = obter_ganhador(t)
    if not pecas_iguais(j_ganhador,cria_peca(' ')) or not profundidade: #se a profundidade for 0 ou se existe um vencedor 
        return peca_para_inteiro(j_ganhador),seq_movimentos             #retorna valor_tabuleiro e a sequencia de movimentos
    else:
        melhor_resultado = ganha_outro_jogador(t,j)
        for p in obter_posicoes_jogador(t,j):
            for p2 in obter_posicoes_adjacentes(p):  
                if eh_posicao_livre(t,p2):                              #indica duas posicoes p e p2 que possam criar um movimento jogavel
                    t_novo = move_peca(cria_copia_tabuleiro(t),p,p2)
                    novo_resultado,nova_seq_movimentos = minimax(t_novo, \
                    inteiro_para_peca(-peca_para_inteiro(j)),\
                    profundidade-1,seq_movimentos + (p,p2))   #executa o minimax com um novo tabuleiro (tranformado com o movimento), a peca do adversario e menos um de profundiade,
                                                              #e sequencia de movimentos. O valor desse minimax e armazenado nas variaveis novo_resultado e nova_seq_movimentos      
                    if melhor_seq_movimentos == () or \
                    (pecas_iguais(j, cria_peca('X')) and \
                    (novo_resultado > melhor_resultado)) or \
                    (pecas_iguais(j, cria_peca('O')) and \
                    (novo_resultado < melhor_resultado)):     #verifica se este novo_resultado e nova_seq_movimentos e melhor que a do oponente ou que a anterior
                        melhor_resultado, melhor_seq_movimentos =\
                        novo_resultado,nova_seq_movimentos  
        
        return melhor_resultado, melhor_seq_movimentos
    
def ganha_outro_jogador(t,j):
    ##tabuleiro x peca --> int
    """
    recebe um tabuleiro t e uma peca j e indica se o jogador contrario
    se encontra em vantagem (pode ganhar na ronda seguinte)
    """
    j_in = inteiro_para_peca(-peca_para_inteiro(j))
    vi = vitoria(t,j_in)
    for r in posicoes_jogaveis(t,j_in): #precorre todas as posicoes de destino de movimentos jogaveis
        if posicoes_iguais(r,vi):       #compara se pode existir vitoria num desses destinos
            return peca_para_inteiro(j_in)
    return 0
     
def str_para_posicao(st):
    ##str --> posicao
    """
    recebe uma str st e transforma em posicao
    """
    col = st[0]
    lin = st[1]
    return cria_posicao(col,lin)

def turno_jog(t,jog):
    ##tabuleiro x peca --> tabuleiro
    """
    devolve um tabuleiro, esse representa o tranformado do tabuleiro t com base
    na peca do jogador jog, na fase de jogo do tabuleiro t e do input 
    introduzido pelo jogador
    """
    jogado_pelo_jogador = obter_movimento_manual(t,jog)
    if len(obter_posicoes_livres(t)) != 3:   #se o jogo nao estiver na fase de movimento, coloca na posicao introduzida pelo jogador a sua peca 
        return coloca_peca(t,jog,jogado_pelo_jogador[0])  
    
    else:                                    #se o jogo estiver na fase de movimento, executa o movimento que o jogador pretendeu
        return move_peca(t,jogado_pelo_jogador[0],jogado_pelo_jogador[1])
    
def turno_pc(t,jog_inv,dif):
    ##tabuleiro x peca x str --> tabuleiro
    """
    devolve um tabuleiro, esse representa tranformado do tabuleiro t com base na
    peca do jogador jog_inv,na fase de jogo do tabuleiro e sua dificuldade jogo
    """
    jogado_pelo_computador = obter_movimento_auto(t,jog_inv,dif)
    if len(obter_posicoes_livres(t)) != 3:
        return coloca_peca(t,jog_inv,jogado_pelo_computador[0])
    else:
        return move_peca(t,jogado_pelo_computador[0],jogado_pelo_computador[1])
    
def jog_X(t,jog,dif):
    ##tabuleiro x peca x str --> peca
    """
    devolve o jogador ganhador apos  um jogo do moinho em que o jogador
    escolheu a peca 'X', e a dificuldade pretendida
    """
    r = cria_peca(' ')
    jog_inv = inteiro_para_peca(-peca_para_inteiro(jog))
    while pecas_iguais(r,cria_peca(' ')):              
        t = turno_jog(t,jog)                    #primeiro joga o jogador
        print(tabuleiro_para_str(t))
        r = obter_ganhador(t)
        if not pecas_iguais(r,cria_peca(' ')):
            break

        print('Turno do computador ('+dif+'):') #depois joga o computador
        t=turno_pc(t,jog_inv,dif)
        print(tabuleiro_para_str(t))
        r = obter_ganhador(t)
    return r

def jog_O(t,jog,dif):
    ##tabuleiro x peca x str --> peca
    """
    devolve o jogador ganhador apos um jogo do moinho em que o jogador escolheu
    a peca 'O', e a dificuldade pretendida
    """
    r = cria_peca(' ')
    jog_inv = inteiro_para_peca(-peca_para_inteiro(jog))
    
    while pecas_iguais(r,cria_peca(' ')):
        print('Turno do computador ('+dif+'):') 
        t=turno_pc(t,jog_inv,dif)             #primeiro o turno do computador
        print(tabuleiro_para_str(t))
        r = obter_ganhador(t)
        if not pecas_iguais(r,cria_peca(' ')):
            break
        
        t = turno_jog(t,jog)                  #depois joga o turno do jogador 
        print(tabuleiro_para_str(t))
        r = obter_ganhador(t)
    return r   
      
def moinho(peca_jogador,dif):
    ##str x str --> str
    ### Esta funcao corresponde a principal do programa. Se quiser jogar
    ### ao jogo do moinho tera de escrever na consola moinho(peca_jogador,dif)
    ### onde peca_jogador corresponde ou a string '[X]'
    ### se quiser jogar com a peca X
    ### e '[O]' se quiser jogar com a peca O
    ### a dif pode ser, 'facil', 'normal' ou 'dificil'
    """
    verifica se com os argumentos dados e possivel um jogo do moinho senao 
    for possivel executa ValueError 'moinho: argumentos invalidos' se for
    valido executa a funcao ate existir um jogador ganhador
    """
    if peca_jogador not in ('[X]','[O]') or\
    dif not in ('facil','normal','dificil'):
        raise ValueError('moinho: argumentos invalidos')
    
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade '+dif+'.')
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    jog = cria_peca(peca_jogador[1])
    if pecas_iguais(jog,cria_peca('X')):
        vencedor = jog_X(t,jog,dif) 
    else:
        vencedor = jog_O(t,jog,dif)  
        
    return peca_para_str(vencedor)
