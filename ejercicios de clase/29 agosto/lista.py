Lista = ["Jose", "Miguel", "Luis", "Pedro", "Pablo", "Ivan", "Juan"]
print(Lista[2:5])
for i in Lista:
    print(i)

Lista2 = Lista
print(Lista2)

Lista2 = Lista[-3]
Lista2 = Lista[:: -1]
Lista2 = Lista[:]
print (Lista2)

Lista2 = [1,2,5,7,9,8,10,12,15,20,30]
Lista[6] = "Pepe"
print(Lista)

Lista.append("Pedro Pablo")
print(Lista)

Lista.insert(6, "Natalia")
print(Lista)

Lista.extend(["Camilo", "Catalina", "Katherine"])
print(Lista)

Lista.remove("Pedro")
print(Lista)

Lista.pop(3)
print(Lista)

for i in range(len(Lista)):
    print(i,":", Lista[i])

lista3 = "Perencejo" in Lista
print(lista3)

Lista4 = ["a","a","b","b","c","c","a"]
cantidad = Lista.count("Jose")
print(cantidad)

Lista.sort()
print(Lista)

Lista2.sort()
print(Lista2)

lista5 = sorted(Lista)
print(lista5)

Lista.reverse()
print(Lista)

lista5 = Lista.copy()
print(lista5)

Lista6 = list(Lista)
print(Lista6)