import csv
import pandas as pd

empleados=[]

with open("documentos/empleados.csv","r") as archivo:
    lector=csv.reader(archivo)
    encabezado=next(lector) # leer solo el encabezado
    for empleado in lector:
        empleados.append([
            int(empleado[0]),
            empleado[1],
            float(empleado[2]),
            empleado[3],
            empleado[4]])  # list de list

print(empleados)

# quiero calcular el total del salario

total=0
for empleado in empleados:
    total=total+empleado[2]

print(f"el total es {total}")

# 1) crear un dataframe
# 2) y aplicar la operacion al dataframe

df=pd.DataFrame(empleados,columns=encabezado)
print(df)

print(df['salary'].sum())