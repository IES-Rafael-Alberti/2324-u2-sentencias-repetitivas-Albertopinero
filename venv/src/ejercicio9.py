def seguridad(passw):
    password = "contraseña"
    for i in passw:
        while passw != password:
            return i
        return i

if __name__ == "__main__":
    
    #entrada
    passw = input("Escribe la contraseña: ")

    #proceso
    password = "contraseña"
    while passw != password:
        passw = input("Escribe la contraseña: ")
    
    #salida
    print("Contraseña Correcta!")   
