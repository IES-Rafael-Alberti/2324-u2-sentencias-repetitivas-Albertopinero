from src.ejercicio9 import seguridad

def test_seguridad():
    passw = 'contraseña'
    assert seguridad(passw),1 == "Contraseña Correcta!"
