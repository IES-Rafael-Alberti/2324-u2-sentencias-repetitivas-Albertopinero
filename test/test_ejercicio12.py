from src.ejercicio12 import frase

def test_frase():
    palabras = "hola me llamo alberto"
    letra = "a"
    assert frase(palabras,letra),3 == "La letra a aparece  3 veces en la frase hola me llamo alberto"