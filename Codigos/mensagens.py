from Graphics import graphics as gf
import time

### MENSAGENS DE AVISOS QUE SÃO MOSTRADAS NA TELA: ###

#Função que cria uma lista com obejtos:
def MensagemErro(mensagem):
    ELEMENTOS_MENSAGEM = []
    apagar = gf.Rectangle(gf.Point(21, 45), gf.Point(518, 335))
    apagar.setFill("white")
    apagar.setOutline("white")
    ELEMENTOS_MENSAGEM.append(apagar)
    caixa_mensagem = gf.Rectangle(gf.Point(160, 130), gf.Point(360, 230))
    caixa_mensagem.setFill("#453F3C")
    ELEMENTOS_MENSAGEM.append(caixa_mensagem)

    #Mensagem da senha errada:
    if mensagem == "SENHA":
        mensagem = gf.Text(gf.Point(260, 160), "Senha incorreta, digite\nnovamente!")
        mensagem.setSize(13)
        mensagem.setOutline("white")
        ELEMENTOS_MENSAGEM.append(mensagem)

    #Mensagem do "BRANCO" errado:
    if mensagem == "BRANCO":
        mensagem = gf.Text(gf.Point(260, 160), "Para votar em BRANCO o\ncampo de voto deve estar vazio.")
        mensagem.setSize(10)
        mensagem.setOutline("white")
        ELEMENTOS_MENSAGEM.append(mensagem)

    #Mensagem do "CORRIGE" errado:
    if mensagem == "CORRIGE":
        mensagem = gf.Text(gf.Point(260, 160), "Para utilizar o CORRIGE você\ndeve digitar algum número\nou votar em BRANCO.")
        mensagem.setSize(10)
        mensagem.setOutline("white")
        ELEMENTOS_MENSAGEM.append(mensagem)

    #Mensagem do "CONFIRMA" errado:
    if mensagem == "CONFIRMA":
        mensagem = gf.Text(gf.Point(260, 160), "Para CONFIRMAR você deve\npreencher o campo de votação\nou votar em BRANCO.")
        mensagem.setSize(10)
        mensagem.setOutline("white")
        ELEMENTOS_MENSAGEM.append(mensagem)

    if mensagem == "ENCERRAR":
        mensagem = gf.Text(gf.Point(260, 160), "Você deseja encerrar a votação?")
        mensagem.setSize(10)
        mensagem.setOutline("white")
        ELEMENTOS_MENSAGEM.append(mensagem)

        botao = gf.Rectangle(gf.Point(210, 200), gf.Point(250, 220))
        botao.setFill("green")
        botao.setOutline("white")
        ELEMENTOS_MENSAGEM.append(botao)
        sim = gf.Text(gf.Point(230, 210), "SIM")
        sim.setStyle("bold")
        sim.setOutline("white")
        sim.setSize(10)
        ELEMENTOS_MENSAGEM.append(sim)

        sec_botao = gf.Rectangle(gf.Point(270, 200), gf.Point(310, 220))
        sec_botao.setFill("RED")
        sec_botao.setOutline("white")
        ELEMENTOS_MENSAGEM.append(sec_botao)
        nao = gf.Text(gf.Point(291, 210), "NÃO")
        nao.setStyle("bold")
        nao.setOutline("white")
        nao.setSize(10)
        ELEMENTOS_MENSAGEM.append(nao)


    elif mensagem != "ENCERRAR":
        botao = gf.Rectangle(gf.Point(240, 200), gf.Point(280, 220))
        botao.setFill("green")
        botao.setOutline("white")
        ELEMENTOS_MENSAGEM.append(botao)
        ok = gf.Text(gf.Point(260, 210), "OK")
        ok.setOutline("white")
        ok.setSize(10)
        ELEMENTOS_MENSAGEM.append(ok)


    return(ELEMENTOS_MENSAGEM)


