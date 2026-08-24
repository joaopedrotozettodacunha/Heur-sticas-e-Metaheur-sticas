instancia = open("instancia_1.txt", "r")
linhas = instancia.readlines()

primeira_linha = linhas[0]
dados = primeira_linha.split() #split transforma em string

numero_vertices = int(dados[0])
numero_arestas = int(dados[1])

matriz = []
lista_adjacencia = []

#matriz
for i in range(numero_vertices):
    linha = []

    for j in range(numero_vertices):
        linha.append(0)

    matriz.append(linha)

#lista de adjacencia
for i in range(numero_vertices):
    lista_adjacencia.append([])

for linha in linhas[1:numero_arestas + 1]:
    dados = linha.split() #split transforma em string

    origem = int(dados[0])
    destino = int(dados[1])
    custo = int(dados[2])

    matriz[origem - 1][destino - 1] = custo
    matriz[destino - 1][origem - 1] = custo

    lista_adjacencia[origem - 1].append((destino, custo))
    lista_adjacencia[destino - 1].append((origem, custo))

print("Matriz:\n")

for m in matriz:
    print(m)
print("")
print("Lista de Adjacência:\n")

for l in lista_adjacencia:
    print(l)

instancia.close()
