# Sistema de Gestão de Peças

pecas = []
caixas = []
caixa_atual = []
CAPACIDADE_CAIXA = 10


def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, "Aprovada"
    else:
        return False, ", ".join(motivos)


def cadastrar_peca():
    global caixa_atual, caixas

    try:
        id_peca = input("ID da peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor: ")
        comprimento = float(input("Comprimento (cm): "))

        aprovada, motivo = avaliar_peca(peso, cor, comprimento)

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "status": "Aprovada" if aprovada else "Reprovada",
            "motivo": motivo
        }

        pecas.append(peca)

        if aprovada:
            caixa_atual.append(peca)

            if len(caixa_atual) == CAPACIDADE_CAIXA:
                caixas.append(caixa_atual)
                print("📦 Caixa cheia! Caixa fechada.")
                caixa_atual = []

        print("Peça cadastrada com sucesso!")

    except:
        print("Erro ao cadastrar peça!")


def listar_pecas():
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    for p in pecas:
        print(f"ID: {p['id']} | Status: {p['status']} | Motivo: {p['motivo']}")


def remover_peca():
    id_remover = input("Digite o ID da peça para remover: ")

    for p in pecas:
        if p["id"] == id_remover:
            pecas.remove(p)
            print("Peça removida!")
            return

    print("Peça não encontrada!")


def listar_caixas():
    if not caixas:
        print("Nenhuma caixa fechada ainda.")
        return

    for i, caixa in enumerate(caixas, start=1):
        print(f"\nCaixa {i}:")
        for p in caixa:
            print(f" - ID: {p['id']}")


def gerar_relatorio():
    aprovadas = 0
    reprovadas = 0
    motivos = {}

    for p in pecas:
        if p["status"] == "Aprovada":
            aprovadas += 1
        else:
            reprovadas += 1
            motivos[p["motivo"]] = motivos.get(p["motivo"], 0) + 1

    print("\n📊 RELATÓRIO FINAL")
    print(f"Aprovadas: {aprovadas}")
    print(f"Reprovadas: {reprovadas}")

    print("\nMotivos de reprovação:")
    for motivo, qtd in motivos.items():
        print(f"{motivo}: {qtd}")

    print(f"\nCaixas utilizadas: {len(caixas)}")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas")
        print("5 - Gerar relatório")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")


# Executar sistema
menu()
