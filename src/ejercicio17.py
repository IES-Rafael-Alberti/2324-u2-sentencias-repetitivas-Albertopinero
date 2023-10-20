def sumando(num):
    while num != 0:
        return num
    
    


if __name__ == "__main__":
    suma = 0
    #entrada
    num=int(input("Número positivo: "))

    #proceso
    while num != 0:
        digito = num % 10
        suma += digito
        num = num // 10

    #salida
    print("Suma de los dígitos:", suma)