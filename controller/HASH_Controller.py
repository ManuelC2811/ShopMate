import csv

#from model.ShoppingList import ShoppingList
from model.ShoppingListHash import ShoppingList
from model.User import User
from view.View import View


class ShoppingListController:
  def __init__(self, user):
    self.user = user
    self.shopping_lists = self.load_shopping_lists_from_csv()

  def create_shopping_list(self):
    nombre = input("\nNombre de tu lista: ")
    shop_list = ShoppingList(nombre, self.user.username)
    self.shopping_lists.append(shop_list)
    self.user.shopping_lists.append(shop_list)
    self.save_list(nombre, self.user.username)
    print("\nLista de compras creada con éxito")
    print("")

  def add_product_to_list(self, shopping_list):
    while True:
      producto = input('\033[1m' + '¿Que producto deseas añadir?: ' +'\033[0m').strip()
      if producto.lower() == "fin":
        break
      precio = int(input('\033[1m' + 'Ingresa el precio: ' + '\033[0m'))
      unidad = input('\033[1m' + 'Ingresa la unidad: ' + '\033[0m')
      cantidad = int(input('\033[1m' + 'Ingresa la cantidad: ' + '\033[0m'))
      categoria = input('\033[1m' + 'Ingresa la categoria: ' + '\033[0m')
      shopping_list.añadir_producto(producto, precio, unidad, cantidad, categoria)
      shopping_list.guardar_productos_json()

  def delete_product(self, shopping_list):
    producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    shopping_list.eliminar_producto(producto_a_eliminar)
    shopping_list.guardar_productos_json()

  def update_product(self,shopping_list):
    producto_a_modificar = input("Ingrese el nombre de producto que desea modificar: ")
    if shopping_list.modificar_producto(producto_a_modificar) is not False:
      print(f"{producto_a_modificar} ha sido modificado")
      shopping_list.guardar_productos_json()

  def mark_purchased(self, shopping_list):
    nombre_producto = input("Ingrese el nombre del producto a marcar como comprado: ")
    if shopping_list.marcar_comprado(nombre_producto) is not False:
      print("")
      print(f"{nombre_producto} se tachó de la lista")
      print("")
      shopping_list.mostrar_lista()
    #shopping_list.guardar_productos_json()

  def filter_cat(self, shopping_list):
    categoria = input("Ingrese la categoria: ")
    print("")
    shopping_list.filtrar_categoria(categoria)


  def find_product(self, shopping_list):
    nombre_producto = input("¿Que producto quieres buscar?: ")
    print("")
    shopping_list.buscar_producto(nombre_producto)

  def load_shopping_lists_from_csv(self):
    shopping_lists = []
    try:
      with open('resources/listas_compras.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
          name, username = row
          if username == self.user.username:
            new_list = ShoppingList(name, self.user.username)
            shopping_lists.append(new_list)
    except FileNotFoundError:
      print("El archivo de listas de compras no existe.")
    return shopping_lists

  def display_shopping_lists(self):
    print("Listas de Compras Disponibles:")
    for i, lista in enumerate(self.shopping_lists, 1):
      print(f"{i}. {lista.name}")

  def save_list(self, nombre_lista, nombre_usuario):
    with open('resources/listas_compras.csv', mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([nombre_lista, nombre_usuario])

  def controller(self):
    while True:
      print("")
      sc = View()
      sc.userMenu()
      op = int(input("\nSeleccione una opción: "))
      print("")
      if op == 1:
        self.create_shopping_list()
      elif op == 2:
        self.display_shopping_lists()
        index = int(input("\nSeleccione una lista de compras: "))
        selected_list = self.shopping_lists[index - 1]
        while True:
          sc.listMenu()
          op = int(input("\nSeleccione una opción: "))
          print("")
          if op == 1:
            print(selected_list)
          elif op == 2:
            self.add_product_to_list(selected_list)
            print("")
            print(selected_list)
            print("")
          elif op == 3:
            print(selected_list)
            print("")
            self.delete_product(selected_list)
            print(selected_list)
            print("")
          elif op == 4:
            print(selected_list)
            print("")
            self.update_product(selected_list)
            print("")
            print(selected_list)
            print("")
          elif op == 5:
            print(selected_list)
            print("")
            self.mark_purchased(selected_list)
          elif op == 6:
            sc = View()
            sc.filterMenu()
            op = int(input("\nSeleccione una opción: "))
            print("")
            if op == 1:
              self.filter_cat(selected_list)
          elif op == 7:
            self.find_product(selected_list)
            print("")
          elif op == 8:
            break
      else:
        print("\n" + '\033[1m' + 'Gracias por usar ShopMate, Hasta luego! ' + '\033[0m')
        break