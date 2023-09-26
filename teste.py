def media(notas):
    # Função que calcula a média 
    t_notas = len(notas)
    soma = sum(notas)
    m = soma / t_notas
    return m

# Lista para armazenar todas as notas dos alunos
notas_alunos = []

while True:
    print("\n--- Menu ---")
    print("1 - Inserir notas")
    print("2 - Calcular média dos alunos")
    print("3 - Visualizar notas dos alunos")
    print("4 - Sair")
    
    opcao = input("Digite o número da operação desejada: ")

    if opcao == '1':
        qtd = int(input('Quantas notas deseja incluir? '))
        for i in range(qtd):
            nota_str = input("Digite a nota do aluno: ")
            nota = float(nota_str)
            notas_alunos.append(nota)

    elif opcao == '2':
        if notas_alunos:
            media_geral = media(notas_alunos)
            print(f"Média geral das notas é: {media_geral:.2f}")
                
        else:
            print("A lista de notas dos alunos está vazia. Insira as notas primeiro.")

    elif opcao == '3':
        if notas_alunos:
            for i, nota_aluno in enumerate(notas_alunos, start=1):
                print(f"Nota do aluno {i}: {nota_aluno}")
        else:
            print("A lista de notas dos alunos está vazia. Insira as notas primeiro.")

    elif opcao == '4':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Digite um número válido do menu.")
