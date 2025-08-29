try:
    facturas = []
    with open("facturasL.txt", "r") as archivo:
        for linea in archivo:
            facturas.append(linea.strip().split(","))
except:
    print("No hay registros para editar")
    exit()

if len(facturas) == 0:
    print("No hay registros")
    exit()

for i, datos in enumerate(facturas, 1):
    print(f"{i}. {datos[0]} - {datos[1]}")

numero = int(input("\n¿Qué número de registro desea editar? "))

if numero < 1 or numero > len(facturas):
    print("Número inválido")
    exit()

factura = facturas[numero-1]

print(f"\nDatos actuales: {factura}")
NuevoCodigo = input("Código Factura: ")
NuevoCliente = input("Cliente: ")
NuevoProducto = input("Producto: ")
NuevaCantidad = input("Cantidad: ")
NuevoPrecio = input("Precio unitario: ")

subtotal = int(NuevaCantidad) * float(NuevoPrecio)
iva = subtotal * 0.19
total = subtotal + iva

facturas[numero-1] = [
    NuevoCodigo, NuevoCliente, NuevoProducto,
    NuevaCantidad, NuevoPrecio,
    str(subtotal), str(iva), str(total)
]

with open("facturasL.txt", "w") as archivo:
    for f in facturas:
        archivo.write(",".join(f) + "\n")

print(" Registro editado con éxito")
