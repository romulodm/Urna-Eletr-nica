from Graphics import graphics as gf

import pygame as pg
import time

####

from Codigos import arquivos as arq #-> funções que criam dicionários com informações dos candidatos e que fazem a contagem dos votos.
from Codigos import informacoes as inf #-> funções que retornam uma lista com os elementos que são desenhados na tela (nome do candidato, partido do candidato...)
from Codigos import visual as vis #-> lista com objetos que são desenhados no início (botoões, tela, imagem "Justiça Eleitoral")
from Codigos import resultados as res #-> funções que fazem o cálculo da porcentagem de cada candidato (no encerramento).
from Codigos import validar_clique as val #-> função que pega a posição X e Y do win.getMouse() e "valida" o clique.
from Codigos import criar_html as criar_html #-> função que cria um html a partir dos arquivos "Resultados".
from Codigos import mensagens as msg #-> funções que mostram mensagens de avisos na tela.

win = gf.GraphWin( "Urna Eletrônica", 790, 380)

### FUNÇÃO PRINCIPAL DO CÓDIGO: ###
def VotacaoPrincipal(win, cargo, GUARDAR_VOTOS):
    win.setBackground("#CDC8B5")
    win.autoflush=False # autoflush para evitar a "piscadinha" na hora de desenhar os botões.

    VISUAL_URNA = vis.VisualUrna(cargo)
    for item in VISUAL_URNA:
        item.draw(win)

    BOTOES = vis.ImagemBotoes()
    for item in BOTOES:
        item.draw(win)

    QUADRADOS = vis.QuadradosVoto(cargo)
    for item in QUADRADOS:
        item.draw(win)

    DIGITOS = vis.DigitosVoto()
    for item in DIGITOS:
        item.draw(win)  
    if cargo != "Senador":
        pos_x = 25
    else:
        pos_x = 0

    voto = "" #-> variável voto

    win.autoflush=True
    
    #Laço de repetição principal do código:
    while True:

        clique = win.getMouse()
        posicao_x = clique.getX()
        posicao_y = clique.getY()

        #FUNÇÃO QUE VALIDA O CLIQUE DO USUÁRIO:
        TECLA = val.ValidarClique(posicao_x, posicao_y)

        #SE O USUÁRIO CLICAR NOS NÚMEROS:
        if TECLA[0] == "NUM" and len(voto) < 3:
            if len(voto) < 3:
                #Concateno o número no voto:
                voto += TECLA[1]

            #Movimento dos botões:
            BOTOES[int(TECLA[1])].move(2,2)
            time.sleep(0.13)
            BOTOES[int(TECLA[1])].move(-2,-2)

            #Mudo cada dígito:
            if len(voto) <= 3:
                if len(voto) == 1:
                    DIGITOS[0] = gf.Text(gf.Point(65+pos_x, 155), f"{voto[0]}")
                    DIGITOS[0].setSize(26)
                    DIGITOS[0].setOutline("green")
                if len(voto) == 2:
                    DIGITOS[1] = gf.Text(gf.Point(115+pos_x, 155), f"{voto[1]}")
                    DIGITOS[1].setSize(26)
                    DIGITOS[1].setOutline("green")
                if len(voto) == 3 and cargo == "Senador":
                    DIGITOS[2] = gf.Text(gf.Point(165, 155), f"{voto[2]}")
                    DIGITOS[2].setSize(26)
                    DIGITOS[2].setOutline("green")
            
                #Apago os dígitos e desenho eles novamente (modificados):
                for item in DIGITOS:
                    item.undraw()
                    item.draw(win)
                

        #SE O USUÁRIO CLICAR EM BOTÕES QUE FAZEM ACÕES:
        if TECLA[0] == "AÇÃO":

            ###SE APERTAR A TECLA CORRIGE E NÃO TIVER NADA PARA CORRIGIR ###
            if TECLA[1] == "CORRIGE" and len(voto) == 0:
                BOTOES[11].move(2,2)
                time.sleep(0.13)
                BOTOES[11].move(-2,-2)

                msg.CorrigeInvalido(win)

            ###SE APERTAR A TECLA CORRIGE: ###
            if TECLA[1] == "CORRIGE":
                BOTOES[11].move(2,2)
                time.sleep(0.13)
                BOTOES[11].move(-2,-2)

                for item in DIGITOS:
                    item.undraw()
                                   
                DIGITOS[0] = gf.Text(gf.Point(0, 0), f"")
                DIGITOS[1] = gf.Text(gf.Point(0, 0), f"")
                if cargo == "Senador":
                    DIGITOS[2] = gf.Text(gf.Point(0, 0), f"")

                voto = voto[:-3]

            ### SE APERTAR A TECLA CONFIRMA SEM O VOTO SER PREENCHIDO: ###
            if TECLA[1] == "CONFIRMA":
                BOTOES[12].move(2,2)
                time.sleep(0.13)
                BOTOES[12].move(-2,-2)

                msg.ConfirmaInvalido(win)

            ### SE APERTAR A TECLA "BRANCO" E O CAMPO DE VOTAÇÃO TIVER NÚMEROS: ###
            if TECLA[1] == "BRANCO" and len(voto) > 0:
                BOTOES[10].move(2,2)
                time.sleep(0.13)
                BOTOES[10].move(-2,-2)

                msg.BrancoInvalido(win)

            ### SE APERTAR A TECLA "BRANCO": ###
            if TECLA[1] == "BRANCO" and len(voto) == 0:
                BOTOES[10].move(2,2)
                time.sleep(0.13)
                BOTOES[10].move(-2,-2)

                for item in QUADRADOS:
                    item.undraw()

                LISTA_BRANCO = vis.VotoBranco()
                for item in LISTA_BRANCO:
                    item.draw(win)  

                Validar = True
                while Validar:
                    clique = win.getMouse()
                    
                    TECLA = val.ValidarClique(clique.getX(), clique.getY())

                    if TECLA[1] == "CONFIRMA":

                        BOTOES[12].move(2,2)
                        time.sleep(0.13)
                        BOTOES[12].move(-2,-2)

                        if cargo == "Senador":
                            GUARDAR_VOTOS[0] = "BRANCO"
                        if cargo == "Governador":
                            GUARDAR_VOTOS[1] = "BRANCO"
                        if cargo == "Presidente":

                            arq.ContagemSenadores(str(GUARDAR_VOTOS[0]))
                            arq.ContagemGovernadores(GUARDAR_VOTOS[1])
                            arq.ContagemPresidentes("BRANCO")

                       
                        for item in LISTA_BRANCO:
                            item.undraw()

                        if cargo == "Senador":
                            time.sleep(0.13)
                            return(VotacaoPrincipal(win, "Governador", GUARDAR_VOTOS))                    
                        if cargo == "Governador":
                            time.sleep(0.13)
                            return(VotacaoPrincipal(win, "Presidente", GUARDAR_VOTOS))
                        if cargo == "Presidente":

                            VISUAL_URNA[3].undraw()
                            time.sleep(0.13)
                            return(VotoConfirmado(win, BOTOES))

                    if TECLA[1] == "CORRIGE":
                        BOTOES[11].move(2,2)
                        time.sleep(0.13)
                        BOTOES[11].move(-2,-2)

                        for item in LISTA_BRANCO:
                            item.undraw()

                        for item in QUADRADOS:
                            item.draw(win)

                        Validar = False
                            

        if len(voto) == 3 and cargo == "Senador":
            CHECAGEM = ChecarVoto("Senador", voto, BOTOES, DIGITOS)

            if CHECAGEM == "CORRIGE":
                for item in DIGITOS:
                    item.undraw()
                voto = voto[:-3]

            if CHECAGEM == "CONFIRMA-CORRETO":
                for item in DIGITOS:
                    item.undraw()
                
                for item in QUADRADOS:
                    item.undraw()

                GUARDAR_VOTOS[0] = voto

                return(VotacaoPrincipal(win, "Governador", GUARDAR_VOTOS))

            if CHECAGEM == "CONFIRMA-NULO":
                for item in DIGITOS:
                    item.undraw()
                
                for item in QUADRADOS:
                    item.undraw()

                GUARDAR_VOTOS[0] = f"NULO"

                return(VotacaoPrincipal(win, "Governador", GUARDAR_VOTOS))

        if len(voto) == 2 and cargo == "Governador":
            CHECAGEM = ChecarVoto("Governador", voto, BOTOES, DIGITOS)

            if CHECAGEM == "CORRIGE":
                for item in DIGITOS:
                    item.undraw()
                voto = voto[:-3]

            if CHECAGEM == "CONFIRMA-CORRETO":
                for item in DIGITOS:
                    item.undraw()
                
                for item in QUADRADOS:
                    item.undraw()

                VISUAL_URNA[3].undraw()

                GUARDAR_VOTOS[1] = f"{voto}"

                return(VotacaoPrincipal(win, "Presidente", GUARDAR_VOTOS))


            if CHECAGEM == "CONFIRMA-NULO":
                for item in DIGITOS:
                    item.undraw()
                
                for item in QUADRADOS:
                    item.undraw()

                VISUAL_URNA[3].undraw()

                GUARDAR_VOTOS[1] = f"NULO"

                return(VotacaoPrincipal(win, "Presidente", GUARDAR_VOTOS))

        if len(voto) == 2 and cargo == "Presidente":
            CHECAGEM = ChecarVoto("Presidente", voto, BOTOES, DIGITOS)

            if CHECAGEM == "CORRIGE":
                for item in DIGITOS:
                    item.undraw()
                voto = voto[:-3]

            if CHECAGEM == "CONFIRMA-CORRETO":
                for item in DIGITOS:
                    item.undraw()
                
                for item in QUADRADOS:
                    item.undraw()

                VISUAL_URNA[3].undraw()

                arq.ContagemSenadores(GUARDAR_VOTOS[0])
                arq.ContagemGovernadores(GUARDAR_VOTOS[1])
                arq.ContagemPresidentes(voto)

                VotoConfirmado(win, BOTOES)

            if CHECAGEM == "CONFIRMA-NULO":
                for item in DIGITOS:
                    item.undraw()
                
                for item in QUADRADOS:
                    item.undraw()

                VISUAL_URNA[3].undraw()

                arq.ContagemSenadores(GUARDAR_VOTOS[0])
                arq.ContagemGovernadores(GUARDAR_VOTOS[1])
                arq.ContagemPresidentes("NULO")

                VotoConfirmado(win, BOTOES)
                      


