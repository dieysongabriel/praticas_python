
mostrarSoma = print('Operações: 1 - soma ');
mostrarSub = print('Operações: 2 - subtraçao ');
mostrarMulti = print('Operações: 3 - multiplicação ');
mostrarDivi = print('Operações: 4 - divisão ');



def calculadora():
    operacao = int(input('Digite o número da operação que deseja usar: '));
    if(operacao == 1):
        num1 = int(input('Digite um número: '));
        num2 = int(input('Digite outro número: '));
        print(f'{num1} + {num2} = {num1 + num2}');
    elif(operacao == 2):
        num3 = int(input('Digite um número: '));
        num4 = int(input('Digite outro número: '));
        print(f'{num3} + {num4} = {num3 - num4}');
    elif(operacao == 3):
        num5 = int(input('Digite um número: '));
        num6 = int(input('Digite outro número: '));
        print(f'{num5} + {num6} = {num5 * num6}');

calculadora();