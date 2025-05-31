

import pdb

def soma_pares(lista):
    pdb.set_trace()
    soma = 0
    for n in lista:
        if n % 2 == 1:
            soma += n
    return soma

print(soma_pares([1, 2, 3, 4]))