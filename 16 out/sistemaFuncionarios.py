funcionarios = []

def adicionarFuncionario():
    print("\n    Adicionar Funcionário    ")
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    try:
        salario = float(input("Salário (ex: 1500.00): "))
        novoFuncionario = {"nome": nome, "cargo": cargo, "salario": salario}
        
        funcionarios.append(novoFuncionario)
        
        print(f"Funcionário {nome} cadastrado com sucesso!")
        
    except ValueError:
        print("Erro: O salário deve ser um número.")

def listarFuncionarios():
    if not funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return 
    
    print("\n    Lista de Funcionários    ")
    for i, func in enumerate(funcionarios):
        print(f"{i + 1}) Nome: {func['nome']}")
        print(f"   Cargo: {func['cargo']}")
        print(f"   Salário: R$ {func['salario']:.2f}")
      
def buscarFuncionario():
    nomeBusca = input("Qual nome você quer buscar? ")
    
    encontrado = False 
    
    for func in funcionarios:
        if func['nome'].lower() == nomeBusca.lower():
            print("\n    Funcionário Encontrado    ")
            print(f"Nome: {func['nome']}")
            print(f"Cargo: {func['cargo']}")
            print(f"Salário: R$ {func['salario']:.2f}")
            encontrado = True
            break  
    
    if not encontrado:
        print(f"Funcionário {nomeBusca} não encontrado.")

while True:
    print("\n    SISTEMA DE FUNCIONÁRIOS    ")
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionarFuncionario()
    elif opcao == '2':
        listarFuncionarios()
    elif opcao == '3':
        buscarFuncionario()
    elif opcao == '0':
        print("Encerrando...")
        break 
    else:
        print("Opção inválida! Tente novamente.")