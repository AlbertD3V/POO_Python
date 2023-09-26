pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19,

}



#MOSTRANDO O DICIONARIO

for nome, idade in pessoas.items():

    print(nome, idade)

print("--"*20)



#PRINT NA VARIAVEL IDADE DE JOÃO

idade_joao = pessoas["João"]

print(f'A idade de João é {idade_joao} anos')

print("--"*20)



#ADICONANDO ANA AO DICIONARIO E MOSTRANDO ELE ATUALIZADO

pessoas["Ana"]=31

for nome, idade in pessoas.items():

    print(nome, idade)

print("--"*20)



#DEFININDO A FUNÇÃO PARA PUXAR A MAIOR IDADE ENTRE AS PESSOAS E MOSTRANDO ELA

def pessoa_com_maior_Idade():

    idades_maiores = max(pessoas.values())

    pessoa_idades_maiores = [nome for nome, idade in pessoas.items() if idade == idades_maiores]

    return f'A pessoa com maior idade é {", ".join( pessoa_idades_maiores)} que tem {idades_maiores} anos'

IdadeMaior = pessoa_com_maior_Idade()

print(IdadeMaior)

