import json

from dataStructures.DoublyLinkedList import DoublyLinkedList
from model.Product import Product
from model.ShoppingListInterface import ShoppingListInterface
from model.User import User


class ShoppingListDoubly(ShoppingListInterface):
  def __init__(self, name, username):
    self.name = name
    self.username = username
    self.productos = DoublyLinkedList()
    self.cargar_productos_desde_json()

  def añadir_producto(self, nombre, precio, unidad, cantidad, categoria):
    producto = Product(nombre, precio, unidad, cantidad, categoria)
    self.productos.push_back(producto)
  
  def eliminar_producto(self, nombre_producto):
    current = self.productos.head
  
    while current:
      if current.data.nombre == nombre_producto:
        prev_node = current.prev
        next_node = current.next
  
        if prev_node:
          prev_node.next = next_node
        else:
          self.productos.head = next_node
  
        if next_node:
          next_node.prev = prev_node
        else:
          self.productos.tail = prev_node
  
        return
  
      current = current.next
  
    print(f"{nombre_producto} no se encontró en la lista de compras.")
  

  def modificar_producto(self, nombre_producto):
    current = self.productos.head
  
    while current:
      if current.data.nombre == nombre_producto:
        nuevo_precio = float(input(f"Nuevo precio para {nombre_producto}: "))
        nueva_cantidad = int(input(f"Nueva cantidad para {nombre_producto}: "))
        nueva_unidad = input(f"Nueva unidad para {nombre_producto}: ")
        current.data.precio = nuevo_precio
        current.data.cantidad = nueva_cantidad
        current.data.unidad = nueva_unidad
        return current.data
  
      current = current.next
  
    print(f"{nombre_producto} no se encontró en la lista de compras.")
    return None
    
  def marcar_comprado(self, nombre_producto):
    for producto in self.productos:
      if producto.nombre == nombre_producto:
        producto.comprado = True

  def filtrar_categoria(self, categoria):
      productos_filtrados = DoublyLinkedList()
      current = self.productos.head

      while current:
          if current.data.categoria == categoria:
              productos_filtrados.push_back(current.data)
          current = current.next

      if productos_filtrados.is_empty():
          print(f"No se encontraron productos en la categoría '{categoria}'")
      else:
          print(f"\033[1mProductos en la categoría '{categoria}':\033[0m")
          for producto in productos_filtrados:
              print(f"{producto.nombre} - Precio: {producto.precio} c/u - Cantidad: {producto.cantidad}")

      return productos_filtrados
    
  def buscar_producto(self, nombre_producto):
    current = self.productos.head
    while current:
      if current.data.nombre == nombre_producto:
        print(f"Producto: {current.data.nombre}")
        print(f"Precio: {current.data.precio}")
        print(f"Unidad: {current.data.unidad}")
        print(f"Cantidad: {current.data.cantidad}")
        print(f"Categoria: {current.data.categoria}")
        return current.data

      current = current.next
    print(f"{nombre_producto} no se encontro en la lista")
    return None

  def mostrar_lista(self):
        print(f'\033[1mTu Lista de Compras:\033[0m {self.name}\n\033[1mProductos:\033[0m')
        for producto in self.productos:
            if not producto.comprado:
                print(f"{producto.cantidad} {producto.unidad} de {producto.nombre} | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad} c/u")


  def guardar_productos_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    productos = []
    temp = self.productos.head
  
    while temp is not None:
      producto_data = {
          "nombre": temp.data.nombre,
          "precio": temp.data.precio,
          "unidad": temp.data.unidad,
          "cantidad": temp.data.cantidad,
          "categoria": temp.data.categoria
      }
      productos.append(producto_data)
      temp = temp.next
  
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


  def __str__(self):
    product_strings = [
        f"{producto.cantidad} {producto.unidad}s de {producto.nombre} | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad}"
        for producto in self.productos
    ]
    product_list = "\n".join(product_strings)
    return f'\033[1mTu Lista de Compras:\033[0m {self.name}\n\033[1mProductos:\033[0m\n{product_list}'


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