from src.ejercicio9 import seguridad

def test_seguridad():
    passw = "contraseña"
    assert seguridad(passw) == "Contraseña Correcta!"
