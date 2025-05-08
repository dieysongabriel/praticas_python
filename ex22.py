

def gerar_pares(num):
    if(num % 2 == 0):
        yield num;

for x in gerar_pares(8):
    print(x);