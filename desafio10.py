
"""
Exercício 1: Frequência de Letras em uma Frase
Descrição:
Peça ao usuário para digitar uma frase e mostre a frequência de cada letra (desconsiderando espaços e sem diferenciar maiúsculas de minúsculas)
"""

def frequencia(str):
    str = str.lower().replace(" ", "")
    ja_apareceu = {}

    for i in str:
        if i in ja_apareceu:
            ja_apareceu[i] += 1
        else:
            ja_apareceu[i] = 1
    return ja_apareceu
    

str = input('Digite uma frase: ')
resu = frequencia(str)

print('Contagem de letras: ')
for x, y in sorted(resu.items()):
    print(f'{x}: {y}')




