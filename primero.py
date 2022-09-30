import decimal

# variables

entero=20   # int
flotante=20.4  # float (20.39999999999)
texto="hola"  # str
bool=True  # bool
dec=decimal.Decimal("20.4")   # decimal 20.4

# grupo de varias
listados=["Chile","Argentina","Peru","Bolivia","Colombia","Brasil"]   # list
listados_tuples=("Chile","Argentina","Peru","Bolivia","Colombia","Brasil")   # tuple

# list vs tuple. el list es editable, el tuple es de solo lectura

# diccionario
cliente={"nombre":"john","edad":33}    # dict

# lista de diccionario

vehiculos=[
    {"marca":"mazda","patente":"aa-bb-45"},     # fila 0
    {"marca":"peugeot","patente":"aa-bb-45"},  # fila 1
    {"marca":"lada","patente":"aa-bb-45"},   # fila 2
]

# usar variables
print(entero)

# uso listado

print(listados[0])  # obtengo el primer elemento.
print(listados[0:2])  # desde el primer valor, obtiene dos valores
print(listados[:2])   # obtengo los dos primeros valores.
print(listados[3:])   # desde el tercer valor, obtiene to do el resto.

# uso diccionario
print(cliente['nombre']) # obtengo el nombre del cliente.

print(vehiculos[1]['marca'])  # obtener la marca de la fila #1



