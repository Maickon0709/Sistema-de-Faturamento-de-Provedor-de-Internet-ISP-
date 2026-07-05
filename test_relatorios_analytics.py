from banco_dados import Assinante
from relatorios_analytics import conta_mais_alta, acima_da_media


def test_conta_mais_alta_identifica_maior_fatura():
    a1 = Assinante(1, "Ana", "R")
    a1.historico[0] = 100

    a2 = Assinante(2, "Bruno", "C")
    a2.historico[0] = 100

    resultado = conta_mais_alta([a1, a2])
    nome, mes, valor = resultado
    assert nome == "Bruno"


def test_acima_da_media_detecta_consumo_atipico():
    a1 = Assinante(1, "Ana", "R")
    a1.historico[0] = 500

    a2 = Assinante(2, "Bruno", "R")
    a2.historico[0] = 10

    a3 = Assinante(3, "Carla", "R")
    a3.historico[0] = 10

    resultado = acima_da_media([a1, a2, a3])
    assert resultado == [1]


def test_acima_da_media_lista_vazia_nao_quebra():
    assert acima_da_media([]) == []