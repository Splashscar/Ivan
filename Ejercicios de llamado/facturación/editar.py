try:
    archivo = open("facturas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
except:
    print("No hay registro que editar")
    exit()

if len(lineas) == 0:
    print("No hay registros para editar")
    exit()

# Listar registros
for numero, linea in enumerate(lineas, 1):
    datos = linea.strip().split(",")
    print(f"{numero}. {datos[0]} - {datos[1]}")

print()
numeroRegistro = int(input("Qué número de registro quiere editar: "))

if numeroRegistro < 1 or numeroRegistro > len(lineas):
    print("Número de registro no válido")
    exit()

# Mostrar datos actuales
datos_actuales = lineas[numeroRegistro - 1].strip().split(",")
print(f"\nDatos actuales del registro {numeroRegistro}")
print(f"Código de la factura: {datos_actuales[0]}")
print(f"Nombre del cliente: {datos_actuales[1]}")
print(f"Producto: {datos_actuales[2]}")
print(f"Cantidad de productos: {datos_actuales[3]}")
print(f"Precio unitario del producto: {datos_actuales[4]}")
print(f"Subtotal: {datos_actuales[5]}")
print(f"Iva: {datos_actuales[6]}")
print(f"Total: {datos_actuales[7]}")

print("\nIngrese los nuevos datos")
NuevoCodigo = input("Código Factura: ")
NuevoCliente = input("Cliente: ")
NuevoProducto = input("Producto: ")
NuevaCantidad = input("Cantidad: ")
NuevoPrecioUni = input("Precio unitario: ")

# Actualizar registro
lineas[numeroRegistro - 1] = (
    NuevoCodigo + "," + NuevoCliente + "," + NuevoProducto + "," +
    NuevaCantidad + "," + NuevoPrecioUni + "\n"
)

archivo = open("facturas.txt", "w")
archivo.writelines(lineas)
archivo.close()
print("✅ El registro cambió exitosamente")
