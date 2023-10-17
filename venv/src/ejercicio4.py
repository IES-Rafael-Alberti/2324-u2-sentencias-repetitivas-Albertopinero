def numero(num):
    for i in range(num, -1 , -1):
        return True
    
if __name__ == "__main__":
    num = int(input("Escribe un número: "))
    for i in range(num, -1 , -1):
        print(i, end=", ")