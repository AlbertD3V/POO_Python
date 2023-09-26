class Funcionario:
    
    def __init__(self,id:int,nome:str,idade:int,cargo:str,salario:float):
        self.id=id
        self.nome =  nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    @property
    def aumento(self):
        return f'{self.nome} quer falar sobre aumento'


funcionario = Funcionario(1,'Albert',29,'Lutador',6859.96)
print(funcionario.__dict__)
print(funcionario.aumento)