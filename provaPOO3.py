class Livro:
    def __init__(self,paginas,teor,escritor,ano):
        self.paginas = paginas
        self.teor = teor
        self.escritor = escritor
        self.ano = ano

    @property
    def exibir_detalhes(self):
            if self.teor == 'romance':
                 return f'O escritor é de {self.escritor}, o livro foi escrito em {self.ano}. Te desejo uma ótima leitura.'
            elif self.teor == 'terror':
                   return f'O escritor é de {self.escritor}, o livro foi escrito em {self.ano}. Te desejo uma ótima leitura.'
            elif self.teor == 'biografia':
                   return f'O escritor é de {self.escritor}, o livro foi escrito em {self.ano}. Te desejo uma ótima leitura.'
            else:
                 return 'Não foi possivel indentificar o seu livro'
                 
    
    
class Romance(Livro):
     def __init__(self, paginas, teor, escritor, ano,classificacao):
           super().__init__(paginas, teor, escritor, ano)
           self.classificacao = classificacao

class Biografia(Livro):
     def __init__(self, paginas, teor, escritor, ano, nacionalidade):
           super().__init__(paginas, teor, escritor, ano)
           self.nacionalidade = nacionalidade


eu_Sou_Malala= Biografia(360,'biografia','Malala Yousafzai',2013,'Paquistanesa')
print('__'*50)
print(eu_Sou_Malala.__dict__)
print(eu_Sou_Malala.exibir_detalhes)
print('--'*50)
print('\n')
um_Amor_Para_Recordar= Romance(144,'romance', 'Nicholas Sparks',1999,'livre')
print('__'*50)
print(um_Amor_Para_Recordar.__dict__)
print(um_Amor_Para_Recordar.exibir_detalhes)
print('--'*50)