import csv

with open("documentos/grades.csv", "r") as archivo:
    lector=csv.reader(archivo)
    for grado in lector:
        print(grado)