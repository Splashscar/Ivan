try:
    archivo = open("inventario.txt", "r")

except:
    print("No hay registros guardados")
    exit()

lineas = archivo.readlines()
archivo.close()
if len(lineas) == 0:
    print("No hay registro guardado")
else:
    print(f"Se encontraron {len(lineas)} registros" )

for numero,lineas in enumerate(lineas, 1):
    lineas_limpiar = lineas.strip()
    datos = lineas_limpiar.split(",")
    print(f"registro # {numero}:")
    print(f"Producto: {datos[0]}")
    print(f"Descripción: {datos[1]}")
    print(f"Tipo: {datos[2]}")
    print(f"Precio: {datos[3]}")
    print("Fin de la información")