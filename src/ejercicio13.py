def letras(palabra):
    while palabra != 'salir':
         return palabra

if __name__ == "__main__":
    #entrada
    palabra = input("Escribe lo que quieras, escribe salir para terminar el programa: ")

    #proceso
    while palabra != 'salir':
        palabra = input("Escribe lo que quieras, escribe salir para terminar el programa: ")
    print("Proceso Terminado!")
    
