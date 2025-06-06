
from functools import reduce

def media_vendas(lista):
    soma = reduce(lambda x, y: x + y, lista);

    vendedores = len(lista);

    media_vendas = soma / vendedores

    mais_vendeu = lista.index(max(lista));

    menos_vendeu = lista.index(min(lista));

    vendeu_acima_media = []

    for i in lista:
        if i > media_vendas:
            vendeu_acima_media.append(i);

    return f'a média é {media_vendas}, o vendedor que vendeu mais foi o vendedor: {mais_vendeu} e o que menos vendeu foi o vendedor: {menos_vendeu}, e os vendedores que venderam acima da média são: {vendeu_acima_media}';


print(media_vendas());


