try:
    archivo = open("facturas.txt","r")
    lineas = archivo.readlines()
    archivo.close()
except:
    print("no hay registros")
    exit()    
if len(lineas) == 0:
    exit()
for numero, linea in enumerate (lineas,1):
    dato=linea.strip().split(",")
    print(f"{numero}, {dato[0]}, {dato[1]}")
print()
numero_registro = input("¿que numero de registro desea borrar? ")
numero_registro = int(numero_registro)
if numero_registro < 1 or numero_registro > len(lineas):
    print("el numero de registro no es valido")
    exit()
datos_borrar = lineas[numero_registro - 1].strip().split(",")
print(f"\nborrando registro {numero_registro}")
print(f"Codigo de factura a borrar: {datos_borrar[0]}")
print(f"Nombre del cliente a borrar: {datos_borrar[1]}")
print(f"Producto a borrar: {datos_borrar[2]}")
print(f"Cantidad a borrar: {datos_borrar[3]}")
print(f"Precio unitario a borrar: {datos_borrar[4]}")
confirmacion = input("\n estas seguro de borrar el registro (si/no): ")
if confirmacion.lower() == "si":
    del lineas[numero_registro - 1]
    archivo = open("facturas.txt", "w")
    archivo.writelines(lineas)
    archivo.close()
    print("registro borrado")
else:
    print("operacion cancelada")