#FUNÇÃO QUE CHECA SE O VOTO DIGITADO É VÁLIDO OU NULO:
def ChecarVoto(cargo, voto, BOTOES, DIGITOS):
    if cargo == "Senador":

        CANDIDATOS = arq.ArquivoSenadores()

        if voto in CANDIDATOS:
            LISTA_INFORMACOES = inf.InformacoesSenador(CANDIDATOS[voto][0], CANDIDATOS[voto][1], 
                                                    CANDIDATOS[voto][2], CANDIDATOS[voto][3], CANDIDATOS[voto][4])

            for item in LISTA_INFORMACOES:
                item.draw(win)

    ####
    if cargo == "Governador":

        CANDIDATOS = arq.ArquivoGovernadores()

        if voto in CANDIDATOS:
            LISTA_INFORMACOES = inf.InformacoesGovernador(CANDIDATOS[voto][0], CANDIDATOS[voto][1], 
                                                    CANDIDATOS[voto][2], CANDIDATOS[voto][3], CANDIDATOS[voto][4])
            for item in LISTA_INFORMACOES:
                item.draw(win)

    ####
    if cargo == "Presidente":

        CANDIDATOS = arq.ArquivoPresidentes()

        if voto in CANDIDATOS:
            LISTA_INFORMACOES = inf.InformacoesPresidente(CANDIDATOS[voto][0], CANDIDATOS[voto][1], 
                                                    CANDIDATOS[voto][2], CANDIDATOS[voto][3], CANDIDATOS[voto][4])
            for item in LISTA_INFORMACOES:
                item.draw(win)

    ### SE O VOTO ESTIVER NA LISTA DE CANDIDATOS: ###
    if voto in CANDIDATOS:
        while True:
            clique = win.getMouse()
            
            TECLA = val.ValidarClique(clique.getX(), clique.getY())

            if TECLA[1] == "CONFIRMA":
            
                BOTOES[12].move(2,2)
                time.sleep(0.13)
                BOTOES[12].move(-2,-2) 
                for item in DIGITOS:
                    item.undraw()

                for item in LISTA_INFORMACOES:
                    item.undraw()

                return("CONFIRMA-CORRETO")

            if TECLA[1] == "CORRIGE":

                BOTOES[11].move(2,2)
                time.sleep(0.13)
                BOTOES[11].move(-2,-2) 
                for item in DIGITOS:
                    item.undraw()

                voto = voto[:-3]
                DIGITOS[0] = gf.Text(gf.Point(0, 0), f"")
                DIGITOS[1] = gf.Text(gf.Point(0, 0), f"")
                if cargo == "Senador":
                    DIGITOS[2] = gf.Text(gf.Point(0, 0), f"")

                for item in LISTA_INFORMACOES:
                    item.undraw()

                return("CORRIGE")

            ### SE APERTAR A TECLA "BRANCO": ###
            if TECLA[1] == "BRANCO" and len(voto) > 0:
                BOTOES[10].move(2,2)
                time.sleep(0.13)
                BOTOES[10].move(-2,-2)

                msg.BrancoInvalido(win)

    ### SE O VOTO NÃO ESTIVER NA LISTA DE CANDIDATOS: ###
    if voto not in CANDIDATOS:
        LISTA_NULO = vis.MostraNulo()

        for item in LISTA_NULO:
            item.draw(win)

        while True:
            clique = win.getMouse()
            
            TECLA = val.ValidarClique(clique.getX(), clique.getY())

            if TECLA[1] == "CONFIRMA":

                BOTOES[12].move(2,2)
                time.sleep(0.13)
                BOTOES[12].move(-2,-2)
                for item in DIGITOS:
                    item.undraw() 

                for item in LISTA_NULO:
                    item.undraw()

                return("CONFIRMA-NULO")

            if TECLA[1] == "CORRIGE":

                BOTOES[11].move(2,2)
                time.sleep(0.13)
                BOTOES[11].move(-2,-2) 
                for item in DIGITOS:
                        item.undraw()

                voto = voto[:-3]
                DIGITOS[0] = gf.Text(gf.Point(0, 0), f"")
                DIGITOS[1] = gf.Text(gf.Point(0, 0), f"")
                if cargo == "Senador":
                    DIGITOS[2] = gf.Text(gf.Point(0, 0), f"")

                for item in LISTA_NULO:
                    item.undraw()

                return("CORRIGE")

            ### SE APERTAR A TECLA "BRANCO": ###
            if TECLA[1] == "BRANCO" and len(voto) > 0:
                BOTOES[10].move(2,2)
                time.sleep(0.13)
                BOTOES[10].move(-2,-2)

                msg.BrancoInvalido(win)


