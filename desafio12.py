
"""
Exercício 3: Números Primos em um Intervalo
Descrição:
Peça dois números ao usuário (início e fim de um intervalo) e mostre todos os números primos dentro desse intervalo

"""



def numeros_primos():
    inicio = int(input('Digite o número pelo qual deseja começar: '))
    fim = int(input('Digite o número pelo qual deseja termina: '))

    for y in range(inicio, fim):
        eh_primo = True
        if y < 2:
            eh_primo= False
        else:
            for a in range(2, y):
                if y % a == 0:
                    eh_primo = False
                    break

        if eh_primo:
            print(y);


numeros_primos();



