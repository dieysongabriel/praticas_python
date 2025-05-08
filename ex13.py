
""" 
Descrição do desafio 41
 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade

"""

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '));
idade = atual - nascimento;

print(f'O atleta tem {idade} anos');



