"""

FUNÇÃO QUE VALIDA O CLIQUE DO USUÁRIO, OU SEJA, PEGA AS 
COORDENADAS E RETORNA UM VALOR QUE CONDIZ COM A POSIÇÃO DO CLIQUE:

"""


def ValidarClique(X, Y):
    #Números:
    if X > 550 and X < 600 and Y > 100 and Y < 130: #1
        return(["NUM","1"])
    if X > 625 and X < 675 and Y > 100 and Y < 130: #2
        return(["NUM","2"])
    if X > 700 and X < 750 and Y > 100 and Y < 130: #3
        return(["NUM","3"])
    if X > 550 and X < 600 and Y > 150 and Y < 180: #4
        return(["NUM","4"])
    if X > 625 and X < 675 and Y > 150 and Y < 180: #5
        return(["NUM","5"])
    if X > 700 and X < 750 and Y > 150 and Y < 180: #6
        return(["NUM","6"])
    if X > 550 and X < 600 and Y > 200 and Y < 230: #7
        return(["NUM","7"])
    if X > 625 and X < 675 and Y > 200 and Y < 230: #8
        return(["NUM","8"])
    if X > 700 and X < 750 and Y > 200 and Y < 230: #9
        return(["NUM","9"])
    if X > 625 and X < 675 and Y > 250 and Y < 280: #0
        return(["NUM","0"])
    #Ações:
    if X  > 540 and X < 600 and Y > 300 and Y < 340: #BRANCO
        return(["AÇÃO", "BRANCO"])
    if X > 620 and X < 680 and Y > 300 and Y < 340: #CORRIGE
        return(["AÇÃO", "CORRIGE"])
    if X > 700 and X < 760 and Y > 300 and Y < 340: #CONFIRMA
        return(["AÇÃO", "CONFIRMA"])
    if X > 220 and X < 300 and Y > 345 and Y < 365: #ENCERRAR
        return(["AÇÃO", "ENCERRAR"])
    #Clique inválido:
    else:
        return("NADA")