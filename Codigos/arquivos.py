### FUNÇÕES QUE CRIAM UM DICIONÁRIO COM AS INFORMAÇÕES NECESSÁRIAS DOS RESPECTIVOS CANDIDATOS: ###



def ArquivoSenadores():
    arquivo_senadores = open("Arquivos/Candidatos/candidatos_senadores.csv", "r",  encoding="utf-8")
    lista = arquivo_senadores.readlines() # fazendo o arquivo virar uma lista
    arquivo_senadores.close()

    nova_lista = [] # nova lista, para fazer o split

    #Fazendo as informações dos candidatos virarem uma sublista:
    for item in lista:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior (sublista da "nova_lista")

    candidatos_senadores = {} #-> criando um dicionário com o conteúdo da lista

    primeiro_indice = 1
    for i in nova_lista[1:]:

        #Fazendo o primeiro elemento de cada lista virar uma "chave" e os demais o conteúdo do dicionário:
        candidatos_senadores[f'{nova_lista[primeiro_indice][0]}'] = [ f'{nova_lista[primeiro_indice][1]}', #-> nome
                                                                    f'{nova_lista[primeiro_indice][2]}', #-> partido
                                                                    f'{nova_lista[primeiro_indice][3]}', #-> 1º suplente (nome)
                                                                    f'{nova_lista[primeiro_indice][4]}', #-> 2º suplente  (nome) 
                                                                    f'Imagens/Senadores/{nova_lista[primeiro_indice][5]}'] #-> foto do(a) senador(a)                                                          
        primeiro_indice += 1

    return(candidatos_senadores)

### FUNÇÃO PARA FAZER A CONTAGEM DOS VOTOS DOS SENADORES: ###
def ContagemSenadores(voto):
    #Abrindo o arquivo e retirando o conteúdo:
    arquivo = open("Arquivos/Contagem/contagem_senadores.csv", "r",  encoding="utf-8")
    conteudo_contagem = arquivo.readlines()
    arquivo.close()

    #Lista vazia que vai virar uma lista com sublistas:
    nova_lista = []

    for item in conteudo_contagem:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    #Adicionando um voto no respectivo candidato:
    for item in nova_lista:
        if voto == item[0]:
            numero = int(item[1])
            numero += 1
            item[1] = str(numero)

    #Criando uma string que será adicionada ao arquivo:
    string_arquivo = ""

    #Concatenando o que é necessário na string:
    for item in nova_lista:
        string_arquivo += item[0]
        string_arquivo += ";"
        string_arquivo += item[1]
        string_arquivo += "\n"

    #Modificando o arquivo:
    arquivo = open("Arquivos/Contagem/contagem_senadores.csv", "w")
    arquivo.write(string_arquivo)
    arquivo.close()

####

### FUNÇÃO QUE CRIA UM DICIONÁRIO COM AS INFORMAÇÕES NECESSÁRIAS DOS GOVERNADORES: ###
def ArquivoGovernadores():
    arquivo_governadores = open("Arquivos/Candidatos/candidatos_gov.csv", "r",  encoding="utf-8")
    lista = arquivo_governadores.readlines() # fazendo o arquivo virar uma lista
    arquivo_governadores.close()

    nova_lista = [] # nova lista, para fazer o split

    #Fazendo as informações dos candidatos virarem uma sublista:
    for item in lista:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior (sublista da "nova_lista")

    candidatos_senadores = {} #-> criando um dicionário com o conteúdo da lista

    primeiro_indice = 1
    for i in nova_lista[1:]:

        #Fazendo o primeiro elemento de cada lista virar uma "chave" e os demais o conteúdo do dicionário:
        candidatos_senadores[f'{nova_lista[primeiro_indice][0]}'] = [ f'{nova_lista[primeiro_indice][1]}', #-> Nome
                                                                    f'{nova_lista[primeiro_indice][2]}', #-> Partido
                                                                    f'{nova_lista[primeiro_indice][3]}', #-> Vice-Governador
                                                                    f'Imagens/Governadores/{nova_lista[primeiro_indice][4]}', #-> Foto-Governador
                                                                    f'Imagens/Governadores/{nova_lista[primeiro_indice][5]}'] #-> Foto-Vice                                                           
        primeiro_indice += 1

    return(candidatos_senadores)

