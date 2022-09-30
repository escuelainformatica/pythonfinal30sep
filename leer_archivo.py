f = open("documentos/texto.txt", "r", newline="\r\n")  # r indica de lectura
print(f.readline())
print(f.readline())
f.close()

with open("documentos/texto.txt", "r", newline="\r\n") as f:
    print(f.readline())
    print(f.readline())

