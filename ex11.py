

primeiroNum = int(input('Digite o primeiro número: '));
segundoNum = int(input('Digite o segunda número: '));

def verificar():
    if(primeiroNum > segundoNum):
        print('O primeiro número é maior');
    elif(segundoNum > primeiroNum):
        print('O Segundo número é maior');
    else:
        print('Não existe valor maior, todos são iguais');



verificar();