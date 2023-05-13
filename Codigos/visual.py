from Graphics import graphics as gf

### TODA A PARTE VISUAL DA URNA: ###
#OBS.: SÃO FUNÇÕES QUE CRIAM LISTAS DE OBJETOS, QUE SERÃO DESENHADAS CONFORME A NECESSIDADE:

def QuadradosVoto(cargo):

    LISTA_QUADRADOS = []

    if cargo == "Senador":
        primeiro_quadrado = gf.Rectangle(gf.Point(45, 135), gf.Point(85, 175))
        LISTA_QUADRADOS.append(primeiro_quadrado)
        segundo_quadrado = gf.Rectangle(gf.Point(95, 135), gf.Point(135, 175))
        LISTA_QUADRADOS.append(segundo_quadrado)
        terceiro_quadrado = gf.Rectangle(gf.Point(145, 135), gf.Point(185, 175))
        LISTA_QUADRADOS.append(terceiro_quadrado)

    #Presidente:
    else:
        primeiro_quadrado = gf.Rectangle(gf.Point(70, 135), gf.Point(110, 175))
        LISTA_QUADRADOS.append(primeiro_quadrado)
        segundo_quadrado = gf.Rectangle(gf.Point(120, 135), gf.Point(160, 175))
        LISTA_QUADRADOS.append(segundo_quadrado)

    return(LISTA_QUADRADOS)


def DigitosVoto():
    DIGITOS = []
    prim_digito = gf.Text(gf.Point(90, 155), "")
    DIGITOS.append(prim_digito)
    seg_digito = gf.Text(gf.Point(140, 155), "")
    DIGITOS.append(seg_digito)
    terc_digito = gf.Text(gf.Point(190, 155), "")
    DIGITOS.append(terc_digito) 

    return(DIGITOS)


#TODA A PARTE VISUAL, QUE É DESENHADA NA JANELA E FICA FIXA:
def VisualUrna(cargo):
    VISUAL_URNA = []
    
    #Quadrado onde os números ficam:
    teclado_numerico = gf.Rectangle(gf.Point(530, 70), gf.Point(770, 350))
    teclado_numerico.setFill("#453F3C")
    teclado_numerico.setWidth(0)
    VISUAL_URNA.append(teclado_numerico)
    #Tela onde as informações são exibidas: 
    tela = gf.Rectangle(gf.Point(20, 40), gf.Point(520, 340))
    tela.setOutline("black")
    tela.setFill("white")
    tela.setWidth(2)
    VISUAL_URNA.append(tela)
    #Imagem que fica acima do teclado numérico com "Justiça Eleitoral" escrita:
    justica_eleitoral = gf.Image(gf.Point(650, 60), "Imagens/justiçaeleitoral.png")
    VISUAL_URNA.append(justica_eleitoral)
    voto_para = gf.Text(gf.Point(115, 75),f"SEU VOTO PARA:\n{cargo}")
    voto_para.setSize(14)
    voto_para.setOutline("BLACK")
    voto_para.setFace("helvetica")
    VISUAL_URNA.append(voto_para)

    return(VISUAL_URNA)


### FUNÇÃO QUE CRIA UM LISTA COM AS IMAGENS DOS BOTÕES: ###
def ImagemBotoes():
    LISTA_BOTOES = []
    LISTA_BOTOES.append(gf.Image(gf.Point(650, 265),"Imagens/Botoes/numero0.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(575, 115),"Imagens/Botoes/numero1.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(650, 115),"Imagens/Botoes/numero2.png")) 
    LISTA_BOTOES.append(gf.Image(gf.Point(725, 115),"Imagens/Botoes/numero3.png"))     
    LISTA_BOTOES.append(gf.Image(gf.Point(575, 165),"Imagens/Botoes/numero4.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(650, 165),"Imagens/Botoes/numero5.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(725, 165),"Imagens/Botoes/numero6.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(575, 215),"Imagens/Botoes/numero7.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(650, 215),"Imagens/Botoes/numero8.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(725, 215),"Imagens/Botoes/numero9.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(570, 320),"Imagens/Botoes/BRANCO.png"))
    LISTA_BOTOES.append(gf.Image(gf.Point(650, 320),"Imagens/Botoes/CORRIGE.png"))          
    LISTA_BOTOES.append(gf.Image(gf.Point(730, 320),"Imagens/Botoes/CONFIRMA.png"))

    return(LISTA_BOTOES)


### UMA LISTA COM TUDO QUE APARECE NA TELA QUANDO O VOTO SERÁ NULO: ###
def MostraNulo():
    LISTA_NULO = []
    numero_errado = gf.Text(gf.Point(118, 215), f'NÚMERO ERRADO:')
    numero_errado.setSize(14)
    LISTA_NULO.append(numero_errado)
    voto_nulo = gf.Text(gf.Point(260, 260), f'VOTO NULO')
    voto_nulo.setSize(20)
    voto_nulo.setStyle("bold")
    LISTA_NULO.append(voto_nulo)
    linha_horizontal = gf.Line(gf.Point(20, 305), gf.Point(520, 305))
    LISTA_NULO.append(linha_horizontal)
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_NULO.append(aperte_tecla)

    return(LISTA_NULO)


### UMA LISTA COM TUDO QUE APARECE NA TELA QUANDO O VOTO É BRANCO: ###
def VotoBranco():
    LISTA_BRANCO = []
    #Mensagem que avisa que o voto será branco:
    voto_branco = gf.Text(gf.Point(260, 200), f'VOTO EM BRANCO')
    voto_branco.setSize(30)
    voto_branco.setStyle("bold")
    LISTA_BRANCO.append(voto_branco)
    #Linha horizontal que passa por toda a tela:
    linha_horizontal = gf.Line(gf.Point(20, 305), gf.Point(520, 305))
    LISTA_BRANCO.append(linha_horizontal)
    #Mensagem que avisa que é necessário apertar a tecla "CORRIGE" ou "CONFIRMA":
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")  
    LISTA_BRANCO.append(aperte_tecla)

    return(LISTA_BRANCO)


def QuadradosEncerrar():
    QUADRADOS = []
    QUADRADOS.append(gf.Rectangle(gf.Point(115, 170), gf.Point(155, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(165, 170), gf.Point(205, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(215, 170), gf.Point(255, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(265, 170), gf.Point(305, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(315, 170), gf.Point(355, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(365, 170), gf.Point(405, 210)))
    return(QUADRADOS)


def AsteriscosEncerrar():
    ASTERISCOS = []
    ASTERISCOS.append(gf.Text(gf.Point(135, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(185, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(235, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(285, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(335, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(385, 195), "*"))
    for item in ASTERISCOS:
        item.setSize(25)

    return(ASTERISCOS)


