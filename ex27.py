
try:
    num1 = int(input('Digite o primeir número: '));
    num2 = int(input('Digite o segundo número: '));
    res = num1 // num2
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
else:
    print(res);
