def numeros(num):
    while num != -1:
        if num % 2 == 0:
            return num
        while num != 0:
            return num
    


if __name__ == "__main__":
    pares = 0
    #entrada
    num = int(input("Número (-1 para terminar el programa): "))

    #proceso
    while num != -1:
        if num % 2 == 0:
            pares += 1
        suma=0
        while num != 0:
            digito = num % 10
            suma += digito
            num = num // 10

    #salida
        print("Suma de sus dígitos:", suma)
        num = int(input("Número (-1 para terminar el programa): "))
    print("Se ingresaron", pares, "números pares")