### FUNÇÃO QUE É CHAMADA QUANDO O VOTO PRESIDENCIAL (ÚLTIMO) FOR CONFIRMADO:
def VotoConfirmado(win, BOTOES):
    #Mensagem "Gravando..." que fica abaixo da barra der carregamento:
    gravando = gf.Text(gf.Point(260, 263), f'Gravando...')
    gravando.setSize(12)
    gravando.setFace("helvetica")
    gravando.draw(win)
    #Barra de carregamento:
    barra = gf.Rectangle(gf.Point(180, 240), gf.Point(340, 250))
    barra.setOutline("black")
    barra.setWidth(2)
    barra.draw(win)
    #Parte verde:
    carregamento = gf.Rectangle(gf.Point(182, 242), gf.Point(182, 248))
    carregamento.draw(win)

    win.autoflush=False
    #Repetição que da a sensação de que a barra de carregamento está sendo preenchida:
    x = 1
    while x < 157:
        carregamento.undraw()          
        carregamento = gf.Rectangle(gf.Point(182, 242), gf.Point(182+x, 248))
        carregamento.setOutline("green")
        carregamento.setFill("green")
        carregamento.setWidth(2)
        carregamento.draw(win)
        gf.update(60)
        #time.sleep(0.1)
        
        x += 1

        if x >= 156:
            win.autoflush=True

    carregamento.undraw() # apaga a parte verde.
    barra.undraw() # apaga o retângulo do carregamento.
    gravando.undraw() # apaga a mensagem "Gravando...".

    play_voto() # função que faz o barulho do voto confirmado.

    #Mensagem que exibe o fim do processo de votação:
    fim = gf.Text(gf.Point(260, 190), f'FIM!')
    fim.setSize(35)
    fim.setFace("helvetica")
    fim.draw(win)
    time.sleep(5) # pausa de 5 segundos.

    fim.undraw() # apaga a mensagem

    validar_encerramento = msg.MensagemEncerramento(win)

    if validar_encerramento == "SIM":
        Encerrar(win, BOTOES)

    if validar_encerramento == "NAO":
        (VotacaoPrincipal(win,"Senador",["", ""]))




