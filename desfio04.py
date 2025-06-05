
def cpf_valido():
    cpf = input('Digite seu CPF: ')

    if not cpf.isdigit() or len(cpf) != 11:
        print('O CPF é inválido!');
    else:
        print('O CPF é válido!');
    
cpf_valido();
    

