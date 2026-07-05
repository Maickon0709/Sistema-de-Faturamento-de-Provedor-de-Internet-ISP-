from motor_calculo import calcular_fatura


def matriz_consumo(assinantes):
    for a in assinantes:
        print(f"{a.nome}: {a.historico}")


def conta_mais_alta(assinantes, nivel="N"):
    maior = None
    maior_valor = -1
    for a in assinantes:
        for mes, consumo in enumerate(a.historico):
            valor = calcular_fatura(consumo, a.plano, nivel)
            if valor > maior_valor:
                maior_valor = valor
                maior = (a.nome, mes + 1, valor)
    return maior


def acima_da_media(assinantes):
    todos_consumos = [c for a in assinantes for c in a.historico]
    if not todos_consumos:
        return []
    media = sum(todos_consumos) / len(todos_consumos)
    return [a.id_assinante for a in assinantes if max(a.historico) > media]