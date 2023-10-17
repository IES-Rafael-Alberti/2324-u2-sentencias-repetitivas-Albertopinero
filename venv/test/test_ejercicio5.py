from src.ejercicio5 import inversion

def test_inversion():
    años = 37
    interes = 15
    cantidad = 37
    assert inversion(años,cantidad,interes) == True