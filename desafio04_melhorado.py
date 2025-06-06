
def validar_cpf(cpf):
    
    #vê se tem só número
    if not cpf.isdigit() or len(cpf) != 11:
        return 'CPF é inválido!';

    # vê se todos os numeros são iguais
    if cpf[0] == cpf[1] == cpf[2] == cpf[3] == cpf[4] == cpf[5] == cpf[6] == cpf[7] == cpf[8] == cpf[9] == cpf[10]:
        return 'CPF é inválido'
    
    soma1 = 0
    for i in range(9):
        soma1 = soma1 + (int(cpf[i]) * (10 - i))
    dig1 = (soma1 * 10) % 11
    if dig1 == 10 or dig1 == 11:
        dig1 = 0    # se for 10 ou 111 zera, sei lá pq mas é a regra
    
    
    soma2 = 0;
    for x in range(9):
        soma2 += int(cpf[x]) * (11 - x)
    soma2 = soma2 + (dig1 * 2)
    dig2 = (soma2 * 10) % 11
    if dig2 == 10 or dig2 == 11:
        dig2 = 0

    if int(cpf[9]) == dig1 and int(cpf[10]) == dig2:
        return 'CPF é válido!';
    else:
        return 'CPF é inválido!';


        

print(validar_cpf(''));
