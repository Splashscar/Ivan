try:
    archivo = open("inventario.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
except:
    print("No hay registro que editar")

if len(lineas) == 0:
    print("No hay registros para editar")
    for numero,lineas in enumerate(lineas, 1):
        datos = lineas.strip().split(",")
        print(f" {numero}.{datos[0]}-{datos[1]}")
    print()

numeroRegistro = input("Que numero de registro quiere editar: ")
numeroRegistro = int(numeroRegistro)
if numeroRegistro < 1  or numeroRegistro > len(lineas):
    print("Numero de registro no valido")
    exit() 
    datos_actuales = lineas[numeroRegistro - 1].strip().split(",")
    print(f"Datos actuales del registro {numeroRegistro}")
    print(f"\n Nombre del producto: {datos_actuales[0]}")
    print(f"Descripcion del producto: {datos_actuales[1]}")
    print(f"Tipo de producto: {datos_actuales[2]}")
    print(f"Precio del producto: {datos_actuales[3]}")
    print("Ingrese los nuevos datos") 

NuevoNombre = input("Nombre: ")
NuevaDescripcion = input("Descripcion: ")
NuevoTipo = input("Tipo: ")
NuevoPrecio = input("Precio: ")
lineas[numeroRegistro - 1] = NuevoNombre + "," + NuevaDescripcion + "," + NuevoTipo + "," + NuevoPrecio + "," "\n"
archivo = open("inventario.txt", "w")
archivo.writelines(lineas)
archivo.close()
print("El registro cambio exitosamente")