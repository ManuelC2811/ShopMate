import json

from dataStructures.BST import BST
from model.Product import Product
from model.ShoppingListInterface import ShoppingListInterface
from model.User import User


class ShoppingList(ShoppingListInterface):
  def __init__(self, name, username):
    self.name = name
    self.username = username
    self.productos = BST()
    self.cargar_productos_desde_json()

  def añadir_producto(self, nombre, precio, unidad, cantidad, categoria):
    producto = Product(nombre, precio, unidad, cantidad, categoria)
    self.productos.insert(producto)

  def eliminar_producto(self, nombre_producto):
    return self.productos.remove(nombre_producto)

  def modificar_producto(self, nombre_producto):
    temp = self.productos.contains(nombre_producto)
    if temp is not None:
      print("1. Precio\n2. Cantidad\n3. Unidad\n")
      opcion = int(input("Ingrese la opcion: "))
      if opcion == 1:
        precio = float(input("Ingrese el nuevo precio: "))
        temp.product.precio = precio
      elif opcion == 2:
        cantidad = int(input("Ingrese la nueva cantidad: "))
        temp.product.cantidad = cantidad
      elif opcion == 3:
        unidad = input("Ingrese la nueva unidad: ")
        temp.product.unidad = unidad
      else:
        print("Opción inválida")
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")
      return False

  def marcar_comprado(self, nombre_producto):
    temp = self.productos.contains(nombre_producto)
    if temp is not None:
      temp.product.comprado = True
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")
      return False

  def filtrar_categoria(self, categoria): 

    def inorder_traversal(node):
      if node is not None:
        inorder_traversal(node.left)
        producto = node.product
        if producto.categoria == categoria:
          print("Productos en la categoría ", categoria)
          print("Nombre: ", producto.nombre,"\n")
        inorder_traversal(node.right)
    inorder_traversal(self.productos.root)


  def buscar_producto(self, nombre_producto):
    temp = self.productos.contains(nombre_producto)
    if temp is not None:
      print(f"Producto: {temp.product.nombre}")
      print(f"Precio: {temp.product.precio}")
      print(f"Unidad: {temp.product.unidad}")
      print(f"Cantidad: {temp.product.cantidad}")
      print(f"Categoría: {temp.product.categoria}")
      print(f"Comprado: {'Sí' if temp.product.comprado else 'No'}")
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")


  def mostrar_lista(self): #No se por que no imprime
    def inorder_traversal(node):
      if node is not None:
        inorder_traversal(node.left)
        producto = node.product
        if producto.comprado is True:
          print("Productos tachados de la lista:")
          print("Nombre:", producto.nombre,"\n")
        inorder_traversal(node.right)

    inorder_traversal(self.productos.root)



  def guardar_productos_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    productos_data = []

    def inorder_traversal(node):
      if node is not None:
        inorder_traversal(node.left)
        producto = node.product
        producto_data = {
            "nombre": producto.nombre,
            "precio": producto.precio,
            "unidad": producto.unidad,
            "cantidad": producto.cantidad,
            "categoria": producto.categoria}
        productos_data.append(producto_data)
        inorder_traversal(node.right)

    inorder_traversal(self.productos.root)

    with open(file_name, 'w') as archivo_json:
      json.dump(productos_data, archivo_json)

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
    product_strings = []

    def inorder_traversal(node):
      if node is not None:
        inorder_traversal(node.left)
        producto = node.product
        product_strings.append(f"{producto.cantidad} {producto.unidad}s de {producto.nombre} | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad} | Comprado: {'Sí' if producto.comprado else 'No'} | Categoría: {producto.categoria}")
        inorder_traversal(node.right)

    inorder_traversal(self.productos.root)

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