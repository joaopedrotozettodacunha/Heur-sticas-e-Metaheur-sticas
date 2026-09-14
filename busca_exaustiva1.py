import time

print("N: ")
n = int(input())

def string_binaria(n):

    if n <= 0:
        return None
    else:
        for i in range(2 ** n):
            print(format(i, f"0{n}b")) #format transforma o numero i em outra representacao 
            #0{n} represente o numero binario com n posicoes,  preenchendo com 0 quando necessario

inicio = time.time()
string_binaria(n)
fim = time.time()

total = fim - inicio

print(f"Tempo de processamento {total:.6f}.")
