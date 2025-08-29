Codigo_factura = input("Ingrese el codigo de la factura: ")
Cliente = input("Ingrese el nombre del cliente: ")
Producto = input("Ingrese el producto vendido: ")
Cantidad = input("Ingrese la cantidad: ")
precio_unitario = input("Ingrese el precio unitario: ")

Cantidad = int(Cantidad)
precio_unitario = float(precio_unitario)

subtotal = (Cantidad * precio_unitario)
iva = subtotal * 0.19
total = subtotal + iva

archivo = open("facturas.txt", "a")
archivo.write(f"{Codigo_factura},{Cliente},{Producto},{Cantidad},{precio_unitario},{subtotal},{iva},{total}\n")
archivo.close()

print("Factura creada y guardada con éxito.")