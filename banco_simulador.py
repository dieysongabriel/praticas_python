

import csv
import os
from datetime import datetime

class Transacao:
    def __init__(self, tipo, valor, cpf_conta):
        self.tipo = tipo
        self.valor = valor
        self.cpf_conta = cpf_conta
        self.data_hora = datetime.now()

    def to_csv_row(self):
        return [self.cpf_conta, self.tipo, self.valor, self.data_hora.strftime("%Y-%m-%d %H:%M:%S")]
    



class ContaBancaria:
    def __init__(self, nome, cpf, numero_conta, saldo=0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Valor de depósito inválido')
        self.saldo += valor
        t = Transacao('Depósito', valor, self.cpf)
        self.transacoes.append(t)
        return t
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('Valor de saque inválido')
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente')
        self.saldo -= valor
        t = Transacao('Saque', valor, self.cpf)
        self.transacoes.append(t)
        return t

    def ver_saldo(self):
        return f'O saldo atual é de {self.saldo} Reais'
    
    def mostrar_transacoes(self):
        print('Transações:')
        for t in self.transacoes:
            print(f'[{t.data_hora}] {t.tipo}: R${t.valor:.2f}')




class Banco:
    def __init__(self, arquivo_contas='contas.csv', arquivo_transacoes='transacoes.csv'):
        self.contas = []
        self.arquivo_contas = arquivo_contas
        self.arquivo_transacoes = arquivo_transacoes
        self.carregar_contas()

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        self.salvar_contas()

    def buscar_conta_por_cpf(self, cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        return None
    
    def salvar_contas(self):
        with open(self.arquivo_contas, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Nome', 'CPF', 'NumeroConta', 'Saldo'])
            for conta in self.contas:
                writer.writerow([conta.nome, conta.cpf, conta.numero_conta, conta.saldo])

    def carregar_contas(self):
        if os.path.exists(self.arquivo_contas):
            with open(self.arquivo_contas, 'r') as f:
                r = csv.DictReader(f)
                for row in r:
                    conta = ContaBancaria(
                        row['Nome'],
                        row['CPF'],
                        row['NumeroConta'],
                        float(row['Saldo'])
                    )
                    
                    self.contas.append(conta)

    def salvar_transacao(self, transacao):
        arquivo_vazio = not os.path.exists(self.arquivo_transacoes) or os.path.getsize(self.arquivo_transacoes) == 0
        with open(self.arquivo_transacoes, 'a', newline='') as file:
            writer = csv.writer(file)
            if arquivo_vazio:
                writer.writerow(['CPF', 'Tipo', 'Valor', 'DataHora'])
            writer.writerow(transacao.to_csv_row())




banco = Banco()


while True:
    print('1 - Criar conta')
    print('2 - Acessar conta')
    print('3 - Sair')
    op = input('Opção: ')


    if op == '1':
        nome = input('Nome: ')
        cpf = input('CPF: ').strip()
        if not cpf.isdigit() or len(cpf) != 11:
            print('CPF inválido')
            continue
        num = input('Número da conta: ')
        if banco.buscar_conta_por_cpf(cpf):
            print('Já existe conta com esse CPF!')
        else:
            conta = ContaBancaria(nome, cpf, num)
            banco.adicionar_conta(conta)
            print('Conta criada!')


    elif op == '2':
        cpf = input('CPF: ')
        conta = banco.buscar_conta_por_cpf(cpf)
        if conta:
            while True:
                print('1 - Depositar')
                print('2 - Sacar')
                print('3 - Ver saldo')
                print('4 - Ver transações')
                print('5 - Voltar')
                op2 = input('Opção: ')


                if op2 == '1':
                    valor = float(input('Valor: '))
                    banco.salvar_transacao(conta.depositar(valor))
                elif op2 == '2':
                    valor = float(input('Valor: '))
                    try:
                        banco.salvar_transacao(conta.sacar(valor))
                    except ValueError as e:
                        print(e)
                elif op2 == "3":
                    print(conta.ver_saldo())
                elif op2 == "4":
                    conta.mostrar_transacoes()
                elif op2 == "5":
                    break
        else:
            print("Conta não encontrada!")

    elif op == "3":
        print("Saindo...")
        banco.salvar_contas()
        break

    else:
        print("Opção inválida!")