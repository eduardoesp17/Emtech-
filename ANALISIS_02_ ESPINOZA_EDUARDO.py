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

#COMENTARIO Y EXPLICACION
#Segui un procedimiento parecido para las tres consignas, primero extraje las columnas que más me interesaban, en la consigna 1 y 2 es principalmente la ruta, la dirección y el valor total
#En el caso de la primer consigna, separé las rutas por si eran exportación o importación de manera que después pudiera ordenarlas de mayor a menor para obtener las rutas más demandadas 
#Para la consigna 1 utilicé "value_counts" para contar las veces que se repetía la ruta y para el transporte utilicé "sum" para sumar el valor de cada transporte y ver cual era el más valioso
#En el valor, igualmenté extraje los datos que necesitaba, añadí producto también, posteriormente sumé todos los valores para que al conseguir el total del valor, pudiera obtener el valor relativo de cada ruta
#De esa manera, al utilizar "cumsum" pudiera detectar visualmente cuando se llegara al 80%. Guardé cada grupo de instrucciones como una función de manera que pudiera ser llamada de forma sencilla al establecer el comando del usuario cuando éste tiene que elegir una opción para visualizar
