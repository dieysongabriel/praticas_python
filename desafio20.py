

def contar():
    palavra = input('Digite uma sequência de letras: ')


    resu = ""
    contador = 1

    for i in range(1, len(palavra)):
        if palavra[i] == palavra[i - 1]:
            contador += 1
        else:
            resu += palavra[i - 1] + str(contador)
            contador = 1
    
    if palavra:
        resu += palavra[-1] + str(contador)
    print(f'Palavra comprimida: {resu}')


contar();
        