#Função que exibe a mensagem da senha errada e espera o clique no "OK":
def SenhaIncorreta(win):
    ELEMENTOS_MENSAGEM = MensagemErro("SENHA")

    for item in ELEMENTOS_MENSAGEM:
        item.draw(win)

    while True:
        clique = win.getMouse()
        X = clique.getX()
        Y = clique.getY()
        
        if X > 240 and X < 280 and Y > 200 and Y < 220:
            ELEMENTOS_MENSAGEM[3].move(2,2)
            ELEMENTOS_MENSAGEM[4].move(2,2)
            time.sleep(0.13)
            ELEMENTOS_MENSAGEM[3].move(-2,-2)
            ELEMENTOS_MENSAGEM[4].move(-2,-2)
            
            for item in ELEMENTOS_MENSAGEM:
                item.undraw()

            return()


#Função que exibe a mensagem do branco inválido e espera o clique no "OK":
def BrancoInvalido(win):
    ELEMENTOS_MENSAGEM = MensagemErro("BRANCO")

    for item in ELEMENTOS_MENSAGEM:
        item.draw(win)

    while True:
        clique = win.getMouse()
        X = clique.getX()
        Y = clique.getY()
        
        if X > 240 and X < 280 and Y > 200 and Y < 220:
            ELEMENTOS_MENSAGEM[3].move(2,2)
            ELEMENTOS_MENSAGEM[4].move(2,2)
            time.sleep(0.13)
            ELEMENTOS_MENSAGEM[3].move(-2,-2)
            ELEMENTOS_MENSAGEM[4].move(-2,-2)
            
            for item in ELEMENTOS_MENSAGEM:
                item.undraw()

            return()


#Função que exibe a mensagem do corrige inválido e espera o clique no "OK":
def CorrigeInvalido(win):
    ELEMENTOS_MENSAGEM = MensagemErro("CORRIGE")

    for item in ELEMENTOS_MENSAGEM:
        item.draw(win)

    while True:
        clique = win.getMouse()
        X = clique.getX()
        Y = clique.getY()
        
        if X > 240 and X < 280 and Y > 200 and Y < 220:
            ELEMENTOS_MENSAGEM[3].move(2,2)
            ELEMENTOS_MENSAGEM[4].move(2,2)
            time.sleep(0.13)
            ELEMENTOS_MENSAGEM[3].move(-2,-2)
            ELEMENTOS_MENSAGEM[4].move(-2,-2)
            
            for item in ELEMENTOS_MENSAGEM:
                item.undraw()

            return()


#Função que exibe a mensagem do confirma errado e espera o clique no "OK":
def ConfirmaInvalido(win):
    ELEMENTOS_MENSAGEM = MensagemErro("CONFIRMA")

    for item in ELEMENTOS_MENSAGEM:
        item.draw(win)

    while True:
        clique = win.getMouse()
        X = clique.getX()
        Y = clique.getY()
        
        if X > 240 and X < 280 and Y > 200 and Y < 220:
            ELEMENTOS_MENSAGEM[3].move(2,2)
            ELEMENTOS_MENSAGEM[4].move(2,2)
            time.sleep(0.13)
            ELEMENTOS_MENSAGEM[3].move(-2,-2)
            ELEMENTOS_MENSAGEM[4].move(-2,-2)
            
            for item in ELEMENTOS_MENSAGEM:
                item.undraw()

            return()

def MensagemEncerramento(win):
    ELEMENTOS_MENSAGEM = MensagemErro("ENCERRAR")

    for item in ELEMENTOS_MENSAGEM:
        item.draw(win)

    while True:
        clique = win.getMouse()
        X = clique.getX()
        Y = clique.getY()
        
        if X > 210 and X < 250 and Y > 200 and Y < 220:
            ELEMENTOS_MENSAGEM[3].move(2,2)
            ELEMENTOS_MENSAGEM[4].move(2,2)
            time.sleep(0.13)
            ELEMENTOS_MENSAGEM[3].move(-2,-2)
            ELEMENTOS_MENSAGEM[4].move(-2,-2)
            
            for item in ELEMENTOS_MENSAGEM:
                item.undraw()

            return("SIM")


        if X > 270 and X < 310 and Y > 200 and Y < 220:
            ELEMENTOS_MENSAGEM[5].move(2,2)
            ELEMENTOS_MENSAGEM[6].move(2,2)
            time.sleep(0.13)
            ELEMENTOS_MENSAGEM[5].move(-2,-2)
            ELEMENTOS_MENSAGEM[6].move(-2,-2)


            for item in ELEMENTOS_MENSAGEM:
                item.undraw()

            return("NAO")