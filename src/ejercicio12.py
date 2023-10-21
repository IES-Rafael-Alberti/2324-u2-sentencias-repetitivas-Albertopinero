def frase(palabras,letra):
    contador = 0
    for i in palabras:
        if i == letra:
            contador += 1
        return i
    return i

if __name__ == "__main__":
    #entrada
    palabras = input("Escribe cualquier frase: ")
    letra = input("Escribe una letra: ")
    
    #proceso
    contador = 0
    for i in palabras:
        if i == letra:
            contador += 1
    
    #salida
    print("La letra %s aparece %2i veces en la frase %s" % (letra, contador, palabras))