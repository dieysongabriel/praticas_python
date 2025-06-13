

import unicodedata
import re


def limpar_texto(texto):
    texto = texto.lower();


    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')


    texto = re.sub(r'[^a-z0-9]', '', texto)

    return texto;

def eh_palindromo(str):
    strP = limpar_texto(str)

    strInvertida = str[::-1]

    if strP == strInvertida:
        return 'É palíndromo';
    else:
        return 'Não é palíndromo';

print(eh_palindromo('salas'));
