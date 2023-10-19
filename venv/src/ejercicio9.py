def seguridad():
    return True

if __name__ == "__main__":
    password = "contraseña"
    contraseña = input("Escribe la contraseña: ")
    while contraseña != password:
        contraseña = input("Escribe la contraseña: ")
    print("Contraseña Correcta!")   
