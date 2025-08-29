from decimal import Decimal

Codigo_factura = input("Ingrese el código de la factura: ")
Cliente = input("Ingrese el nombre del cliente: ")
Producto = input("Ingrese el producto vendido: ")
Cantidad = int(input("Ingrese la cantidad: "))
precio_unitario = float(input("Ingrese el precio unitario: "))

subtotal = Cantidad * precio_unitario
iva = subtotal * 0.19
total = subtotal + iva

factura = [
    Codigo_factura, Cliente, Producto,
    str(Cantidad), str(precio_unitario),
    str(subtotal), str(iva), str(total)
]

with open("facturasL.txt", "a") as archivo:
    archivo.write(",".join(factura) + "\n")

print("Factura creada y guardada con éxito.")
