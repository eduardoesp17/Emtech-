# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

archivo = pd.read_csv(r'C:\Users\patok\Documents\CursoDataScienceSantander\ReporteProyecto2\synergy_logistics_database.csv', index_col = 0)

"""
flujos = archivo["direction"].value_counts()
print(flujos)

flujosexp = archivo[["direction", "origin", "destination"]]
print()


print(archivo.sort_values(["direction", "origin", "destination"]))
"""
#CONSIGNA 1
# Exportaciones

onlyexports= archivo[archivo["direction"] == "Exports"]
sumbyexports = onlyexports.loc[:, ["direction", "origin", "destination"]] 
exportscount = sumbyexports.groupby(["origin", "destination"])["direction"].count()
exportsmax = exportscount.sort_values(ascending = False)


print("10 rutas con mayor exportaciones\n", exportsmax.iloc[:10])
# Importaciones

onlyimports= archivo[archivo["direction"] == "Imports"]
sumbyimports = onlyimports.loc[:, ["direction", "origin", "destination"]] 
importscount = sumbyimports.groupby(["origin", "destination"])["direction"].count()
importsmax = importscount.sort_values(ascending = False)

print("10 rutas con mayor importaciones\n", importsmax.iloc[:10])

#CONSIGNA 2
#Medios de transporte

transport = archivo.loc[:, ["transport_mode","total_value"]]
transportsum = transport.groupby("transport_mode")["total_value"].sum()
transportsort = transportsum.sort_values(ascending = False)
print("Tres modos de transporte más importantes por valor de exportaciones e importaciones\n", transportsort.iloc[:3])

#CONSIGNA 3
#Valor de exportaciones e importaciones

valormax = archivo.loc[:, ["origin", "destination", "product", "total_value"]]
valortotal = archivo["total_value"].sum()
valormax["valor_proportion"] = (valormax["total_value"] / valortotal) * 100
valorsort = valormax.sort_values("valor_proportion", ascending = False) 
valorsort["valor_cumsum"] = valorsort["valor_proportion"].cumsum() 

print("Rutas que representan el 80% del valor de las exp e imp\n", valorsort.iloc[:12])


"""    
    print("País de origen:", importsmax[index][0], "País de destino:", importsmax[index][1], "Numero de importaciones:", 
          importsmax[index][2])
"""    
"""
print(archivo.groupby(["origin", "destination"])["direction"].agg(max))
"""