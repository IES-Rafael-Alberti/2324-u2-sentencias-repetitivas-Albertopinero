def numeros(num):
    salir = 0
    sumando = []
    salir += num
    while num != 0:
        return num

if __name__ == "__main__":
    #entrada
    num = int(input("Escribe un número: "))

    #proceso
    salir = 0
    sumando = []
    salir += num
    while num != 0:
        sumando.append(num)
        num = int(input("Escribe otro número: "))
    resultado = sum(sumando)

    #salida
    print("Proceso Terminado, la suma de los números ingresados es ",resultado)