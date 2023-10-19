def numero(num):
    for i in range(1, num+1, 2):
        return num

if __name__ == "__main__":
    #entrada
    num = int(input("Escribe un número: "))

    #proceso
    for i in range(1, num+1, 2):

    #salida
        print(i, end=", ")