def numbers():
    return True

if __name__ == "__main__":
    mayor = -1
    num = int(input("Número positivo: "))
    while num >= 0:
        if num > mayor:
            mayor = num
    num = int(input("Número positivo: "))
    print("Mayor número ingresado:", mayor)
