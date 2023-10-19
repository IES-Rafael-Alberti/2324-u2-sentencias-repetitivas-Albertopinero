def seguridad():
    return True

if __name__ == "__main__":
    #entrada
    contraseña = input("Escribe la contraseña: ")

    #proceso
    password = "contraseña"
    while contraseña != password:
        contraseña = input("Escribe la contraseña: ")
    
    #salida
    print("Contraseña Correcta!")   
