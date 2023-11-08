import json

from dataStructures.AVL import AVLTree
from model.Product import Product
from model.ShoppingListInterface import ShoppingListInterface
from model.User import User


class ShoppingListAVL(ShoppingListInterface):

  def __init__(self, name, username):
    self.name = name
    self.username = username
    self.avl_tree = AVLTree()
    self.cargar_productos_desde_json()

  def añadir_producto(self, nombre, precio, unidad, cantidad, categoria):
    producto = Product(nombre, precio, unidad, cantidad, categoria)
    self.avl_tree.insert_product(producto)

  def eliminar_producto(self, nombre_producto):
    self.avl_tree.delete_product(nombre_producto)

  def buscar_producto(self, nombre_producto):
    producto_nodo = self.avl_tree.search_product(nombre_producto)
    if producto_nodo:
      producto = producto_nodo.product
      print(f"Producto: {producto.nombre}")
      print(f"Precio: {producto.precio}")
      print(f"Unidad: {producto.unidad}")
      print(f"Cantidad: {producto.cantidad}")
      print(f"Categoría: {producto.categoria}")
    else:
      print(f"{nombre_producto} no se encontró en la lista de compras.")

  def modificar_producto(self, nombre_producto):
    pass

  def marcar_comprado(self, nombre_producto):
    pass

  def filtrar_categoria(self, categoria):
    pass

  def guardar_productos_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    productos_data = []

    # Función recursiva para recorrer el árbol en orden y recopilar los datos
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.left)
            producto = node.product
            producto_data = {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "unidad": producto.unidad,
                "cantidad": producto.cantidad,
                "categoria": producto.categoria
            }
            productos_data.append(producto_data)
            inorder_traversal(node.right)

    # Llamar a la función de recorrido inorden en la raíz del árbol
    inorder_traversal(self.avl_tree.root)

    with open(file_name, 'w') as archivo_json:
        json.dump(productos_data, archivo_json)


  def cargar_productos_desde_json(self):
    file_name = f"resources/productos_{self.username}_{self.name}.json"
    try:
      with open(file_name, 'r') as archivo_json:
        productos_data = json.load(archivo_json)

      for producto_data in productos_data:
        nombre = producto_data["nombre"]
        precio = producto_data["precio"]
        unidad = producto_data["unidad"]
        cantidad = producto_data["cantidad"]
        categoria = producto_data["categoria"]
        producto = Product(nombre, precio, unidad, cantidad, categoria)
        self.avl_tree.insert_product(producto)

    except FileNotFoundError:
      pass


  def __str__(self):
    product_strings = []

    # Función recursiva para recorrer el árbol en orden e incluir la descripción de cada producto
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.left)
            producto = node.product
            product_strings.append(
                f"{producto.cantidad} {producto.unidad}s de {producto.nombre} | Precio: {producto.precio} c/u | Total: {producto.precio * producto.cantidad}"
            )
            inorder_traversal(node.right)

    # Llamar a la función de recorrido inorden en la raíz del árbol
    inorder_traversal(self.avl_tree.root)

    product_list = "\n".join(product_strings)
    return f'\033[1mTu Lista de Compras:\033[0m {self.name}\n\033[1mProductos:\033[0m\n{product_list}'


  #para test
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