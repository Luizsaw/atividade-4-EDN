def media_turma():
    notas = []
    total_alunos = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(total_alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")

media_turma()