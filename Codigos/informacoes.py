from Graphics import graphics as gf

### INFORMAÇÕES DOS CANDIDATOS, QUE APARECEM NA TELA: ###

#SÃO CRIADAS E RETORNADAS LISTAS DE OBJETOS:

def InformacoesSenador(nome_senador, partido_senador, primeiro_suplente,segundo_suplente, foto_senador):
    LISTA_INFORMACOES = []

    #Criando os objetos e adicionando na lista:
    info_nome = gf.Text(gf.Point(51, 200), f'Nome:')
    info_nome.setStyle("bold")
    LISTA_INFORMACOES.append(info_nome)
    info_partido = gf.Text(gf.Point(56, 230), f'Partido:')
    info_partido.setStyle("bold")
    LISTA_INFORMACOES.append(info_partido)
    info_suplente = gf.Text(gf.Point(72, 260), f'1º Suplente:')
    info_suplente.setStyle("bold")
    LISTA_INFORMACOES.append(info_suplente)
    info_secsuplente = gf.Text(gf.Point(72, 290), f'2º Suplente:')
    info_secsuplente.setStyle("bold")
    LISTA_INFORMACOES.append(info_secsuplente)

    #
    num = len(nome_senador) * 3.7 #-> variável para saber qual a distância cada nome vai ter do "Nome:"
    nome_candidato = gf.Text(gf.Point(85+num, 200), f'{nome_senador}') #-> nome do candidato, recebido como parâmetro
    LISTA_INFORMACOES.append(nome_candidato)
    #
    num = len(partido_senador) * 4.3 #-> variável para saber qual a distância cada nome vai ter do "Partido:"
    partido_candidato = gf.Text(gf.Point(93+num, 230), f'{partido_senador}') #-> partido do candidato
    LISTA_INFORMACOES.append(partido_candidato)
    #
    num = len(primeiro_suplente) * 3.6 #-> variável para saber qual a distância cada nome vai ter do "Vice-Presidente:"
    primeiro_suplente = gf.Text(gf.Point(127+num, 260), f'{primeiro_suplente}') #-> nome do vice
    LISTA_INFORMACOES.append(primeiro_suplente)

    num = len(segundo_suplente) * 3.6 #-> variável para saber qual a distância cada nome vai ter do "Vice-Presidente:"
    segundo_suplente = gf.Text(gf.Point(127+num, 290), f'{segundo_suplente}') #-> nome do vice
    LISTA_INFORMACOES.append(segundo_suplente)

    #Foto do senador:
    foto_sen = gf.Image(gf.Point(467, 109.5), f"{foto_senador}.png")
    LISTA_INFORMACOES.append(foto_sen)
    senador = gf.Text(gf.Point(467, 185), "Senador") #-> mensagem que fica abaixo da foto
    senador.setSize(8)
    LISTA_INFORMACOES.append(senador)

    foto_primeirosup = gf.Image(gf.Point(472, 255), f"Imagens/Senadores/undefined.png")
    LISTA_INFORMACOES.append(foto_primeirosup)
    prim_sup = gf.Text(gf.Point(472, 319), "1º Suplente") #-> mensagem que fica abaixo da foto
    prim_sup.setSize(8)
    LISTA_INFORMACOES.append(prim_sup)

    #
    linha_horizontal = gf.Line(gf.Point(20, 308), gf.Point(423, 308))
    LISTA_INFORMACOES.append(linha_horizontal)
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_INFORMACOES.append(aperte_tecla)

    return(LISTA_INFORMACOES)

