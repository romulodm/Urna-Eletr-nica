### FUNÇÕES QUE CRIAM STRINGS, QUE VIRAM  ARQUIVOS (PÁGINAS HTML): ###

def HTMLPresidente():
    #PEGO AS INFORMAÇÕES DO ARQUIVO DOS RESULTADOS:
    arquivo = open("Arquivos/Resultados/resultado_presidentes.csv", "r", encoding="utf-8")
    LISTA = arquivo.readlines()
    arquivo.close()

    #FAÇO CADA LINHA DO ARQUIVO VIRAR UMA SUBLISTA:
    lista = []
    for item in LISTA:
        uma_lista = item.split("\n")
        lista.append(uma_lista)

    #REMOVO UM ESPAÇO EM BRANCO QUE FICOU EM CADA SUBLISTA:
    LISTA = []  
    for item in lista:
        item.pop()
        LISTA.append(item)

    #FAÇO UM SPLIT(;) NESSA SUBLISTA, E ADICIONO CADA ELEMENTO DELA NA "LISTA RESULTADO":
    LISTA_RESULTADO = []
    for item in LISTA:
        uma_lista = item[0].split(";")
        for item in uma_lista:
            LISTA_RESULTADO.append(item)

    #PEGO O NÚMERO, UTILIZADO PARA ACHAR O ÚLTIMO ELEMENTO DESSA LISTA (VOTOS TOTAIS):
    num = len(LISTA_RESULTADO) - 1

    #COMEÇO A CRIAR A STRING DO "HTML", QUE VAI VIRAR UM ARQUIVO DEPOIS:
    primeira_string = f"<html>\n\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-wdith, initial-scale=1.0\">\n<link rel=\"shortcut icon\" href=\"Extras/brasil.ico\" type=\"image/x-icon\">\n<link rel=\"stylesheet\" href=\"./CSS/style.css\">\n<title>Resultado das Eleições</title>\n</head>\n\n<body>\n\n<header>\n\n<div class=\"banner\" id=\"banner\">\n<div class=\"navegacao\">\n<ul>\n<li><a href=\"\"></a></li>\n<li><a href=\"./index.html\">Resultado Presidencial</a></li>\n<li><a href=\"./Paginas/governadores.html\">Resultado Governadores</a></li>\n<li><a href=\"./Paginas/senadores.html\">Resultado Senadores</a></li>\n</ul>\n</div>\n</header>\n\n<main>\n<div class=\"body\">\n<div class=\"banner-superior\"></div>\n<hr class=\"barra\">\n<h1 class=\"conteudo-title\">Resultados Presidenciais</h1>\n\n<div class=\"conteudo-background\">\n<br>\n<div class=\"conteudo\">\n<div class=\"texto\">\n"

    #ADICIONO O {LISTA_RESULTADO[num]} NO SEU DEVIDO LUGAR: (Votos totais: ....)    
    string = primeira_string +  f"<p>{LISTA_RESULTADO[num]}</p>\n</div>\n<br>\n<table>\n\n<thead>\n\n<th>Número</th>\n<th>Candidato</th>\n<th>Partido</th>\n<th>Quantidade de Votos</th>\n<th>Porcentagem</th>\n\n</thead>\n"

    #FAÇO O CÁLCULO PRA SABER QUANTAS LINHAS A TABELA VAI TER:
    ultimo_indice = num / 5

    #INICIO A CONCATENAÇÃO DAS LINHAS DA TABELA, NA STRING DO HTML:
    indice = 0
    for i in range(0, int(ultimo_indice)):
        string += "\n<tr>\n"
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += "</tr>\n"

    #ADICIONO MAIS ELEMENTOS NA STRING:
    string += "\n</table>\n\n<div class=\"texto\">\n"

    #ADICIONO OS "Votos Nulos: ..." E "Votos Brancos...", E FECHO AS TAGS, FINALIZANDO O HTML:
    ultima_string = string + f"<p>{LISTA_RESULTADO[num-1]}</p>\n<br>\n<p>{LISTA_RESULTADO[num-2]}</p>\n<br>\n</div>\n\n</div>\n\n</div>\n\n</div>\n\n</main>\n\n</body>\n\n</html>"

    #MODIFICO O ARQUIVO HTML COM AS DEVIDAS INFORMAÇÕES:
    arquivo = open("index.html", "w", encoding="utf-8")
    arquivo.write(ultima_string)
    arquivo.close()



