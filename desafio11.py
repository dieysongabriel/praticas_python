

"""
Exercício 2: Cadastro de Produtos com Preços
Descrição:
Crie um programa que permita ao usuário cadastrar produtos com seus respectivos preços (nome e valor). Quando o usuário digitar “sair”, o programa deve exibir todos os produtos cadastrados e o total gasto.

Requisitos:

Usar um dicionário.

Entrada em loop.

"""

def cadastrando_produtos():
    produtos = {}

    while True:
        nome = input('Produto: ').strip()
        if nome.lower() == 'sair':
            break

        preco = input('Preço: ').replace(",", ".").strip()

        if preco == "":
            print('O Preço está vazio')
            continue

        try:
            preco = float(preco)
            produtos[nome] = preco

        except:
            print('Não consegui entender o preço')

    print('Produtos adicionados:')
    for x in produtos:
        print(f'- {x}: R$ {produtos[x]:.2f}')
    
    total = 0
    for valor in produtos.values():
        total += valor

    print(f'Total geral: R$ {round(total, 2)}')


cadastrando_produtos();