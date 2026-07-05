from motor_calculo import calcular_fatura

def rodar():
    while True:
        try:
            consumo = float(input("Consumo em GB:"))
            plano = input("Plano (R/E/C): ").upper()
            nivel = input("Nível de rede (N/M/A1/A2): ").upper()
            fatura = calcular_fatura(consumo, plano, nivel)
            print(f"Fatura final: R$: {fatura:.2f}")
        except ValueError:
            print("Entrada inválida, digite um número para o consumo.")
        except KeyError:
            print("Plano ou nível de rede inválido.")

        continuar = input("Calcular outra? (s/n): ").lower()
        if continuar != "s":
            break