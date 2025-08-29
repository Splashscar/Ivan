try:
    facturas = []
    with open("facturasL.txt", "r") as archivo:
        for linea in archivo:
            facturas.append(linea.strip().split(","))
except:
    print("No hay registros guardados")
    exit()

if len(facturas) == 0:
    print("No hay registros guardados")
else:
    print(f"Se encontraron {len(facturas)} registros")

for i, datos in enumerate(facturas, 1):
    print(f"\nRegistro #{i}:")
    print(f"Código factura: {datos[0]}")
    print(f"Cliente: {datos[1]}")
    print(f"Producto: {datos[2]}")
    print(f"Cantidad: {datos[3]}")
    print(f"Precio unitario: {datos[4]}")
    print(f"Subtotal: {datos[5]}")
    print(f"IVA: {datos[6]}")
    print(f"Total: {datos[7]}")
    print("Fin de la información")
