
def ehNumFeliz():
    numero = int(input('Digite um número: '))
    ja_vi = set()

    while numero != 1:
        if numero in ja_vi:
            return 'O número é infeliz';

        ja_vi.add(numero)

        soma = 0
        for c in str(numero):
            soma = soma + int(c) ** 2

        numero = soma;
    
    return 'O número é feliz';

print(ehNumFeliz());
