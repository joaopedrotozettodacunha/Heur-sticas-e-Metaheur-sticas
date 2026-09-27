import math
import random

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

class SimmulatedAnnealing:

    def __init__(self, temperatura_inicial, sa_max, alpha, cond_parada):


        self.temperatura_inicial = temperatura_inicial
        self.sa_max = sa_max
        self.alpha = alpha
        self.cond_parada = cond_parada


    def aceitar_solucao(self, delta, temperatura):

        if delta < 0:

            return True

        else:

            probabilidade = math.exp(-delta / temperatura)

            return random.random() < probabilidade
    




