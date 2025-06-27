

"""
Exercicio Ordenar Lista e Remover Duplicatas
Descrição:
Peça ao usuário que digite uma lista de números separados por vírgula. 
O programa deve:
Remover os números duplicados
Ordenar a lista em ordem crescente
Mostrar a lista final

"""

str = '3, 5, 9, 12, 17, 5'

def lista(str):

    first_list = str.split(',')

    second_list = []
    for i in first_list:
        second_list.append(int(i));
    
    second_list.sort();
    third_list = list(set(second_list));

    return third_list


print(lista(str));