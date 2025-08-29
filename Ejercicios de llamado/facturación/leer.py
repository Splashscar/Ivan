try:
    archivo = open("facturas.txt", "r")

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
    print(f"Codigo factura: {datos[0]}")
    print(f"Cliente: {datos[1]}")
    print(f"Producto: {datos[2]}")
    print(f"Cantidad: {datos[3]}")
    print(f"Precio unitario: {datos[4]}")
    print(f"Subtotal: {datos[5]}")
    print(f"iva: {datos[6]}")
    print(f"Total: {datos[7]}")
    print("Fin de la información")