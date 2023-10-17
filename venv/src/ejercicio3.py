def numero(num):
    for i in range(1, num+1, 2):
        return True

if __name__ == "__main__":
    num = int(input("Escribe un número: "))
    for i in range(1, num+1, 2):
        print(i, end=", ")