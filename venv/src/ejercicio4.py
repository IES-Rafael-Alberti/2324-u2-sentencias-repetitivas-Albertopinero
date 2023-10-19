def numero(num):
    for i in range(num, -1 , -1):
        return num
    
if __name__ == "__main__":
    #entrada
    num = int(input("Escribe un número: "))

    #proceso
    for i in range(num, -1 , -1):

    #salida
        print(i, end=", ")