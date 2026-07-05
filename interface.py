from motor_calculo import calcular_fatura
from banco_dados_poo import cadastrar_assinante, assinantes
from relatorios_analytics import matriz_consumo, conta_mais_alta, acima_da_media


def calcular_fatura_avulsa():
    try:
        consumo = float(input("Consumo em GB: "))
        plano = input("Plano (R/E/C): ").upper()
        nivel = input("Nível de rede (N/M/A1/A2): ").upper()
        fatura = calcular_fatura(consumo, plano, nivel)
        print(f"Fatura final: R$ {fatura:.2f}")
    except ValueError:
        print("Entrada inválida, digite um número para o consumo.")
    except KeyError:
        print("Plano ou nível de rede inválido.")


def cadastrar_novo_assinante():
    try:
        id_assinante = int(input("ID do assinante: "))
        nome = input("Nome: ")
        plano = input("Plano (R/E/C): ").upper()
        if plano not in ("R", "E", "C"):
            print("Plano inválido.")
            return
        cadastrar_assinante(id_assinante, nome, plano)
        print(f"Assinante {nome} cadastrado com sucesso.")
    except ValueError:
        print("ID inválido, digite um número.")


def lancar_consumo_mensal():
    try:
        id_busca = int(input("ID do assinante: "))
        assinante = next((a for a in assinantes if a.id_assinante == id_busca), None)
        if assinante is None:
            print("Assinante não encontrado.")
            return
        mes = int(input("Mês (1-12): "))
        if not 1 <= mes <= 12:
            print("Mês inválido.")
            return
        consumo = float(input("Consumo em GB: "))
        assinante.historico[mes - 1] = consumo
        print(f"Consumo de {consumo}GB lançado para {assinante.nome} no mês {mes}.")
    except ValueError:
        print("Entrada inválida, digite números onde esperado.")


def ver_relatorios():
    if not assinantes:
        print("Nenhum assinante cadastrado ainda.")
        return
    print("\n--- Matriz de Consumo ---")
    matriz_consumo(assinantes)
    print("\n--- Conta Mais Alta ---")
    print(conta_mais_alta(assinantes))
    print("\n--- IDs Acima da Média ---")
    print(acima_da_media(assinantes))


def rodar():
    while True:
        print("\n=== Sistema de Faturamento ISP ===")
        print("1. Calcular fatura avulsa")
        print("2. Cadastrar assinante")
        print("3. Lançar consumo mensal")
        print("4. Ver relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            calcular_fatura_avulsa()
        elif opcao == "2":
            cadastrar_novo_assinante()
        elif opcao == "3":
            lancar_consumo_mensal()
        elif opcao == "4":
            ver_relatorios()
        elif opcao == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")