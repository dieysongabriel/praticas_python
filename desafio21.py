

def limpar_cnpj(cnpj):
    cnpj_limpo = ""
    for caractere in cnpj:
        if caractere.isdigit():
            cnpj_limpo += caractere
    return cnpj_limpo

def calcular_digito(cnpj_parcial, pesos):
    soma = 0
    for i in range(len(pesos)):
        soma += int(cnpj_parcial[i]) * pesos[i]
    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)


def validar_cnpj(cnpj):
    cnpj = limpar_cnpj(cnpj)


    if len(cnpj) != 14:
        return False
    
    if cnpj == cnpj[0] * 14:
        return False
    
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    primeiro_digito = calcular_digito(cnpj[:12], pesos1)

    segundo_digito = calcular_digito(cnpj[:12] + primeiro_digito, pesos2)

    if cnpj[-2:] == primeiro_digito + segundo_digito:
        return True
    else:
        return False
    

