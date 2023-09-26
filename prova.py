numeros = []
for n in range(3):
    vl = input(f' Digite aqui o {n+1}º número:')
    numeros.append(vl)
    print('--------------------------------')

numeros.sort()

for n in range(0,len(numeros)-1):
    if numeros[n] == numeros[n+1]:
           repete = numeros[n+1]
           print(f'O numero {repete} é repitido')
     
print(f'O Maior valor é {max(numeros)}')
print(f'O Menor valor é {min(numeros)}')

