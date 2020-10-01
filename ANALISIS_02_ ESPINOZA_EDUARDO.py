import pandas as pd

archivo = pd.read_csv(r'C:\Users\patok\Documents\CursoDataScienceSantander\ReporteProyecto2\synergy_logistics_database.csv', index_col = 0)

#CONSIGNA 1
# Exportaciones

def exportaciones():
    onlyexports= archivo[archivo["direction"] == "Exports"]
    sumbyexports = onlyexports.loc[:, ["direction", "origin", "destination"]] 
    exportscount = sumbyexports.groupby(["origin", "destination"])["direction"].count()
    exportsmax = exportscount.sort_values(ascending = False)
    print("10 rutas con mayor exportaciones\n", exportsmax.iloc[:10])
    
# Importaciones
def importaciones():
    onlyimports= archivo[archivo["direction"] == "Imports"]
    sumbyimports = onlyimports.loc[:, ["direction", "origin", "destination"]] 
    importscount = sumbyimports.groupby(["origin", "destination"])["direction"].count()
    importsmax = importscount.sort_values(ascending = False)
    print("10 rutas con mayor importaciones\n", importsmax.iloc[:10])

#CONSIGNA 2
#Medios de transporte
def transporte():
    transport = archivo.loc[:, ["transport_mode","total_value"]]
    transportsum = transport.groupby("transport_mode")["total_value"].sum()
    transportsort = transportsum.sort_values(ascending = False)
    print("Tres modos de transporte más importantes por valor de exportaciones e importaciones\n", transportsort.iloc[:3])

#CONSIGNA 3
#Valor de exportaciones e importaciones
def valor():
    valormax = archivo.loc[:, ["origin", "destination", "product", "total_value"]]
    valortotal = archivo["total_value"].sum()
    valormax["valor_proportion"] = (valormax["total_value"] / valortotal) * 100
    valorsort = valormax.sort_values("valor_proportion", ascending = False) 
    valorsort["valor_cumsum"] = valorsort["valor_proportion"].cumsum() 
    print("Rutas que representan el 80% del valor de las exp e imp\n", valorsort.iloc[:12])

opcion = int(input("Hola, bienvenido\n Elige una opción a consultar:\n 1.- 10 rutas con mayores expoertaciones\n 2.- 10 rutas con mayores importaciones\n 3.- Tres transportes más usados\n 4.- Conjunto de países que conforman el 80% del valor de las rutas\n"))

if opcion == 1:
    exportaciones()
elif opcion == 2:
    importaciones()
elif opcion == 3:
    transporte()
elif opcion == 4:
    valor()
else:
    print("La opción que seleccionaste no es correcta")

