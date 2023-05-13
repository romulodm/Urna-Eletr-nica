from Codigos import arquivos as arq

### FUNÇÕES QUE CRIAM ARQUIVOS COM OS RESULTADOS DAS ELEIÇÕES (NUM DE VOTOS E PERCENTUAIS DE CADA CANDIDATO): ###

def ResultadoPresidentes():
    arquivo = open("Arquivos/Contagem/contagem_presidentes.csv", "r", encoding="utf-8")
    conteudo = arquivo.readlines()
    arquivo.close()

    lista = []
    for item in conteudo:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    total_votos = 0

    for item in lista:
        numero = int(item[1])
        total_votos += numero

    lista_porcentagem = []

    for item in lista:
        if int(item[1]) > 0:
            porcentagem = int(item[1]) / total_votos * 100
            lista_porcentagem.append(f"{item[0]};{porcentagem:.2f}%")
        else:
            lista_porcentagem.append(f"{item[0]};0.00%")

    candidatos = arq.ArquivoPresidentes()

    outra_lista = []

    n = 0
    for item in lista_porcentagem:
        uma_lista = item.split(";")

        if uma_lista[0] != "NULO" and uma_lista[0] != "BRANCO":
            nome_candidato = candidatos[uma_lista[0]][0]
            partido_candidato = candidatos[uma_lista[0]][1]

            outra_lista.append(f'{uma_lista[0]};{nome_candidato};{partido_candidato};{lista[n][1]};{uma_lista[1]}')

        n += 1


    porcentagem_nulo = lista_porcentagem[0].split(";")
    porcentagem_branco = lista_porcentagem[1].split(";")

    outra_lista.append(f'Votos Nulos: {lista[0][1]} ({porcentagem_nulo[1]})')
    outra_lista.append(f'Votos Brancos: {lista[1][1]} ({porcentagem_branco[1]})')
    outra_lista.append(f'Total de Votos: {total_votos}')

    string_resultado = ""

    for item in outra_lista:
        string_resultado += item
        string_resultado += "\n"

    arquivo = open("Arquivos/Resultados/resultado_presidentes.csv", "w", encoding="utf-8")
    arquivo.write(string_resultado)
    arquivo.close()

def ResultadoGovernadores():
    arquivo = open("Arquivos/Contagem/contagem_governadores.csv", "r", encoding="utf-8")
    conteudo = arquivo.readlines()
    arquivo.close()

    lista = []

    for item in conteudo:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    total_votos = 0

    for item in lista:
        numero = int(item[1])
        total_votos += numero

    lista_porcentagem = []

    for item in lista:
        if int(item[1]) > 0:
            porcentagem = int(item[1]) / total_votos * 100
            lista_porcentagem.append(f"{item[0]};{porcentagem:.2f}%")
        else:
            lista_porcentagem.append(f"{item[0]};0.00%")

    candidatos = arq.ArquivoGovernadores()

    outra_lista = []

    n = 0
    for item in lista_porcentagem:
        uma_lista = item.split(";")

        if uma_lista[0] != "NULO" and uma_lista[0] != "BRANCO":
            nome_candidato = candidatos[uma_lista[0]][0]
            partido_candidato = candidatos[uma_lista[0]][1]

            outra_lista.append(f'{uma_lista[0]};{nome_candidato};{partido_candidato};{lista[n][1]};{uma_lista[1]}')

        n += 1


    porcentagem_nulo = lista_porcentagem[0].split(";")
    porcentagem_branco = lista_porcentagem[1].split(";")

    outra_lista.append(f'Votos Nulos: {lista[0][1]} ({porcentagem_nulo[1]})')
    outra_lista.append(f'Votos Brancos: {lista[1][1]} ({porcentagem_branco[1]})')
    outra_lista.append(f'Total de Votos: {total_votos}')

    string_resultado = ""

    for item in outra_lista:
        string_resultado += item
        string_resultado += "\n"

    arquivo = open("Arquivos/Resultados/resultado_governadores.csv", "w", encoding="utf-8")
    arquivo.write(string_resultado)
    arquivo.close()

def ResultadoSenadores():
    arquivo = open("Arquivos/Contagem/contagem_senadores.csv", "r", encoding="utf-8")
    conteudo = arquivo.readlines()
    arquivo.close()

    lista = []

    for item in conteudo:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    total_votos = 0

    for item in lista:
        numero = int(item[1])
        total_votos += numero

    lista_porcentagem = []

    for item in lista:
        if int(item[1]) > 0:
            porcentagem = int(item[1]) / total_votos * 100
            lista_porcentagem.append(f"{item[0]};{porcentagem:.2f}%")
        else:
            lista_porcentagem.append(f"{item[0]};0.00%")

    candidatos = arq.ArquivoSenadores()

    outra_lista = []

    n = 0
    for item in lista_porcentagem:
        uma_lista = item.split(";")

        if uma_lista[0] != "NULO" and uma_lista[0] != "BRANCO":
            nome_candidato = candidatos[uma_lista[0]][0]
            partido_candidato = candidatos[uma_lista[0]][1]

            outra_lista.append(f'{uma_lista[0]};{nome_candidato};{partido_candidato};{lista[n][1]};{uma_lista[1]}')

        n += 1


    porcentagem_nulo = lista_porcentagem[0].split(";")
    porcentagem_branco = lista_porcentagem[1].split(";")

    outra_lista.append(f'Votos Nulos: {lista[0][1]} ({porcentagem_nulo[1]})')
    outra_lista.append(f'Votos Brancos: {lista[1][1]} ({porcentagem_branco[1]})')
    outra_lista.append(f'Total de Votos: {total_votos}')

    string_resultado = ""

    for item in outra_lista:
        string_resultado += item
        string_resultado += "\n"

    arquivo = open("Arquivos/Resultados/resultado_senadores.csv", "w", encoding="utf-8")
    arquivo.write(string_resultado)
    arquivo.close()