### FUNÇÃO PARA FAZER A CONTAGEM DOS VOTOS DOS GOVERNADORES: ###
def ContagemGovernadores(voto):
    #Abrindo o arquivo e retirando o conteúdo:
    arquivo = open("Arquivos/Contagem/contagem_governadores.csv", "r",  encoding="utf-8")
    conteudo_contagem = arquivo.readlines()
    arquivo.close()

    #Lista vazia que vai virar uma lista com sublistas:
    nova_lista = []

    for item in conteudo_contagem:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    #Adicionando um voto no respectivo candidato:
    for item in nova_lista:
        if voto == item[0]:
            numero = int(item[1])
            numero += 1
            item[1] = str(numero)

    #Criando uma string que será adicionada ao arquivo:
    string_arquivo = ""

    #Concatenando o que é necessário na string:
    for item in nova_lista:
        string_arquivo += item[0]
        string_arquivo += ";"
        string_arquivo += item[1]
        string_arquivo += "\n"

    #Modificando o arquivo:
    arquivo = open("Arquivos/Contagem/contagem_governadores.csv", "w")
    arquivo.write(string_arquivo)
    arquivo.close()

####

### FUNÇÃO QUE TRANSFORMA O CONTEÚDO DO ARQUIVO EM UM DICIONÁRIO, PARA RETIRAR AS INFORMAÇÕES DOS RESPECTIVOS CANDIDATOS: ###
def ArquivoPresidentes():
    arquivo_presidentes = open("Arquivos/Candidatos/candidatos_pres.csv", "r",  encoding="utf-8")
    lista = arquivo_presidentes.readlines() # fazendo o arquivo virar uma lista
    arquivo_presidentes.close()

    nova_lista = [] # nova lista, para fazer o split

    #Fazendo as informações dos candidatos virarem uma sublista:
    for item in lista:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior (sublista da "nova_lista")

    candidatos = {} #-> criando um dicionário com o conteúdo da lista

    primeiro_indice = 1
    for i in nova_lista[1:]:

        #Fazendo o primeiro elemento de cada lista virar uma "chave" e os demais o conteúdo do dicionário:
        candidatos[f'{nova_lista[primeiro_indice][0]}'] = [ f'{nova_lista[primeiro_indice][1]}', #-> nome
                                                            f'{nova_lista[primeiro_indice][2]}', #-> partido
                                                            f'{nova_lista[primeiro_indice][3]}', #-> vice-presidente
                                                            f'Imagens/Presidentes/{nova_lista[primeiro_indice][4]}', #-> imagem-presidente
                                                            f'Imagens/Presidentes/{nova_lista[primeiro_indice][5]}'] #-> imagem-vice                                                               
        primeiro_indice += 1

    return(candidatos)


### FUNÇÃO PARA FAZER A CONTABILIZAÇÃO DOS VOTOS: ###
def ContagemPresidentes(voto):
    #Abrindo o arquivo e retirando o conteúdo:
    arquivo = open("Arquivos/Contagem/contagem_presidentes.csv", "r",  encoding="utf-8")
    conteudo_contagem = arquivo.readlines()
    arquivo.close()

    #Lista vazia que vai virar uma lista com sublistas:
    nova_lista = []

    for item in conteudo_contagem:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    #Adicionando um voto no respectivo candidato:
    for item in nova_lista:
        if voto == item[0]:
            numero = int(item[1])
            numero += 1
            item[1] = str(numero)

    #Criando uma string que será adicionada ao arquivo:
    string_arquivo = ""

    #Concatenando o que é necessário na string:
    for item in nova_lista:
        string_arquivo += item[0]
        string_arquivo += ";"
        string_arquivo += item[1]
        string_arquivo += "\n"

    #Modificando o arquivo:
    arquivo = open("Arquivos/Contagem/contagem_presidentes.csv", "w")
    arquivo.write(string_arquivo)
    arquivo.close()

