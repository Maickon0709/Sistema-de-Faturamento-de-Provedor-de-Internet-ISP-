import pytest
from motor_calculo import calcular_fatura


@pytest.mark.parametrize("consumo,plano,nivel,esperado", [
    (100, "R", "N", 59.36),
    (100, "E", "N", 108.11),
    (100, "C", "N", 218.73),
    (220, "R", "A1", 114.35),
])
def test_calcular_fatura_casos_validos(consumo, plano, nivel, esperado):
    assert calcular_fatura(consumo, plano, nivel) == esperado


def test_plano_invalido_gera_keyerror():
    with pytest.raises(KeyError):
        calcular_fatura(100, "X", "N")


def test_nivel_invalido_gera_keyerror():
    with pytest.raises(KeyError):
        calcular_fatura(100, "R", "Z")


def test_consumo_zero():
    resultado = calcular_fatura(0, "R", "N")
    assert resultado == 25.00


def test_consumo_multiplo_exato_de_50():
    resultado = calcular_fatura(50, "R", "M")
    assert resultado > 0