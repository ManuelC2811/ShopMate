import json

from dataStructures.Hash import HashTable
from model.Product2 import Product
from model.ShoppingListInterface import ShoppingListInterface
from model.User import User


class ShoppingList(ShoppingListInterface):
  def __init__(self, name, username):
    self.name = name
    self.username = username
    self.productos = HashTable()
    self.cargar_productos_desde_json()

  def añadir_producto(self, nombre, precio, unidad, cantidad, categoria):
    producto = Product(precio, unidad, cantidad, categoria)
    self.productos.set_item(nombre, producto)

  def eliminar_producto(self, nombre_producto):
    return self.productos.remove_item(nombre_producto)

  def modificar_producto(self, nombre_producto):
    temp = self.productos.get_item(nombre_producto)
    if temp is not None:
      print("1. Precio\n2. Cantidad\n3. Unidad\n")
      opcion = int(input("Ingrese la opcion: "))
      if opcion == 1:
        precio = float(input("Ingrese el nuevo precio: "))
        temp.precio = precio
      elif opcion == 2:
        cantidad = int(input("Ingrese la nueva cantidad: "))
        temp.cantidad = cantidad
      elif opcion == 3:
        unidad = input("Ingrese la nueva unidad: ")
        temp.unidad = unidad
      else:
        print("Opción inválida")
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")
      return False

  def marcar_comprado(self, nombre_producto):
    temp = self.productos.get_item(nombre_producto)
    if temp is not None:
      temp.comprado = True
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")
      return False

  def filtrar_categoria(self, categoria): 
     all_keys = []
     for i in range(len(self.productos.data_map)):
       if self.productos.data_map[i] is not None:
         for j in range(len(self.productos.data_map[i])):
           if self.productos.data_map[i][j][1].categoria == categoria:
             all_keys.append(self.productos.data_map[i][j][0])    
     print(*all_keys,"\n")


  def buscar_producto(self, nombre_producto):
    temp = self.productos.get_item(nombre_producto)
    if temp is not None:
      print(f"Producto: {nombre_producto}")
      print(f"Precio: {temp.precio}")
      print(f"Unidad: {temp.unidad}")
      print(f"Cantidad: {temp.cantidad}")
      print(f"Categoría: {temp.categoria}")
      print(f"Comprado: {'Sí' if temp.comprado else 'No'}")
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")


  def mostrar_lista(self): #No se por que no imprime
    all_keys = []
    for i in range(len(self.productos.data_map)):
      if self.productos.data_map[i] is not None:
        for j in range(len(self.productos.data_map[i])):
          if self.productos.data_map[i][j][1].comprado is True:
            all_keys.append(self.productos.data_map[i][j][0])    
    print(*all_keys,"\n")
    


  def guardar_productos_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    productos_data = []
    
    for i in range(len(self.productos.data_map)):
      if self.productos.data_map[i] is not None:
        for j in range(len(self.productos.data_map[i])):
          nombre_producto = self.productos.data_map[i][j][0]
          producto = self.productos.data_map[i][j][1]
          producto_data = {
              "nombre": nombre_producto,
              "precio": producto.precio,
              "unidad": producto.unidad,
              "cantidad": producto.cantidad,
              "categoria": producto.categoria}
          productos_data.append(producto_data)

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

    for i in range(len(self.productos.data_map)):
      if self.productos.data_map[i] is not None:
        for j in range(len(self.productos.data_map[i])):
          nombre_producto = self.productos.data_map[i][j][0]
          producto = self.productos.data_map[i][j][1]
          
          product_strings.append(f"{producto.cantidad} {producto.unidad}s de {nombre_producto} | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad} | Comprado: {'Sí' if producto.comprado else 'No'} | Categoría: {producto.categoria}")      

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