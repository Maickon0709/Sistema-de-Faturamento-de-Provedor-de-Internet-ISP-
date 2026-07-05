IMPOSTO_ALIQUOTA = 0.2725

TARIFAS = {
    "R": {"td": 0.15, "ti": 0.10, "taxa_equip": 25.00},
    "E": {"td": 0.20, "ti": 0.15, "taxa_equip": 60.00},
    "C": {"td": 0.28, "ti": 0.22, "taxa_equip": 150.00},
}

NIVEL_REDE = {"N": 0.00, "M": 0.90, "A1": 2.50, "A2": 4.80}


def calcular_fatura(consumo_gb, plano, nivel):
    dados_plano = TARIFAS[plano]
    custo_base = consumo_gb * (dados_plano["td"] + dados_plano["ti"])
    acrescimo_rede = (consumo_gb // 50) * NIVEL_REDE[nivel]
    subtotal = custo_base + acrescimo_rede
    base_calculo = subtotal / (1 - IMPOSTO_ALIQUOTA)
    total = base_calculo + dados_plano["taxa_equip"]
    return round(total, 2)