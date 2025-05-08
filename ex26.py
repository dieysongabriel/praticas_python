
frase = 'Estudando python para ser um desenvolvedor de software';

def verificar(str):
    strinvertida = str[::-1];
    if str == strinvertida:
        print('É palíndroma');
    else:
        print('Não é palíndroma');

verificar(frase);