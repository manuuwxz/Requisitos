NumAlunos = 5

nomes = []
notas = []

totalNotas = 0.0

print("    Sistema De Cadastro De Alunos    ")
print(f"Por favor, digite os dados de {NumAlunos} alunos.")

for i in range(NumAlunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")
    notaValida = False
    while not notaValida:
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
            notaValida = True
        except ValueError:
            print("Nota inválida. Por favor, digite um número (ex: 8.5).")

    nomes.append(nome)
    notas.append(nota)
    totalNotas = totalNotas + nota

if NumAlunos > 0:
    mediaTurma = totalNotas / NumAlunos
else:
    mediaTurma = 0.0 

print("\n    LISTA DE ALUNOS CADASTRADOS    ")
for i in range(NumAlunos):
    print(f"- {nomes[i]} | Nota: {notas[i]}")
print(f"\nMédia da turma: {mediaTurma:.2f}")