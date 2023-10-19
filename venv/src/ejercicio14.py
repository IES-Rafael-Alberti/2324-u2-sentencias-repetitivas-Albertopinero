def numeros():
    return True

if __name__ == "__main__":
    salir = 0
    sumando = []
    num = int(input("Escribe un número: "))
    salir += num
    while num != 0:
        sumando.append(num)
        num = int(input("Escribe otro número: "))
    resultado = sum(sumando)
    print("Proceso Terminado, la suma de los números ingresados es ",resultado)