def seguridad(passw):
    password = "contraseña"
    while passw != password:
        return passw

if __name__ == "__main__":


    #entrada
    passw = input("Escribe la contraseña: ")

    #proceso
    password = "contraseña"
    while passw != password:
        passw = input("Escribe la contraseña: ")
    
    #salida
    print("Contraseña Correcta!")   
