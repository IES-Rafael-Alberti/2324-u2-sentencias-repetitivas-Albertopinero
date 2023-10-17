def años(edad):
    for i in range(edad):
        return True
    
if __name__ == "__main__":
    edad = int(input("Escribe tu edad: "))
    for i in range(edad):
        print("Has cumplido ",str(i+1), "años") 