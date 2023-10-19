from src.ejercicio19 import palabra

def test_palabra():
    frase = "hola me llamo alberto"
    letra = "a"
    assert palabra(frase,letra),3 == "Se encontró en la posición 3"