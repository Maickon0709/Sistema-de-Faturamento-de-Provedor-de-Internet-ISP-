import pytest
from banco_dados import Assinante, cadastrar_assinante, assinantes


@pytest.fixture(autouse=True)
def limpar_assinantes():
    assinantes.clear()
    yield
    assinantes.clear()


def test_criar_assinante_inicializa_historico_com_doze_zeros():
    a = Assinante(1, "Ana", "R")
    assert a.historico == [0.0] * 12
    assert len(a.historico) == 12


def test_cadastrar_assinante_adiciona_na_lista_global():
    cadastrar_assinante(1, "Ana", "R")
    assert len(assinantes) == 1
    assert assinantes[0].nome == "Ana"


def test_cadastrar_assinante_retorna_o_objeto_criado():
    novo = cadastrar_assinante(2, "Bruno", "E")
    assert novo.id_assinante == 2
    assert novo.plano == "E"