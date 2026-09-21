from catalog import catalog 

print("Bienvenido/a al Catálogo de colección de Minerales y Piedras.")

#Ingreso y guardado de datos

for i in range(10):
    id = input("Ingrese el ID de la pieza: ")

    while True:
        name = input("Ingrese el nombre de la pieza: ")
        if name.strip() == "":
            print("El nombre no puede estar vacío")
        else:
            break

    category = input("¿Qué tipo de piedra o mineral es?: ")

    while True:
        try:
            price = float(input("Ingrese el precio estimado: "))
            if price > 0:
                break
            else:
                print("El precio debe ser mayor que cero")
        except:
            print("Eso no es un número válido")

    while True:
        status = input("Ingrese el estado de la pieza: ")
        if status in ["disponible", "reservada", "vendida"]:
            break
        else:
            print("Estado inválido. Debe ser: disponible, reservada o vendida")

    while True:
        description = input("Describa brevemente la pieza: ")
        if "usada" in description or "certificada" in description:
            break
        else:
            print("La descripción debe incluir la palabra 'usada' o 'certificada'")

    pieces = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    catalog.append(pieces)

print(catalog)

#Mostrar catálogo

for piece in catalog:
    print("ID:", piece["id"])
    print("Nombre:", piece["name"])
    print("Categoría:", piece["category"])
    print("Precio:", piece["price"])
    print("Estado:", piece["status"])
    print("Descripción:", piece["description"])
    print("---")

#Cantidad de piezas

print("Piezas registradas: ", len(catalog))

#Mostrar categorías

categories = set()

for piece in catalog:
    categories.add(piece["category"])
print("Categorías disponibles: ", len(categories))
print("Categorías: ", categories)

#Filtro de piezas por estado

counter = 0
for piece in catalog:
    if piece["status"] == "disponible":
        print(piece["name"])
        print("Pieza disponible para la venta")
        counter = counter + 1

if counter == 0:
    print("No hay piezas disponibles")

counter = 0
for piece in catalog:
    if piece["status"] == "reservada":
        print(piece["name"])
        print("Pieza reservada")
        counter = counter + 1

if counter == 0:
    print("No hay piezas reservadas")

counter = 0
for piece in catalog:
    if piece["status"] == "vendida":
        print(piece["name"])
        print("Pieza vendida")
        counter = counter + 1

if counter == 0:
    print("No hay piezas vendidas")

#Filtro de piezas por precio

while True:
    try:
        min_price = float(input("Ingrese el precio mínimo::"))
        break
    except:
        print("Error. Ingresa un valor numérico.")

counter = 0
for piece in catalog:
    if piece["price"] > min_price:
        print(piece["name"], "-", piece["price"])
        counter = counter + 1

if counter == 0:
    print("No se encontraron piezas")

# Piezas que pueden publicarse

for piece in catalog:
    if piece["price"] > 0 and piece["status"] == "disponible":
        print(piece["name"], "- Puede publicarse")
    else:
        print(piece["name"], "- No puede publicarse")

# Piezas que necesitan revisión

for piece in catalog:
    if piece["status"] == "reservada" or piece["status"] == "vendida":
        print(piece["name"], "- Requiere revisión")
    else:
        print(piece["name"], "- No requiere revisión")

# Mostrar piezas no vendidas

for piece in catalog:
    if piece["status"] != "vendida":
        print(piece["name"], "- No vendida")


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

#Métricas

available = 0
reserved = 0
sold = 0

for piece in catalog:
    if piece["status"] == "disponible":
        available = available + 1
    elif piece["status"] == "reservada":
        reserved = reserved + 1
    elif piece["status"] == "vendida":
        sold = sold + 1

print("Disponibles:", available)
print("Reservadas:", reserved)
print("Vendidas:", sold)
print("Total de piezas:", len(catalog))

for indice, piece in enumerate(catalog, start=1):
    print(indice, ".", piece["name"])

#Menú intercativo

while True:
    print("1. Mostrar todas las piezas")
    print("2. Mostrar piezas disponibles")
    print("3. Mostrar precio promedio")
    print("4. Salir")

    option = input("Ingrese una opción: ")

    if option == "1":
        for piece in catalog:
            print(piece)
    elif option == "2":
        for piece in catalog:
            if piece["status"] == "disponible":
                print(piece)
    elif option == "3":
        total_price = 0
        for piece in catalog:
            total_price += piece["price"]
        print("Precio promedio: ", total_price / len(catalog))
    elif option == "4":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción inválida")
