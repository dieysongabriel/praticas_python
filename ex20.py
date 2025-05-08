

class ContaBancaria():
    def __init__(self, nomeCliente, numeroConta, saldo):
        self.nomeCliente = nomeCliente;
        self.numeroConta = numeroConta;
        self.saldo = saldo;

    def exibir_saldo(self):
        print(f'Heelo, Sr ou Sra {self.nomeCliente}, o valor que você tem na conta é de {self.saldo}');
        print('Tenha um Bom Dia');

    def depositar(self, valor):
        if(valor > 0):
            self.saldo += valor;
            print(f'O Deposito no valor de {valor} reais realizado com sucesso');
            print('Tenha um Bom Dia');
        else:
            print('valor inválido');
    
    def sacar(self, valor):
        if(valor > 0 and valor < self.saldo):
            self.saldo -= valor;
            print(f'Saque no valor de {valor} reais Realizado com Sucesso');
            print('Tenha um Bom Dia');
        elif(valor > self.saldo):
            print('Saldo insuficiente');
            print('Tenha um Bom Dia');
        else:
            print('Valor inválido');
            print('Tenha um Bom Dia');


conta1 = ContaBancaria('Dieyson', 214, 790);

conta1.exibir_saldo();
