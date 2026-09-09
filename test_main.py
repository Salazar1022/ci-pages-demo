from main import saludo

def test_saludo():
    # Valor incorrecto a proposito para que pytest falle
    assert saludo () == "Hola Mundo"