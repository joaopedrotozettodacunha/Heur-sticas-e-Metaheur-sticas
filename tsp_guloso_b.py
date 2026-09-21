import time
import random
import math

instancia = open("tsp_51", "r")
linhas = instancia.readlines()

coordenadas = {}

qtd_cidades = 0
inicio_coordenadas = False

for linha in linhas:

    dados = linha.split()

    if dados[0] == "DIMENSION":
        qtd_cidades = int(dados[2])

    if dados[0] == "NODE_COORD_SECTION":
        inicio_coordenadas = True
        continue

    if dados[0] == "EOF":
        break

    if inicio_coordenadas:

        cidade = int(dados[0])
        x = float(dados[1])
        y = float(dados[2])

        coordenadas[cidade] = (x, y)

def distancia(cidade1, cidade2, coordenadas):

    x1, y1 = coordenadas[cidade1]
    x2, y2 = coordenadas[cidade2]

    distancia = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

    return distancia

def solucao_inicial(qtd_cidades):

    sol_inicial = list(range(1, qtd_cidades + 1))

    random.shuffle(sol_inicial)

    return sol_inicial


def avaliacao(solucao, coordenadas):

    distancia_total = 0
    for i in range(len(solucao) - 1):

        cidade_atual = solucao[i]
        proxima_cidade = solucao[i + 1]

        distancia_total += distancia(
            cidade_atual,
            proxima_cidade,
            coordenadas
        )

    
    distancia_total += distancia(
        solucao[-1],
        solucao[0],
        coordenadas
    )

    return distancia_total

def operador_vizinhanca(solucao, posicao1, posicao2):

    vizinho = solucao.copy()

    vizinho[posicao1:posicao2 + 1] = reversed(
        vizinho[posicao1:posicao2 + 1]
    )

    return vizinho


def vizinho_mais_proximo(coordenadas, qtd_cidades, cidade_inicial):

    visitadas = set()
    rota = []

    cidade_atual = cidade_inicial

    rota.append(cidade_atual)
    visitadas.add(cidade_atual)

    while len(rota) < qtd_cidades:

        cidades = sorted(
            coordenadas.keys(),
            key=lambda cidade: distancia(
                cidade_atual,
                cidade,
                coordenadas
            ),
            reverse = True
        )

        for cidade in cidades:

            if cidade not in visitadas:

                rota.append(cidade)
                visitadas.add(cidade)

                cidade_atual = cidade

                break

    rota.append(cidade_inicial)

    return rota



def main():

    inicio = time.time()

    solucao = vizinho_mais_proximo(
        coordenadas,
        qtd_cidades,
        1
    )

    fim = time.time()

    distancia_final = avaliacao(
        solucao,
        coordenadas
    )

    print("")
    print("Resultado Final")
    print("")


    
    print(
        "Rota completa:",
        solucao
    )

    print(
        f"Distância total: "
        f"{distancia_final:.2f}"
    )

    print(
        f"Tempo de processamento: "
        f"{fim - inicio:.15f} segundos"
    )

main()