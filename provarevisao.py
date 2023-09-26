def calcular_media(notas):
    # Função que calcula a média aritmética das notas
    total_notas = len(notas)
    soma_notas = sum(notas)
    media = soma_notas / total_notas
    return media

# Lista para armazenar as notas dos alunos
notas_alunos = []

# Loop while para pedir ao usuário que insira as notas dos alunos
while True:
    nota_str = input("Digite a nota do aluno (ou 's' para sair): ")
    if nota_str.lower() == 's':
        break
    nota = float(nota_str)
    notas_alunos.append(nota)

# Loop for para imprimir a média de cada aluno
for i, notas_aluno in enumerate(notas_alunos, start=1):
    media_aluno = calcular_media(notas_aluno)
    print(f"Média do aluno {i}: {media_aluno:.2f}")
