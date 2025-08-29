try:
    archivo = open("inventario.txt","r")
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
print(f"nombre del producto a borrar a borrar: {datos_borrar[0]}")
print(f"descripción del producto a borrar: {datos_borrar[1]}")
print(f"Tipo de producto a borrar: {datos_borrar[2]}")
print(f"Precio de producto a borrar: {datos_borrar[3]}")
confirmacion = input("\n estas seguro de borrar el registro (si/no): ")
if confirmacion.lower() == "si":
    del lineas[numero_registro - 1]
    archivo = open("inventario.txt", "w")
    archivo.writelines(lineas)
    archivo.close()
    print("registro borrado")
else:
    print("operacion cancelada")