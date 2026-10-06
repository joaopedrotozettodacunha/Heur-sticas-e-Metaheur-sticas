import math
import random
import time

class CaixeiroViajante:

    def __init__(self, cidade, x, y):

        self.cidade = cidade
        self.x = x
        self.y = y

    def distancia(self, cidade_1, cidade_2):

        distancia = math.sqrt(((cidade_2.x - cidade_1.x) ** 2) + ((cidade_2.y - cidade_1.y) ** 2))


        return distancia

    def custo(self, cidades, rota):

        custo = 0

        for i in range(len(rota) - 1):
            custo += self.distancia(rota[i], rota[i+1])


        custo += self.distancia(rota[-1], rota[0])

        return custo

    

    def solucoes_iniciais(self, cidades, qtd_solucoes):

        solucoes = []

        for i in range(qtd_solucoes):
            rota = cidades.copy()
            random.shuffle(rota)

            solucoes.append(rota)

        return solucoes

    def gerar_vizinho(self, rota):

        vizinho = rota.copy()

        cidade_1 = random.randint(0, len(vizinho) - 1)
        cidade_2 = random.randint(0, len(vizinho) - 1)

        while cidade_1 == cidade_2:

            cidade_2 = random.randint(0, len(vizinho) - 1)

        
        auxiliar = vizinho[cidade_1]
        vizinho[cidade_1] = vizinho[cidade_2]
        vizinho[cidade_2] = auxiliar

        return vizinho

class Grasp:

    def __init__(self, tsp, alpha_estatico, graspmax):

        self.tsp = tsp
        self.alpha_estatico = alpha_estatico
        self.graspmax = graspmax
    
    def ConstrucaoGulosaAleatorio(self, alpha_estatico, cidade_inserida):

        lista_candidatos = []
        lista_restrita_candidatos = []
        distancias_cidade_inserida = []

        for c in lista_candidatos:

            distancia = distancia(c, cidade_inserida)
            distancias_cidade_inserida.append(distancia)

        c_min = min(distancias_cidade_inserida)
        c_max = max(distancias_cidade_inserida)

        g_c = c_min + alpha_estatico(c_max - c_min)

        for c, i in enumarate(lista_candidatos):

            if distancias_cidade_inserida[i] <= g_c

            lista_restrita_candidatos.append(c)

        return lista_candidatos


    def aceitar_solucao(self, delta, temperatura):

        if delta < 0:

            return True

        else:

            probabilidade = math.exp(-delta / temperatura)

            return random.random() < probabilidade


    def grasp(self, cidades):

        rota_atual = cidades.copy()
        
        random.shuffle(rota_atual)

        melhor_rota = rota_atual.copy()

        custo_atual = self.tsp.custo(cidades, rota_atual)

        melhor_custo = custo_atual

        temperatura = self.temperatura_inicial

        while temperatura > self.cond_parada:

            for i in range(self.sa_max):

                nova_rota = self.tsp.gerar_vizinho(rota_atual)

                novo_custo = self.tsp.custo(cidades, nova_rota)


                delta = novo_custo - custo_atual


                #decide se aceita o vizinho

                if self.aceitar_solucao(delta, temperatura):

                    rota_atual = nova_rota

                    custo_atual = novo_custo

                    if custo_atual < melhor_custo:

                        melhor_rota = rota_atual.copy()

                        melhor_custo = custo_atual

            temperatura = self.alpha * temperatura

        return melhor_rota, melhor_custo


def main():

    print("Executando: ")

    instancia = open("tsp_51", "r")
    linhas = instancia.readlines()

    cidades = []

    
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

            cidades.append(
                CaixeiroViajante(cidade, x, y)
            )

    instancia.close()


    tsp = CaixeiroViajante(None, None, None)

    sa = Grasp(
    tsp,
    temperatura_inicial=100,
    sa_max=100,
    alpha=0.99,
    cond_parada=0.01
)

    inicio = time.time()

    melhor_rota, melhor_custo = sa.grasp(cidades)

    fim = time.time()

    print("")
    print("Resultado Final")
    print("")

    print("Rota completa:")

    for cidade in melhor_rota:
        print(cidade.cidade, end=" -> ")

    print(melhor_rota[0].cidade)

    print(
        f"Distância total: {melhor_custo:.2f}"
    )

    print(
        f"Tempo de processamento: "
        f"{fim - inicio:.6f} segundos"
    )


main()
    


