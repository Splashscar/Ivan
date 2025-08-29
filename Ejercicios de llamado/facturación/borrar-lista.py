try:
    facturas = []
    with open("facturasL.txt", "r") as archivo:
        for linea in archivo:
            facturas.append(linea.strip().split(","))
except:
    print("No hay registros")
    exit()

if len(facturas) == 0:
    print("No hay registros para borrar")
    exit()

for i, datos in enumerate(facturas, 1):
    print(f"{i}. {datos[0]} - {datos[1]}")

numero = int(input("\n¿Qué número de registro desea borrar? "))

if numero < 1 or numero > len(facturas):
    print("Número inválido")
    exit()

print(f"\nBorrando factura #{numero}: {facturas[numero-1]}")
confirmacion = input("¿Seguro que desea borrar? (si/no): ")

if confirmacion.lower() == "si":
    del facturas[numero-1]
    with open("facturasL.txt", "w") as archivo:
        for f in facturas:
            archivo.write(",".join(f) + "\n")
    print(" Registro borrado")
else:
    print(" Operación cancelada")
