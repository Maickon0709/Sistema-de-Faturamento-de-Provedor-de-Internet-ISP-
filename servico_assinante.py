# servico_assinante.py
from banco_dados_poo import cadastrar_assinante, assinantes

PLANOS_VALIDOS = ("R", "E", "C")

def registrar_assinante(id_assinante, nome, plano):
    if plano not in PLANOS_VALIDOS:
        raise ValueError("Plano inválido.")
    return cadastrar_assinante(id_assinante, nome, plano)

def buscar_assinante(id_busca):
    return next((a for a in assinantes if a.id_assinante == id_busca), None)

def registrar_consumo(id_busca, mes, consumo):
    assinante = buscar_assinante(id_busca)
    if assinante is None:
        raise ValueError("Assinante não encontrado.")
    if not 1 <= mes <= 12:
        raise ValueError("Mês inválido.")
    assinante.historico[mes - 1] = consumo
    return assinante