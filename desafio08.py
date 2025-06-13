

my_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
def somar_ds(matriz):
    tamanho = len(matriz)
    soma = 0
    linha = 0

    while linha < tamanho:
        colunaD = tamanho - 1 - linha
        elemento = matriz[linha][colunaD]
        soma += elemento
        linha += 1

    return soma


resultado = somar_ds(my_matriz)
print("Soma diagonal:", resultado)