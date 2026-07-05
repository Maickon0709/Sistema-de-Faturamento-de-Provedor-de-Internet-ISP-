from motor_calculo import calcular_fatura
from banco_dados import assinantes
from relatorios_analytics import matriz_consumo, conta_mais_alta, acima_da_media
from servico_assinante import registrar_assinante, registrar_consumo


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
        registrar_assinante(id_assinante, nome, plano)
        print(f"Assinante {nome} cadastrado com sucesso.")
    except ValueError as e:
        print(e)


def lancar_consumo_mensal():
    try:
        id_busca = int(input("ID do assinante: "))
        mes = int(input("Mês (1-12): "))
        consumo = float(input("Consumo em GB: "))
        assinante = registrar_consumo(id_busca, mes, consumo)
        print(f"Consumo de {consumo}GB lançado para {assinante.nome} no mês {mes}.")
    except ValueError as e:
        print(e)


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