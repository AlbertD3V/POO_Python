
list1 = []
list2 = []

qtd = int(input('Quantos elementos tem a lista 1? '))
for i in range(qtd):
    lista1 = int(input(f"informe o {i+1} elemento da primeira lista: "))
    list1.append(lista1)
qtd2 = int(input('Quantos elementos tem a lista 2? '))
for i in range(qtd2):
    lista2 = int(input(f'Informe o {i+1} elementos da segunda lista: '))
    list2.append(lista2)


elementos_em_comum = list(set(list1).intersection(list2))

soma_elementos = sum(elementos_em_comum)

resultado = (elementos_em_comum, soma_elementos)

print("Elementos em comum:", resultado[0])
print("Soma dos elementos em comum:", resultado[1])
