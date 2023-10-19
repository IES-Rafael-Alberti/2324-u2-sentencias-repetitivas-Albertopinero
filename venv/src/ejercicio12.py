def frase():
    return True

if __name__ == "__main__":
    palabras = input("Escribe cualquier frase: ")
    letra = input("Escribe una letra: ")
    contador = 0
    for i in palabras:
        if i == letra:
            contador += 1
    print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, palabras))