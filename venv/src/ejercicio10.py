def numprimo():
    return True

if __name__ == "__main__":
    x = 2
    num = int(input("Escribe un número mayor que 2: "))
    while num <= 2:
            num = int(input("Escribe un número mayor que 2: "))
    while num % x != 0:
        x += 1
    if x == num:
        print(str(num) + " es primo")
    else:
        print(str(num) + " no es primo") 
