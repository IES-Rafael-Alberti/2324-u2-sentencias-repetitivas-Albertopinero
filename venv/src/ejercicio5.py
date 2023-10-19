def inversion():   
        return True
    
if __name__ == "__main__":
    cantidad = float(input("Escribe la cantidad a invertir: "))
    interes = float(input("Escribe tu interés anual: "))
    años = int(input("Escribe el número de años: "))
    for i in range(años):
        cantidad *= 1 + interes / 100
        print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))