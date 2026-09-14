from itertools import permutations
import time

print("N: ")
n = int(input())

def permutacoes(n):

    if n <= 0:
        return None

    else:

        for permutacao in permutations(range(1, n + 1)):
            print(list(permutacao))

   
inicio = time.time()
permutacoes(n)
fim = time.time()

total = fim - inicio

print(f"Tempo de processamento {total:.6f}.")