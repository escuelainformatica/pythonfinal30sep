listados=["Chile","Argentina","Peru","Bolivia","Colombia","Brasil"]

print(listados)

for pais in listados:
    print(pais)

print("usando map:")

def mostrar(pais):
    print(pais)

map(mostrar,listados)