def InformacoesGovernador(nome_governador,partido_governador,vice_governador,foto_governador,foto_vice):
    LISTA_INFORMACOES = []
    info_nome = gf.Text(gf.Point(50, 215), f'Nome:')
    info_nome.setStyle("bold")
    LISTA_INFORMACOES.append(info_nome)
    info_partido = gf.Text(gf.Point(55, 245), f'Partido:')
    info_partido.setStyle("bold")
    LISTA_INFORMACOES.append(info_partido)
    info_vice = gf.Text(gf.Point(92, 275), f'Vice-Governador:')
    info_vice.setStyle("bold")
    LISTA_INFORMACOES.append(info_vice)
    #
    num = len(nome_governador) * 3.5 #-> variável para saber qual a distância cada nome vai ter do "Nome:"
    nome_candidato = gf.Text(gf.Point(86+num, 215), f'{nome_governador}') #-> nome do candidato, recebido como parâmetro
    LISTA_INFORMACOES.append(nome_candidato)
    #
    num = len(partido_governador) * 3.9 #-> variável para saber qual a distância cada nome vai ter do "Partido:"
    partido_candidato = gf.Text(gf.Point(93+num, 245), f'{partido_governador}') #-> partido do candidato
    LISTA_INFORMACOES.append(partido_candidato)
    #
    num = len(vice_governador) * 3.6 #-> variável para saber qual a distância cada nome vai ter do "Vice-Presidente:"
    vice_governador = gf.Text(gf.Point(168+num, 275), f'{vice_governador}') #-> nome do vice
    LISTA_INFORMACOES.append(vice_governador)
    #Imagem do presidente:
    foto_pre = gf.Image(gf.Point(467, 109.5), f"{foto_governador}")
    LISTA_INFORMACOES.append(foto_pre)
    presidente = gf.Text(gf.Point(467, 185), "Governador") #-> mensagem que fica abaixo da foto
    presidente.setSize(8)
    LISTA_INFORMACOES.append(presidente)
    #Imagem do vice-presidente:
    foto_vice = gf.Image(gf.Point(472, 255), f"{foto_vice}")
    LISTA_INFORMACOES.append(foto_vice)
    vice = gf.Text(gf.Point(472, 319), "Vice-Governador") #-> mensagem que fica abaixo da foto
    vice.setSize(7)
    LISTA_INFORMACOES.append(vice)
    #
    linha_horizontal = gf.Line(gf.Point(20, 308), gf.Point(423, 308))
    LISTA_INFORMACOES.append(linha_horizontal)
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_INFORMACOES.append(aperte_tecla)

    return(LISTA_INFORMACOES)


### LISTA COM TODAS AS INFORMAÇÕES DOS CANDIDATOS: ####
def InformacoesPresidente(nome_presidente,partido_presidente,vice_presidente,foto_presidente,foto_vice):
    LISTA_INFORMACOES = []

    #Criando os objetos e adicionando na lista:
    info_nome = gf.Text(gf.Point(50, 215), f'Nome:')
    info_nome.setStyle("bold")
    LISTA_INFORMACOES.append(info_nome)
    info_partido = gf.Text(gf.Point(55, 245), f'Partido:')
    info_partido.setStyle("bold")
    LISTA_INFORMACOES.append(info_partido)
    info_vice = gf.Text(gf.Point(88, 275), f'Vice-Presidente:')
    info_vice.setStyle("bold")
    LISTA_INFORMACOES.append(info_vice)
    #
    num = len(nome_presidente) * 3.7 #-> variável para saber qual a distância cada nome vai ter do "Nome:"
    nome_candidato = gf.Text(gf.Point(86+num, 215), f'{nome_presidente}') #-> nome do candidato, recebido como parâmetro
    LISTA_INFORMACOES.append(nome_candidato)
    #
    num = len(partido_presidente) * 4 #-> variável para saber qual a distância cada nome vai ter do "Partido:"
    partido_candidato = gf.Text(gf.Point(93+num, 245), f'{partido_presidente}') #-> partido do candidato
    LISTA_INFORMACOES.append(partido_candidato)
    #
    num = len(vice_presidente) * 3.8 #-> variável para saber qual a distância cada nome vai ter do "Vice-Presidente:"
    vice_presidente = gf.Text(gf.Point(158+num, 275), f'{vice_presidente}') #-> nome do vice
    LISTA_INFORMACOES.append(vice_presidente)
    #Imagem do presidente:
    foto_pre = gf.Image(gf.Point(467, 109.5), f"{foto_presidente}")
    LISTA_INFORMACOES.append(foto_pre)
    presidente = gf.Text(gf.Point(467, 185), "Presidente") #-> mensagem que fica abaixo da foto
    presidente.setSize(8)
    LISTA_INFORMACOES.append(presidente)
    #Imagem do vice-presidente:
    foto_vice = gf.Image(gf.Point(472, 255), f"{foto_vice}")
    LISTA_INFORMACOES.append(foto_vice)
    vice = gf.Text(gf.Point(472, 319), "Vice-Presidente") #-> mensagem que fica abaixo da foto
    vice.setSize(7)
    LISTA_INFORMACOES.append(vice)
    #
    linha_horizontal = gf.Line(gf.Point(20, 308), gf.Point(423, 308))
    LISTA_INFORMACOES.append(linha_horizontal)
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_INFORMACOES.append(aperte_tecla)

    return(LISTA_INFORMACOES)
