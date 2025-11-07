from imc import *

def test_calcular_imc():
    assert calcular_imc(70, 1.75) == 22.86
    assert calcular_imc(70, 1.75) == round(22.857142857, 2)
    assert calcular_imc(70, 0) == False


def test_classificar_imc_abaixo_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"
    assert classificar_imc(22.0) == "Peso normal"
    assert classificar_imc(27.3) == "Sobrepeso"
    assert classificar_imc(33.0) == "Obesidade grau I"
    assert classificar_imc(37.0) == "Obesidade grau II"
    assert classificar_imc(45.0) == "Obesidade grau III"
