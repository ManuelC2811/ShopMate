import json

from dataStructures.DynamicArray import DynamicArray as Array
from model.Product import Product
from model.ShoppingListInterface import ShoppingListInterface
from model.User import User


class ShoppingArray(ShoppingListInterface):
  
  def __init__(self, name, username):
    self.name = name
    self.username = username
    self.productos = Array()
    self.cargar_productos_desde_json()

  def añadir_producto(self, nombre, precio, unidad, cantidad, categoria):
    producto = Product(nombre, precio, unidad, cantidad, categoria)
    self.productos.append(producto)
    
  def display_products_with_indices(self):
    if len(self.productos) == 0:
        print("La lista de compras está vacía.")
    else:
        print("Productos en la lista de compras:")
        for i, product in enumerate(self.productos):
            print(
                f"{i + 1}. {product.nombre} - Precio: {product.precio} - Cantidad: {product.cantidad}")

  def eliminar_producto(self, indice_producto):
    if len(self.productos) == 0:
        print("La lista de compras está vacía.")
        return None

    self.display_products_with_indices()

    try:
        indice_producto -= 1
        if 0 <= indice_producto < len(self.productos):
            self.productos.delete(indice_producto)
            #removed = self.productos[indice_producto+1]
            #print(f"Producto eliminado: {removed.nombre} - Precio: {removed.precio} - Cantidad: {removed.cantidad}")
            #return removed
        else:
            print("Indice fuera de rango, ingrese un valor válido")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero como índice.")


  def __str__(self):
    if len(self.productos) == 0:
        return f'\033[1mTu Lista de Compras:\033[0m {self.name}\n\033[1mProductos:\033[0m\n(No hay productos en la lista)'
    
    product_strings = [
        f"{i + 1}. {producto.nombre} - {producto.cantidad} {producto.unidad}s | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad} c/u"
        for i, producto in enumerate(self.productos)
    ]
    product_list = "\n".join(product_strings)
    
    return f'\n\033[1mTu Lista de Compras:\033[0m {self.name}\n\033[1mProductos:\033[0m\n{product_list}'
    

  def modificar_producto(self, indice_producto):
    indice_producto -= 1
    if indice_producto < 0 or indice_producto >= len(self.productos):
        print("No se encontró en la lista de compras.")
        return None

    nuevo_precio = float(input(f"Nuevo precio: "))
    nueva_cantidad = int(input(f"Nueva cantidad: "))
    nueva_unidad = input(f"Nueva unidad: ")

    current = self.productos.__getitem__(indice_producto)

    current.precio = nuevo_precio
    current.cantidad = nueva_cantidad
    current.unidad = nueva_unidad

  def marcar_comprado(self, nombre_producto):
    for producto in self.productos:
      if producto.nombre == nombre_producto:
        producto.estado = True

  def filtrar_categoria(self, categoria):
      productos_filtrados = Array()

      for producto in self.productos:
            if producto.categoria == categoria:
                productos_filtrados.append(producto)

      if productos_filtrados.is_empty():
            print(f"No se encontraron productos en la categoría '{categoria}'")
      else:
            print(f"\033[1mProductos en la categoría '{categoria}':\033[0m")
            for producto in productos_filtrados:
                print(f"{producto.nombre} - Precio: {producto.precio} c/u - Cantidad: {producto.cantidad}")

      return productos_filtrados
    
  def buscar_producto(self, indice_producto):
    indice_producto -= 1
    if 0> indice_producto >= len(self.productos):
      print(f"El indice {indice_producto} no es válido")
    else:
      current = self.productos.__getitem__(indice_producto)
      print(f"Producto: {current.nombre}")
      print(f"Precio: {current.precio}")
      print(f"Unidad: {current.unidad}")
      print(f"Cantidad: {current.cantidad}")
      print(f"Categoria: {current.categoria}")


  def mostrar_lista(self):
    print(f'\033[1mTu Lista de Compras:\033[0m {self.name}\n\033[1mProductos añadidos al carrito:\033[0m')
    for producto in self.productos:
        if producto.estado:
            print(f"{producto.cantidad} {producto.unidad} de {producto.nombre} | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad} c/u")


  def guardar_productos_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    productos = []
    ide = 0
    for producto in self.productos:
      producto_data = {
          "nombre": producto.nombre,
          "precio": producto.precio,
          "unidad": producto.unidad,
          "cantidad": producto.cantidad,
          "categoria": producto.categoria,
          "id": ide,
      }
      ide += 1
      productos.append(producto_data)
  
    with open(file_name, 'w') as archivo_json:
      json.dump(productos, archivo_json)


  def cargar_productos_desde_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    try:
      with open(file_name, 'r') as archivo_json:
        productos = json.load(archivo_json)
        for producto_data in productos:
          nombre = producto_data["nombre"]
          precio = producto_data["precio"]
          unidad = producto_data["unidad"]
          cantidad = producto_data["cantidad"]
          categoria = producto_data["categoria"]
          self.añadir_producto(nombre, precio, unidad, cantidad, categoria)
    except FileNotFoundError:
      pass
    except json.JSONDecodeError:
      pass


  #revisar para test
  def añadir_productos_desde_json(self, json_file):
        try:
            with open(json_file, 'r') as archivo_json:
                productos = json.load(archivo_json)
                for producto_data in productos:
                    nombre = producto_data["nombre"]
                    precio = producto_data["precio"]
                    unidad = producto_data["unidad"]
                    cantidad = producto_data["cantidad"]
                    categoria = producto_data["categoria"]
                    self.añadir_producto(nombre, precio, unidad, cantidad, categoria)
        except FileNotFoundError:
            print("El archivo JSON no se encontró.")
   
  