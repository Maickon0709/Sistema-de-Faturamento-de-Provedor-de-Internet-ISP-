import pytest
from banco_dados import assinantes
from servico_assinante import registrar_assinante, buscar_assinante, registrar_consumo


@pytest.fixture(autouse=True)
def limpar_assinantes():
    assinantes.clear()
    yield
    assinantes.clear()


def test_registrar_assinante_com_plano_valido():
    novo = registrar_assinante(1, "Ana", "R")
    assert novo.nome == "Ana"
    assert novo.plano == "R"
    assert len(assinantes) == 1


def test_registrar_assinante_com_plano_invalido_gera_valueerror():
    with pytest.raises(ValueError):
        registrar_assinante(1, "Ana", "X")


def test_buscar_assinante_existente():
    registrar_assinante(1, "Ana", "R")
    encontrado = buscar_assinante(1)
    assert encontrado is not None
    assert encontrado.nome == "Ana"


def test_buscar_assinante_inexistente_retorna_none():
    resultado = buscar_assinante(999)
    assert resultado is None


def test_registrar_consumo_com_assinante_valido():
    registrar_assinante(1, "Ana", "R")
    assinante = registrar_consumo(1, 3, 150)
    assert assinante.historico[2] == 150


def test_registrar_consumo_assinante_inexistente_gera_valueerror():
    with pytest.raises(ValueError):
        registrar_consumo(999, 1, 100)


def test_registrar_consumo_mes_invalido_gera_valueerror():
    registrar_assinante(1, "Ana", "R")
    with pytest.raises(ValueError):
        registrar_consumo(1, 13, 100)