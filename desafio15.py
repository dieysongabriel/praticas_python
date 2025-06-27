

"""
Exercício: Conversor de Data
Descrição:
Peça ao usuário para digitar uma data no formato DD/MM/AAAA. O programa deve:

Validar se a data tem o formato correto

Converter e imprimir a data por extenso (ex: "15 de junho de 2025")

"""


from datetime import datetime

def conversor_data():
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    str_data = input('Digite uma data no formato DD/MM/AAAA: ')

    try:
        data = datetime.strptime(str_data, "%d/%m/%Y")
        dia = data.day
        mes = data.month
        ano = data.year
        print(f'{dia} de {meses[mes - 1]} de {ano}')
    except ValueError:
        print('Data inválida ou em formato errado')

conversor_data();
