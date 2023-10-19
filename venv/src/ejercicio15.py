def numbers():
    return True

if __name__ == "__main__":
    positivos = 0
    sumando = []
    num = int(input("Número (0 para terminar): "))
    while num != 0:
        if num > 0:
            positivos += num
        num = int(input("Número (0 para terminar): "))
    print("Proceso Terminado, la suma de los números ingresados es:", positivos)
