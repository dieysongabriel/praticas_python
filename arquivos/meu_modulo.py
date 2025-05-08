
def cadastrar_usuario(*args, **kwargs):
    print('Hobbies: ');
    for x in args:
        print(f'-{x}');

    print('Informações adicionais: ');
    for key, value in kwargs.items():
        print(f'{key}: {value}');

cadastrar_usuario('Jogar bola', 'Treinar', 'Fazer dinheiro', 'Nome: ' 'Dieyson', 'idade: ', 19  );