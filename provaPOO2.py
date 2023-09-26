class Automovel:
    def __init__(self,placa:str,motor:str,modelo:str,cor:str,rodas:int):
        self.placa = placa
        self.motor = motor
        self.modelo = modelo
        self.cor = cor
        self.rodas = rodas
    @property
    def situacao(self):
            return f'O {self.modelo} é novo de fabrica'
    
    @property
    def lugar(self):
         if self.rodas == 4:
              return 'Todos os passageiros devem usar o cinto mesmo roando na cidade'
         elif self.rodas == 2:
              return 'Condutor e passageiro devem usar capacete'
         elif self.rodas > 4:
              return 'O automovel é de grande porte, conduza com atenção pois a possibilidade de esta levando vidas'
    
class Carro(Automovel):
     def __init__(self, placa:str, motor:str, modelo:str, cor:str, rodas:int,lugares:int):
          super().__init__(placa, motor, modelo, cor, rodas)
          self.lugares = lugares


class Onibus(Automovel):
     def __init__(self, placa:str, motor:str, modelo:str, cor:str, rodas:int, passageiros:int):
          super().__init__(placa, motor, modelo, cor, rodas)
          self.passageiros = passageiros


hb20= Carro('PP3K69','Motor 2.0','Hyundai HB20S','vermelho',4,5)
print(hb20.lugar)
print(hb20.situacao)

buzao = Onibus('354AZQ','Motor Mercedes Benz','Mecerds  Executivo','Azul',8,48)
print(buzao.lugar)