#MESMO FUNÇÃO, MAS PEGANDO O RESULTADO DOS GOVERNADORES E MODIFICANDO O ARQUIVO HTML REFERENTE AOS GOVERNADORES:
def HTMLGovernador():
    
    arquivo = open("Arquivos/Resultados/resultado_governadores.csv", "r", encoding="utf-8")
    LISTA = arquivo.readlines()
    arquivo.close()

    lista = []
    for item in LISTA:
        uma_lista = item.split("\n")
        lista.append(uma_lista)

    LISTA = []  

    for item in lista:
        item.pop()
        LISTA.append(item)

    LISTA_RESULTADO = []

    for item in LISTA:
        uma_lista = item[0].split(";")
        for item in uma_lista:
            LISTA_RESULTADO.append(item)

    num = len(LISTA_RESULTADO) - 1

    primeira_string = f"<html>\n\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-wdith, initial-scale=1.0\">\n<link rel=\"shortcut icon\" href=\"../Extras/brasil.ico\" type=\"image/x-icon\">\n<link rel=\"stylesheet\" href=\"../CSS/style.css\">\n<title>Resultado das Eleições</title>\n</head>\n\n<body>\n\n<header>\n<div class=\"banner\" id=\"banner\">\n<div class=\"navegacao\">\n<ul>\n<li><a href=\"\"></a></li>\n<li><a href=\"../index.html\">Resultado Presidencial</a></li>\n<li><a href=\"./governadores.html\">Resultado Governadores</a></li>\n<li><a href=\"./senadores.html\">Resultado Senadores</a></li>\n</ul>\n</div>\n</header>\n\n<main>\n<div class=\"body\">\n<div class=\"banner-superior\"></div>\n<hr class=\"barra\">\n<h1 class=\"conteudo-title\">Resultados Governamentais</h1>\n\n<div class=\"conteudo-background\">\n<br>\n<div class=\"conteudo\">\n<div class=\"texto\">\n"
        
    string = primeira_string +  f"<p>{LISTA_RESULTADO[num]}</p>\n</div>\n<br>\n<table>\n\n<thead>\n\n<th>Número</th>\n<th>Candidato</th>\n<th>Partido</th>\n<th>Quantidade de Votos</th>\n<th>Porcentagem</th>\n\n</thead>\n"

    ultimo_indice = num / 5

    indice = 0
    for i in range(0, int(ultimo_indice)):
        string += "\n<tr>\n"
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += "</tr>\n"

    string += "\n</table>\n\n<div class=\"texto\">\n"

    ultima_string = string + f"<p>{LISTA_RESULTADO[num-1]}</p>\n<br>\n<p>{LISTA_RESULTADO[num-2]}</p>\n<br>\n</div>\n\n</div>\n\n</div>\n\n</div>\n\n</main>\n\n</body>\n\n</html>"

    arquivo = open("Paginas/governadores.html", "w", encoding="utf-8")
    arquivo.write(ultima_string)
    arquivo.close()



#MESMO FUNÇÃO, MAS PEGANDO O RESULTADO DOS SENADORES E MODIFICANDO O ARQUIVO HTML REFERENTE AOS SENADORES:
def HTMLSenador():

    arquivo = open("Arquivos/Resultados/resultado_senadores.csv", "r", encoding="utf-8")
    LISTA = arquivo.readlines()
    arquivo.close()

    lista = []
    for item in LISTA:
        uma_lista = item.split("\n")
        lista.append(uma_lista)

    LISTA = []  

    for item in lista:
        item.pop()
        LISTA.append(item)

    LISTA_RESULTADO = []

    for item in LISTA:
        uma_lista = item[0].split(";")
        for item in uma_lista:
            LISTA_RESULTADO.append(item)

    num = len(LISTA_RESULTADO) - 1

    primeira_string = f"<html>\n\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-wdith, initial-scale=1.0\">\n<link rel=\"shortcut icon\" href=\"../Extras/brasil.ico\" type=\"image/x-icon\">\n<link rel=\"stylesheet\" href=\"../CSS/style.css\">\n<title>Resultado das Eleições</title>\n</head>\n\n<body>\n\n<header>\n<div class=\"banner\" id=\"banner\">\n<div class=\"navegacao\">\n<ul>\n<li><a href=\"\"></a></li>\n<li><a href=\"../index.html\">Resultado Presidencial</a></li>\n<li><a href=\"./governadores.html\">Resultado Governadores</a></li>\n<li><a href=\"./senadores.html\">Resultado Senadores</a></li>\n\n</ul>\n</div>\n</header><main>\n<div class=\"body\">\n<div class=\"banner-superior\"></div>\n<hr class=\"barra\">\n<h1 class=\"conteudo-title\">Resultados do Senado</h1>\n\n<div class=\"conteudo-background\">\n<br>\n<div class=\"conteudo\">\n<div class=\"texto\">\n"
        
    string = primeira_string +  f"<p>{LISTA_RESULTADO[num]}</p>\n</div>\n<br>\n<table>\n\n<thead>\n\n<th>Número</th>\n<th>Candidato</th>\n<th>Partido</th>\n<th>Quantidade de Votos</th>\n<th>Porcentagem</th>\n\n</thead>\n"

    ultimo_indice = num / 5

    indice = 0
    for i in range(0, int(ultimo_indice)):
        string += "\n<tr>\n"
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += f"<td>{LISTA_RESULTADO[indice]}</td>\n"
        indice += 1
        string += "</tr>\n"

    string += "\n</table>\n\n<div class=\"texto\">\n"

    ultima_string = string + f"<p>{LISTA_RESULTADO[num-1]}</p>\n<br>\n<p>{LISTA_RESULTADO[num-2]}</p>\n<br>\n</div>\n\n</div>\n\n</div>\n\n</div>\n\n</main>\n\n</body>\n\n</html>"

    arquivo = open("Paginas/senadores.html", "w", encoding="utf-8")
    arquivo.write(ultima_string)
    arquivo.close()
