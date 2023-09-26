num_sorte = 20

while True:
    print('Vamos advinhar qual é o numero da sorte. Você tem ate 10 tentativas. =D')
    print('**'*10)
    
    for i in range(10):
        n = int(input(f'Informe aqui a sua {i+1} tentativa: '))
        tentativas = i+1
        print('--'*10)
        if n == num_sorte:
            print(f'Parabens você acertou com {tentativas} tentativa(s)')
            break
        elif n < num_sorte:
            print(f'Vou lhe dar uma dica. O numero da sorte é maior.')
            continue
        elif tentativas == 9:
            print(f'Oh que pena! Não foi dessa vez, sua tentativas acabaram =/.')
            print(f'O numero da sorte é {num_sorte}')
            break
        elif n > num_sorte:
            print(f'Vou lhe dar uma dica. O numero da sorte é um pouco menor.')
            continue
       
    if n == num_sorte: break 
    else:
        tentativas == 10
        break 








