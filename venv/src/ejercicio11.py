def palabra():
    return True

if __name__ == "__main__":
    #entrada
    word = input("Escribe cualquier palabra: ")

    #proceso
    for i in range(len(word)-1, -1, -1):
    #salida
        print (word[i])