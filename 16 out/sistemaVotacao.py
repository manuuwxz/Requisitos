opcoes = ["Candidato A", "Candidato B", "Voto em Branco"]

votos = [0] * len(opcoes) 

print("    SISTEMA DE VOTAÇÃO    ")
print("As opções são:")

for i, opcao in enumerate(opcoes):
    print(f"{i + 1} - {opcao}")

while True:
    try:
        escolhas = input(f"\nEscolha uma opção (1-{len(opcoes)}) ou 0 para encerrar: ")
        escolha = int(escolhas)

        if escolha == 0:
            break 
        elif 1 <= escolha <= len(opcoes):
            votos[escolha - 1] += 1
            print(f"Voto confirmado na {opcoes[escolha - 1]}")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite apenas números.")

print("\n    RESULTADOS FINAIS    ")
for i, opcao in enumerate(opcoes):
    print(f"{opcao}: {votos[i]} voto(s)")