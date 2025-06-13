
numeros_salvos = {}

def fatorial(num):
    

    if num < 1:
        return 1

    if num in numeros_salvos:
        return numeros_salvos[num]
            
    resultado = num * fatorial(num - 1)
    numeros_salvos[num] = resultado
    return resultado

print(fatorial(5))

print(numeros_salvos)