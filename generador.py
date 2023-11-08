import json
import random

# Lista de posibles categorías
categorias = ["Lacteos", "Dulces", "Pescados", "Frutas", "Verduras", "Carnes", "Panaderia"]

# Mezclar aleatoriamente las categorías
random.shuffle(categorias)

productos = []
for i in range(100000):
    producto = {
        "nombre": f"Producto{i}",
        "precio": random.uniform(1.0, 100.0),  # Precio aleatorio entre 1.0 y 100.0
        "unidad": random.choice(["unidad", "paquete", "kg"]),  # Unidad aleatoria
        "cantidad": random.randint(1, 10),  # Cantidad aleatoria entre 1 y 10
        "categoria": categorias[i % len(categorias)]  # Categoría aleatoria sin repeticiones
    }
    productos.append(producto)

# Mezclar aleatoriamente la lista de productos
random.shuffle(productos)

# Guardar la lista de productos en un archivo JSON
with open("productos-con-categorias.json", "w") as archivo_json:
    json.dump(productos, archivo_json, indent=4)

print("Archivo JSON generado con productos en un orden aleatorio y categorías sin repeticiones.")
