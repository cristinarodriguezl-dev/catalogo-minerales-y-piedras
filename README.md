# Catálogo de Minerales y Piedras

## Objetivo

Programa en Python que funciona por consola y permite gestionar un catálogo básico de piezas coleccionables. Permite registrar piezas, consultar la información del catálogo, aplicar filtros, calcular métricas y validar los datos ingresados por el usuario.

## Contexto

El catálogo está orientado a una colección de minerales y piedras (cuarzos, gemas, rocas, etc.), donde cada pieza representa un ejemplar con su identificador, nombre, categoría, precio, estado de venta y una descripción.

## Funcionalidades implementadas

- Registro de 10 piezas coleccionables por terminal.
- Almacenamiento de las piezas en una colección principal (`catalog`).
- Consulta y visualización de todas las piezas del catálogo.
- Cálculo de categorías únicas registradas.
- Filtrado de piezas por estado (`disponible`, `reservada`, `vendida`).
- Filtrado de piezas por precio mínimo.
- Reglas de negocio: piezas que pueden publicarse, piezas que requieren revisión, piezas no vendidas.
- Operaciones con strings: concatenación, interpolación, separación de etiquetas, reemplazo de palabras, formateo de texto (mayúsculas, minúsculas, formato título) y normalización de nombres.
- Menú interactivo con opciones para mostrar todas las piezas, mostrar piezas disponibles, calcular el precio promedio y salir.
- Cálculo de métricas: cantidad de piezas por estado, cantidad total, suma y precio promedio del catálogo.
- Validaciones de los datos ingresados (precio numérico y mayor que cero, nombre no vacío, estado permitido, descripción con palabra obligatoria, opción de menú válida).

## Estructura de una pieza

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Texto | Identificador único de la pieza |
| `name` | Texto | Nombre de la pieza |
| `category` | Texto | Categoría a la que pertenece |
| `price` | Número decimal | Precio de venta o valor de referencia |
| `status` | Texto | Estado actual de la pieza |
| `description` | Texto | Descripción detallada de la pieza |

### Estados permitidos
- `disponible`
- `reservada`
- `vendida`

### Descripción
Debe incluir obligatoriamente la palabra `usada` o `certificada`.

## Tecnologías utilizadas

- Python 3
  
## Cómo ejecutar el programa
 
1. Asegúrate de tener Python 3 instalado en tu equipo.
2. Descarga o clona este repositorio en tu equipo.
3. Abre una terminal (o consola de comandos).
4. Ejecuta el archivo principal con el siguiente comando:
```bash
   python main.py
```
5. Sigue las instrucciones que aparecen por pantalla para ir introduciendo los datos de las piezas.
   
## Ejemplo de interacción

<img width="922" height="237" alt="image" src="https://github.com/user-attachments/assets/11869732-f98c-415a-a838-7b4dffcd1ea9" />
