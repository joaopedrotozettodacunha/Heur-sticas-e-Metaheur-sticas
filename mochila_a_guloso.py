import time
import random

instancia = open("mochila_4_20", "r")
linhas = instancia.readlines()

primeira_linha = linhas[0]
dados = primeira_linha.split() #split transforma em string

qtd_itens = int(dados[0])
capacidade_max = int(dados[1])

valores = []
pesos = []

for linha in linhas[1:]:

    dados = linha.split()
    valor = int(dados[0])
    peso = int(dados[1])

    valores.append(valor)
    pesos.append(peso)


def solucao_inicial(qtd_itens, pesos, capacidade):

    while True: #se ultrapassar a capacidade, a solução atual é descartada

        sol_inicial = []
        peso_total = 0

        for i in range(qtd_itens):
            valor = random.choice([0, 1])
            sol_inicial.append(valor)

        for i in range(qtd_itens):
            if sol_inicial[i] == 1:
                peso_total += pesos[i]

        if peso_total <= capacidade:
            return sol_inicial
    
def avaliacao(qtd_itens, valores, sol_inicial):

    valor_objetivo = 0

    for i in range(qtd_itens):
                if sol_inicial[i] == 1:
                    valor_objetivo += valores[i]

    return valor_objetivo

def verificar_capacidade(qtd_itens, pesos, capacidade, solucao):
     
    peso_total = 0
     
    for i in range(qtd_itens):
        if solucao[i] == 1:
            peso_total += pesos[i]
    
    if peso_total <= capacidade:
         return True
    else: 
         return False
     


def operador_vizinhanca(sol_inicial, posicao_alterada):

    vizinho = sol_inicial.copy()

    if vizinho[posicao_alterada] == 0:
        vizinho[posicao_alterada] = 1
    else:
        vizinho[posicao_alterada] = 0

    return vizinho


def custo_beneficio(qtd_itens, pesos, valores, capacidade):

    peso_total = 0

    solucao = [0] * qtd_itens
    
    custo_beneficio = []

    for item in range(qtd_itens):
        beneficio_item = valores[item] / pesos[item]
        custo_beneficio.append(beneficio_item)

    itens = sorted(
        range(qtd_itens),
        key=lambda i: custo_beneficio[i],
        reverse=True
    )

    for item in itens:
        if peso_total + pesos[item] <= capacidade:
            solucao[item] = 1
            peso_total += pesos[item]

    return solucao





def main():

    inicio = time.time()

    solucao = custo_beneficio(
        qtd_itens,
        pesos,
        valores,
        capacidade_max
    )

    fim = time.time()

    valor = avaliacao(qtd_itens, valores, solucao)

    print("Solução:", solucao)
    print("Valor:", valor)

    print(f"Tempo de processamento: {fim - inicio:.15f} segundos")

main()


