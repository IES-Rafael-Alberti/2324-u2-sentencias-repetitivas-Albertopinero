def numbers():
    return True

if __name__ == "__main__":
    #entrada
    num = int(input("Número (0 para terminar): "))
    
    #proceso
    positivos = 0
    sumando = []
    while num != 0:
        if num > 0:
            positivos += num
        num = int(input("Número (0 para terminar): "))

    #salida    
    print("Proceso Terminado, la suma de los números ingresados es:", positivos)
