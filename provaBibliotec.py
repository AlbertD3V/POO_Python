import random
#LETRA C GERANDO UMA LISTA COM 5 ELEMENTOS DE NUMEROS ALEATORIOS ENTRE 1 E 100
lista = []

for i in range(5):
    x = random.randint(1, 100)
    lista.append(x)
print(lista)