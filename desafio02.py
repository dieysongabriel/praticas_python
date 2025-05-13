

palavra = 'Python';

def ehPalindromo(palavra):
    palavraInvertida = palavra[::-1];
    if palavra == palavraInvertida:
        print(f'A palavra {palavra} é palíndromo');
    else:
        print(f'A palavra {palavra} não é palíndromo')



ehPalindromo(palavra);