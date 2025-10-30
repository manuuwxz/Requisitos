alunos = {}

def adicionarAluno():
    nome = input("Nome do aluno: ")
    try:
        nota = float(input(f"Nota final de {nome}: "))
        alunos[nome] = nota
        print(f"Aluno {nome} cadastrado com sucesso.")
    except ValueError:
        print("Erro - Aa nota deve ser um número (ex: 9.5).")

def listarAlunos():
    if not alunos:
        print("Aluno não cadastrado.")
        return 
    
    print("\n    Lista de Alunos    ")
    for nome, nota in alunos.items():
        print(f"- {nome} | Nota: {nota}")

def buscarNota():
    nome = input("Nome do aluno que você quer buscar: ")
    if nome in alunos:
        print(f"A nota de {nome} é: {alunos[nome]}")
    else:
        print(f"Aluno {nome} não encontrado.")

def sistema():
     while True:
        print("\n    Sistema de Alunos    ")
        print("  1 - Adicionar aluno")
        print("  2 - Listar alunos")
        print("  3 - Buscar nota")
        print("  0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionarAluno()
        elif opcao == '2':
            listarAlunos()
        elif opcao == '3':
            buscarNota()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break 
        else:
            print("Opção inválida! Tente novamente.")

sistema()