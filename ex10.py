

valorCasa = int(input('Digite o valor da casa: '));

salarioComprador = int(input('Digite o valor do seu sálario: '));

prazo = int(input('Em quantos meses você vai pagar? '));

valorParcela = valorCasa // prazo;
print(f'O valor da parcela é {valorParcela}');

def emprestimo():
    if(valorParcela > (valorCasa * 100) / 30):
        print('Empréstimo negado');
    else: 
        print('Empréstimo aceito');
emprestimo();