def triangulo():
    return True
    
if __name__ == "__main__":
    #entrada
    num = int(input("Escribe la altura de triángulo: "))

    #proceso
    for i in range(1, num+1, 2):
        for x in range(i, 0, -2):

    #salida
            print(x, end=" ")
        print("")