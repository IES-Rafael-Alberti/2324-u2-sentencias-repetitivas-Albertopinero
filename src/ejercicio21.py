def venta(monto):
    total = 0
    while monto != 0:
        if monto < 0:
            return monto
        return monto




if __name__ == "__main__":
    total = 0
    #entrada
    monto = float(input("Monto de una venta €: "))

    #proceso
    while monto != 0:
        if monto < 0:
            print("Monto no válido.")
        else:
            total += monto
            monto = float(input("Monto de una venta €: "))
        if total > 1000:
            total -= total*0.1

    #salida
    print("Monto total a pagar:", total,"€")