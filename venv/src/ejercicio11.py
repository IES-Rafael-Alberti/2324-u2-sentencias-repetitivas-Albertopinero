def palabra():
    return True

if __name__ == "__main__":
    word = input("Escribe cualquier palabra: ")
    for i in range(len(word)-1, -1, -1):
        print (word[i])