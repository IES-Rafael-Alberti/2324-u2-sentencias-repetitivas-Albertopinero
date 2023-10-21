from src.ejercicio5 import inversion

def test_inversion():
    años = 3
    cantidad = 5
    interes = 10
    assert inversion(años,cantidad,interes),3 == "Capital tras 1 años: 5.5"