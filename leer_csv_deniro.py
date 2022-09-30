import csv
import pandas as pd

listafinal=[]  # lista vacia

with open("documentos/deniro.csv", "r") as archivo:
    lector=csv.reader(archivo,delimiter=",",skipinitialspace=True)
    encabezado=next(lector)  # leo la primera linea
    print(encabezado)
    for pelicula in lector:    # pelicula=["1988","33","nombre"]
        listafinal.append([int(pelicula[0]),int(pelicula[1]),pelicula[2]])

print(listafinal)  # list de list

tabla=pd.DataFrame(listafinal,columns=["año","score","pelicula"])
print(tabla)

valor=tabla['score'].sum()/tabla['score'].count()
print(f"El promedio #1 es {valor}")

promedio2=tabla['score'].mean()
print(f"El promedio #2 es : {promedio2}")



# sin usar pandas
total=0
for pelicula in listafinal:
    total=total+pelicula[1]  # sumar columna "score"

conteo=len(listafinal)

promedio=total/conteo

print(f"el promedio #3 es {promedio}")