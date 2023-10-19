def numprimo(num):
    x = 2
    while num <= 2:
        return num    
    while num % x != 0:
        return num
    if x == num:
        return num
    else:
        return num


if __name__ == "__main__":
    #entrada
    num = int(input("Escribe un número mayor que 2: "))

    #proceso
    x = 2
    while num <= 2:
            num = int(input("Escribe un número mayor que 2: "))
    while num % x != 0:
        x += 1
    if x == num:
        print(str(num) + " es primo")
    else:
        print(str(num) + " no es primo") 
