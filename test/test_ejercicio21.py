from src.ejercicio21 import venta

def test_venta():
    monto = 500
    assert venta(monto),2 == "Monto total a pagar: 600.0 €"