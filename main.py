from catalog import catalog 

print("Bienvenido/a al Catálogo de colección de Minerales y Piedras.")

#Ingreso y guardado de datos

for i in range(10):
    id = input("Ingrese el ID de la pieza: ")
    name = input("Ingrese el nombre de la pieza: ")
    category = input("¿Qué tipo de piedra o mineral es?: ")
    price = float(input("Ingrese el precio estimado: "))
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

#Mostrar catálogo

for pieza in catalog:
    print("ID:", pieza["id"])
    print("Nombre:", pieza["name"])
    print("Categoría:", pieza["category"])
    print("Precio:", pieza["price"])
    print("Estado:", pieza["status"])
    print("Descripción:", pieza["description"])
    print("---")

#Cantidad de piezas

print("Piezas registradas: ", len(catalog))

#Mostrar categorías

categories = set()

for pieza in catalog:
    categories.add(pieza["category"])
print("Categorías disponibles: ", len(categories))
print("Categorías: ", categories)

#Filtro de piezas por estado

contador = 0
for pieza in catalog:
    if pieza["status"] == "disponible":
        print(pieza["name"])
        print("Pieza disponible para la venta")
        contador = contador + 1

if contador == 0:
    print("No hay piezas disponibles")

contador = 0
for pieza in catalog:
    if pieza["status"] == "reservada":
        print(pieza["name"])
        print("Pieza reservada")
        contador = contador + 1

if contador == 0:
    print("No hay piezas reservadas")

contador = 0
for pieza in catalog:
    if pieza["status"] == "vendida":
        print(pieza["name"])
        print("Pieza vendida")
        contador = contador + 1

if contador == 0:
    print("No hay piezas vendidas")

#Filtro de piezas por precio

while True:
    try:
        min_price = float(input("Ingrese el precio mínimo::"))
        break
    except:
        print("Error. Ingresa un valor numérico.")

contador = 0
for pieza in catalog:
    if pieza["price"] > min_price:
        print(pieza["name"], "-", pieza["price"])
        contador = contador + 1

if contador == 0:
    print("No se encontraron piezas")

# Piezas que pueden publicarse

for pieza in catalog:
    if pieza["price"] > 0 and pieza["status"] == "disponible":
        print(pieza["name"], "- Puede publicarse")
    else:
        print(pieza["name"], "- No puede publicarse")

# Piezas que necesitan revisión

for pieza in catalog:
    if pieza["status"] == "reservada" or pieza["status"] == "vendida":
        print(pieza["name"], "- Requiere revisión")
    else:
        print(pieza["name"], "- No requiere revisión")

# Mostrar piezas no vendidas

for pieza in catalog:
    if pieza["status"] != "vendida":
        print(pieza["name"], "- No vendida")


#Concatenación

print(catalog[0]["name"] + " - " + catalog[0]["category"] + " - " + str(catalog[0]["price"]) + " - " + catalog[0]["status"] + " - " + catalog[0]["description"])

#Interpolación

print(f"{catalog[0]['name']} - {catalog[0]['category']} - {catalog[0]['price']} - {catalog[0]['status']} - {catalog[0]['description']}")

#Etiquetas

tags = input("Ingrese etiquetas (separadas por comas): ")
tags_list = tags.split(",")
print(tags_list)

#Reemplazo de palabra en descripción

new_description = catalog[0]["description"].replace("usada", "certificada")
print(new_description)

#Ingreso de usuario

username = input("Ingrese su nombre de usuario: ")
print(username.strip())
print(username.lower())
print(username.upper())
print(username.title())

#Formato normalizado

normalized_name = catalog[0]["name"].strip().title()
print("Pieza: ", normalized_name)


#Menú intercativo

while True:
    print("1. Mostrar todas las piezas")
    print("2. Mostrar piezas disponibles")
    print("3. Mostrar precio promedio")
    print("4. Salir")

    option = input("Ingrese una opción: ")

    if option == "1":
        for pieza in catalog:
            print(pieza)
    elif option == "2":
        for pieza in catalog:
            if pieza["status"] == "disponible":
                print(pieza)
    elif option == "3":
        total_price = 0
        for pieza in catalog:
            total_price += pieza["price"]
        print("Precio promedio: ", total_price / len(catalog))
    elif option == "4":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción inválida")