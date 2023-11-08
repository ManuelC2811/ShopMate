import sys

sys.setrecursionlimit(100000000)
import time
import unittest

#from model.ShoppinListAVL import ShoppingListAVL
from model.ShoppingListBST import ShoppingList


class test_case(unittest.TestCase):

  def setUp(self):
    self.shopping_list = ShoppingList("MiLista", "MiUsuario")

  def test_cargar_productos_desde_json(self):
    start_time = time.time()
    self.shopping_list.añadir_productos_desde_json("10K.json")
    self.shopping_list.guardar_productos_json()
    #self.shopping_list.buscar_producto("Producto53")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo de ejecución: {elapsed_time} segundos")


if __name__ == '__main__':
  unittest.main()
