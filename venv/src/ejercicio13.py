def letras():
    return True

if __name__ == "__main__":
    #entrada
    palabra = input("Escribe lo que quieras, escribe salir para terminar el programa: ")

    #proceso
    while palabra == 'salir':
        print("Proceso Terminado")
    while palabra != 'salir':
            palabra = input("Escribe lo que quieras, escribe salir para terminar el programa: ")