#FUNÇÃO PARA FAZER O SOM DO VOTO CONFIRMADO:
def play_voto():
    pg.mixer.init() 
    pg.mixer.music.load("Extras/Voto_Confirmado.mp3")
    pg.mixer.music.set_volume(10) 
    pg.mixer.music.play(loops=0)
    
    

#FUNÇÃO QUE EXIBE A TELA DO ENCERRAMENTO:
def Encerrar(win, BOTOES):
    texto = gf.Text(gf.Point(120,130), "DIGITE A SENHA:")
    texto.setSize(16)
    texto.draw(win)

    aperte_tecla = gf.Text(gf.Point(260, 277), f'Aperte a tecla CONFIRMA para VALIDAR a senha.\n Aperte a tecla CORRIGE para REINICIAR a senha.\n\n\n\n\n\n\nAperte a tecla BRANCO para VOLTAR para a votação.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    aperte_tecla.setStyle("bold")
    aperte_tecla.draw(win)

    QUADRADOS = vis.QuadradosEncerrar()
    for item in QUADRADOS:
        item.draw(win)

    ASTERISCOS = vis.AsteriscosEncerrar()

    senha = "999999"
    tentativa_senha = ""

    ValidarSenha = True
    while ValidarSenha:
        clique = win.getMouse()
        posicao_x = clique.getX()
        posicao_y = clique.getY()

        TECLA = val.ValidarClique(posicao_x, posicao_y)

        if TECLA[0] == "NUM" and len(tentativa_senha) < 6:

            BOTOES[int(TECLA[1])].move(2,2)
            time.sleep(0.13)
            BOTOES[int(TECLA[1])].move(-2,-2)

            if len(tentativa_senha) < 6:
                tentativa_senha += TECLA[1]
            if len(tentativa_senha) == 1:
                ASTERISCOS[0].draw(win)
            if len(tentativa_senha) == 2:
                ASTERISCOS[1].draw(win)
            if len(tentativa_senha) == 3:
                ASTERISCOS[2].draw(win)
            if len(tentativa_senha) == 4:
                ASTERISCOS[3].draw(win)
            if len(tentativa_senha) == 5:
                ASTERISCOS[4].draw(win)
            if len(tentativa_senha) == 6:
                ASTERISCOS[5].draw(win)

        if TECLA[0] == "AÇÃO":
            if TECLA[1] == "CONFIRMA":

                BOTOES[12].move(2,2)
                time.sleep(0.13)
                BOTOES[12].move(-2,-2)
                
                if tentativa_senha == senha:
                    for item in ASTERISCOS:
                        item.undraw()

                    for item in QUADRADOS:
                        item.undraw()

                    texto.undraw()

                    aperte_tecla.undraw()

                    ResultadoEleicoes(win)

                else:
                    msg.SenhaIncorreta(win)

                    tentativa_senha = ""

                    for item in ASTERISCOS:
                        item.undraw()

            if TECLA[1] == "CORRIGE":

                BOTOES[11].move(2,2)
                time.sleep(0.13)
                BOTOES[11].move(-2,-2)

                tentativa_senha = ""

                for item in ASTERISCOS:
                    item.undraw()
                
            if TECLA[1] == "BRANCO":
                BOTOES[10].move(2,2)
                time.sleep(0.13)
                BOTOES[10].move(-2,-2)

                for item in ASTERISCOS:
                    item.undraw()
                for item in QUADRADOS:
                    item.undraw()
                
                texto.undraw()

                aperte_tecla.undraw()

                return(VotacaoPrincipal(win, "Senador", ["",""]))


#FUNÇÃO QUE GERA ARQUIVOS COM OS RESULTADOS PRESIDENCIAIS:              
def ResultadoEleicoes(win):
    #Chamo as funções que fazem a contagem e a mudança dos arquivos:
    res.ResultadoPresidentes()
    res.ResultadoSenadores()
    res.ResultadoGovernadores()

    #Chamo as funções que fazem o HTML baseado nos resultados:
    criar_html.HTMLPresidente()
    criar_html.HTMLGovernador()
    criar_html.HTMLSenador()

    #Mensagem:
    processando = gf.Text(gf.Point(260, 263), f'Processando votos...')
    processando.setSize(12)
    processando.setFace("helvetica")
    processando.draw(win)
    #Barra de carregamento:
    barra = gf.Rectangle(gf.Point(160, 240), gf.Point(360, 250))
    barra.setOutline("black")
    barra.setWidth(2)
    barra.draw(win)
    #Parte verde:
    carregamento = gf.Rectangle(gf.Point(162, 242), gf.Point(162, 248))
    carregamento.draw(win)

    win.autoflush = False
    #Repetição que da a sensação de que a barra de carregamento está sendo preenchida:
    x = 1
    while x < 197:
        carregamento.undraw()          
        carregamento = gf.Rectangle(gf.Point(162, 242), gf.Point(162+x, 248))
        carregamento.setOutline("green")
        carregamento.setFill("green")
        carregamento.setWidth(2)
        carregamento.draw(win)
        gf.update(60)
        
        x += 1

        if x >= 196:
            win.autoflush = True

    carregamento.undraw() # apaga a parte verde.
    barra.undraw() # apaga o retângulo do carregamento.
    processando.undraw() # apaga a mensagem "Gravando...".
    play_voto() # função que faz o barulho do voto confirmado.

    #Mensagem que exibe o fim do processo de votação:
    fim = gf.Text(gf.Point(260, 190), f'SESSÃO FINALIZADA!')
    fim.setSize(25)
    fim.setFace("helvetica")
    fim.setStyle("bold")
    fim.draw(win)

    time.sleep(10) # pausa de 10 segundos.

    win.close() # fecha o programa.
        

if __name__ == "__main__":
    VotacaoPrincipal(win, "Senador", ["", ""])