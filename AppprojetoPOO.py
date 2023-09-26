from funcionario import *

class App:
    def __init__(self):
        self.dados = []
        f1 = Funcionario(1,'Xavier',33,'professor',15000.00)
        f2 = Funcionario(2,'Glauco',25,'testador ',50000.00)
        self.dados.append(f1)
        self.dados.append(f2)
        while True:            
            print ('''
            ----------[MENU]----------
            I -> Incluir funcionario
            A -> Alterar funcionario
            E -> Excluir funcionario
            C -> Consultar funcionario
            X -> PARAR APLICAÇÃO        
            ''')
            op = input('Que opção deseja? ')
            if op.upper() == 'I':
                self.incluir_funcionario()
            elif op.upper() == 'A':
                self.alterar_funcionario()
            elif op.upper() == 'E':
                self.excluir_funcionario()
            elif op.upper() == 'C':
                self.consultar_funcionario()
            elif op.upper() == 'X':
                break

#ROTINA DE INCLUIR FUNCIONARIO
    def incluir_funcionario(self):
        id = int(input('Digite o ID do funcionario :'))
        nome = input('Digite o nome do funcionario: ')
        idade = int(input('Idade do funcionario      : '))
        cargo = input ('Cargo do funcionario      : ')
        salario = float(input('Salario do funcionario  : '))
        funcionario = Funcionario(id,nome,idade,cargo,salario)
        self.dados.append(funcionario)

 
#CHAMA A ROTINA DE ALTERAR DADOS DO FUNICONARIO
    def alterar_funcionario(self):
        self.consultar_funcionario()
        a = input('O que você deseja alterar?(responda [nome, idade, cargo, salario ou tudo] ).\n').lower()
        
        if a == 'nome':
            self.alterar_funcionario_nome()
        elif a == 'idade':
            self.alterar_funcionario_idade()
        elif a == 'cargo':
            self.alterar_funcionario_cargo()
        elif a == 'salario':
           self.alterar_funcionario_salario()
        elif a == 'tudo':
            self.alterar_funcionario_tudo()
        else:
            ('Opção invalida')

       #SUB ROTINA PARA ALTERAR NOME DO FUNCIONARIO 
    def alterar_funcionario_nome(self):
        idfun = int(input('Id do Funcionario que vai ser alterado :'))
        for f in self.dados:
            if idfun == f.id:
                nmfun = input('Nome do Funcionario   :')
                f.nome = nmfun

       #SUB ROTINA PARA ALTERAR A IDADE DO FUNCIONARIO
    def alterar_funcionario_idade(self):
        idfun = int(input('Id do Funcionario que vai ser alterado :'))
        for f in self.dados:
            if idfun == f.id:
                idadfun = input('Idade do Funcionario   :')
                f.idade = idadfun

       #SUB ROTINA PARA ALETRAR O CARGO DO FUNCIONARIO 
    def alterar_funcionario_cargo(self):
        idfun = int(input('Id do Funcionario que vai ser alterado :'))
        for f in self.dados:
            if idfun == f.id:
                cargofun = input('Bovo cargo do Funcionario :')
                f.cargo = cargofun

        #SUB ROTINA PAA ALTERAR O SALARIO DO FUNCIONARIO
    def alterar_funcionario_salario(self):
       idfun = float(input('Id do Funcionario que vai ser alterado :'))
       for f in self.dados:
            if idfun == f.id:
               salarioFun = float(input('Novo salario do Funcionario: '))
               f.salario = salarioFun

       #SUB ROTINA DE ALTERAR tODO OS DADOS DO FUNCIONARIO
    def alterar_funcionario_tudo(self):
        idfun = int(input('Id do Funcionario que vai ser alterado :'))
        for f in self.dados:
            if idfun == f.id:
                nomefun = input('Novo nome do Funcionario     :')
                idadfun = int(input('Nova idade do Funcionario: '))
                cargofun = input('Novo cargo do Funcionario   :')
                salariofun = float(input('Novo salário do Funcionario:'))
                f.nome = nomefun
                f.idade = idadfun
                f.cargo = cargofun
                f.salario = salariofun
                

 # EXCLUI O FUNCIONARIO PELA ID
    def excluir_funcionario(self):
       self.consultar_funcionario()
       id= int(input('Qual o id do funcionario que deseja excluir: '))
       for f in self.dados:
             if id == f.id :
               self.dados.remove(f)
             else:
                 print(f'Essa ID {id} não foi encontrada')
                 break         
        
 #CONSULTA TODOS OS FUNCIONARIOS CADASTRADOS       
    def consultar_funcionario(self):
        for f in self.dados:
            print(f'''┃_ID: {f.id}__┃┃_NOME: {f.nome}__┃┃_IDADE: {f.idade}__┃┃_CARGO: {f.cargo}__┃┃_SALARIO: {f.salario}__┃''')

if __name__ == '__main__':
    app = App()