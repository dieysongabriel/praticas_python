

try: 
    num = int(input('Digite um número: '));

    res = 10 / num;
except ValueError:
    print('Digite um número válido');
except ZeroDivisionError:
    print('Divisão por zero, não é permitida');
else:
    print(f'Resultado: {res}');
finally:
    print('Operação concluída');

