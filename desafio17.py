

class Funcionarios:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    
    def aumentar_salario(self, salario, porcentual):
        self.salario = salario + (salario * porcentual)
        print(f'Você teve um aumento de sálario, seu salário Atual é {self.salario}')


    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cargo: {self.cargo}')
        print(f'Salário: {self.salario}')


funcionario1 = Funcionarios('Ana', 'Analista de Dados', 4500)
funcionario2 = Funcionarios('Bruno', 'Desenvolvedor Backend', 5800)

funcionario1.aumentar_salario(4500, 0.30);

funcionario1.exibir_dados()

funcionario2.exibir_dados()
         
