pessoa = []
idade = []
sexo = []

for i in range(5):
    
    nome = input(' Digite aqui o seu nome: ')
    pessoa.append(nome)  
    idad = int(input('Digite aqui sua idade: '))
    idade.append(idad) 
    sex = input('Digite seu sexo: ')
    sexo.append(sex)
    if idade[i] <= min(idade):
         s = sexo[i]
    print('**'*10)

maioridade = pessoa[idade.index(max(idade))]
menorde20 = 0
maiorde40 = 0

for i in range(0,len(idade)):
   if idade[i] < 20:
     menorde20 +=1
   elif idade[i] > 40:
     maiorde40 +=1
           
print(f'A Média de idades é {sum(idade)/len(idade)} anos')
print(f'A pessoa mais velha é {maioridade}')
print(f'Existe(m) {menorde20} pessoa(as) menor(es) de 20 anos')
print(f'Existe(m) {maiorde40} pessoa(as) maior(es) que 40 anos')
print(f'O sexo da pessoa mais nova é do sexo {s}')



