terminar = False

def programa():
    opciones = '''
    1 ▶ Opción 1 - comenzar programa
    2 ▶ Opción 2 - imprimir listado
    3 ▶ Opción 3 - finalizar programa
    '''
    while not terminar:
        return opciones


if __name__ == "__main__":
    
    print(programa())

    while not terminar:
        #entrada
        opcion=int(input("Opción elegida: "))

        #proceso
        if opcion==1:
            print("¡Comenzamos el juego!")
        elif opcion==2:
            print("Listado:")
            print("Alberto, Luis, Javi, Adri")
        elif opcion==3:
            print("Hasta la próxima")
            break
        else:
            print("Opción incorrecta. Debe ingresar 1, 2 o 3")