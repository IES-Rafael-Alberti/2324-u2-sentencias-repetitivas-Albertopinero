def numbers():
    return True

if __name__ == "__main__":
    #entrada
    num = int(input("Número positivo: "))
    
    #proceso
    mayor = -1
    while num >= 0:
        if num > mayor:
            mayor = num
    num = int(input("Número positivo: "))

    #salida
    print("Mayor número ingresado:", mayor)
