

"""
Exercício Validador de Senha Forte
Descrição:
Crie um programa que leia uma senha digitada pelo usuário e verifique se ela é forte. Uma senha forte deve:

Ter no mínimo 8 caracteres
Conter pelo menos uma letra maiúscula
Conter pelo menos uma letra minúscula
Conter pelo menos um número
Conter pelo menos um caractere especial (ex: !@#$%&*)

"""




def validador(senha):
    
    if len(senha) < 8:
        return 'Digite uma senha com 8 ou mais caracteres'
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    caracteres = '!@#$%&*_'
    numeros = '0123456789'

    tem_maiuscula = 0
    tem_minuscula = 0
    tem_caractere = 0
    tem_numero = 0
    
    for i in senha:
        if i in maiusculas:
            tem_maiuscula += 1
        elif i in minusculas:
            tem_minuscula += 1
        elif i in caracteres:
            tem_caractere += 1
        elif i in numeros:
            tem_numero += 1
    
    if tem_maiuscula >= 1 and  tem_caractere >= 1 and tem_minuscula >= 1 and tem_numero >= 1 and len(senha) >= 8:
        return 'A senha é valida'
    else:
        return 'A senha é invalida'

print(validador('teste!123'));

#hUEQ5_zb6<8m
#teste!123