from functools import reduce

compras = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0  # para el total con un numero
for compra in compras:  # listado de compras, a una compra
    print(f"total: {total} + {compra}")
    total = total + compra

print(f"El total es {total}")

total2 = reduce(lambda t, s: t + s, compras)

print(f"el total2 es {total2}")
