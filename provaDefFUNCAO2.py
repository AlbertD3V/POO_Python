numeros = [3]

for i in range(10):
    vl =+ i
    numeros.append(vl)

def media_numero():
    return f'A média aritmética dos valores são: {(sum(numeros)/len(numeros)):.3}'


lista = media_numero()
print(lista)