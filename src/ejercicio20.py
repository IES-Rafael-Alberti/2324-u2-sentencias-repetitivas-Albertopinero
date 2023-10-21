def palabra(frase,letra):
    x = 0
    while x != len(frase):
        if letra != frase[x]:
            return letra
        return x



if __name__ == "__main__":
    x = 0
    #entrada
    frase = input("Escribe cualquier frase: ")
    letra = input("Letra para buscar su posición: ")

    #proceso
    while x != len(frase):
        if letra != frase[x]:
            print("No se encontró en la posición", x)
            x += 1
            continue
        break
        
    #salida
    print("Se encontró en la posición", x)