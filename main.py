from catalog import catalog 

print("Bienvenido/a al Catálogo de colección de Minerales y Piedras.")

#Piezas
for i in range (10):
    id = input("Ingrese el ID de la pieza: ")
    name = input("Ingrese el nombre de la pieza: ")
    category = input("¿Qué tipo de piedra o mineral es?: ")
    price = input("Ingrese el precio estimado: ")
    status = input("Ingrese el estado de la pieza: ")
    description = input("Describa brevemente la pieza: ")
    
    piezas = {
    "id" : id,
    "name" : name,
    "category" : category,
    "price" : price,
    "status" : status,
    "description" : description
    }
    
    catalog.append(piezas)

print(catalog)