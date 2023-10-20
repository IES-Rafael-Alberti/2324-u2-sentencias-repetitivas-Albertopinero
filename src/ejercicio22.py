def parimpar(numero):
    while numero != 0:
        if ultimodigito % 2 == 0:
            return ultimodigito
        else:
            return numero
    
if __name__ == "__main__":
    
    #entrada
    numero = int(input("Escribe un número: "))

    #proceso
    totalPares = 0
    totalImpares = 0
    while numero != 0:
        pares = 0
        impares = 0
        while numero != 0:   
            ultimodigito = numero % 10
            if ultimodigito % 2 == 0:
                pares += 1
                totalPares += 1
            else:
                impares += 1
                totalImpares += 1
                numero=numero // 10
        print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
        numero = int(input("Otro número: "))

    #salida
    print("Total de dígitos pares:", totalPares)
    print("Total de dígitos impares:", totalImpares)