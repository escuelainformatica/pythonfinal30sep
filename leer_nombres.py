with open("documentos/nombres.txt", "r") as archivo:
    todo=archivo.read()  # str
    nombres=todo.split("\n") # list str
    print(nombres)

conteo=len(nombres)
print(f"La cantidad de nombres es {conteo}")