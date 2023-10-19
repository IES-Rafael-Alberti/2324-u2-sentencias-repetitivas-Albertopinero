def triangulo(num):
    for i in range(num):
        return True
    
if __name__ == "__main__":
    num = int(input("Escribe la altura del triángulo: "))
    for i in range(num):
        print("*"*(i+1))