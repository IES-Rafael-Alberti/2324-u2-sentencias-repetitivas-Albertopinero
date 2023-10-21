def inversion(años,cantidad,interes):
    for i in range(años):
        cantidad *= 1 + interes / 100   
        return años
    
if __name__ == "__main__":
    #entrada
    cantidad = float(input("Escribe la cantidad a invertir: "))
    interes = float(input("Escribe tu interés anual: "))
    años = int(input("Escribe el número de años: "))

    #proceso
    for i in range(años):
        cantidad *= 1 + interes / 100
    
    #salida
        print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))