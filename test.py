import time
import unittest

#from model.ShoppingList import ShoppingList
#from model.ShoppingArray import ShoppingArray
from model.ShoppingListDoubly import ShoppingListDoubly


class test_case(unittest.TestCase):

    def setUp(self):
        self.shopping_list = ShoppingListDoubly("MiLista", "MiUsuario")

    def test_cargar_productos_desde_json(self):
        
        start_time = time.time()
        self.shopping_list.añadir_productos_desde_json("100K.json")
        self.shopping_list.guardar_productos_json()
        #self.shopping_list.modificar_producto('Producto50000')
        #self.shopping_list.buscar_producto('Producto5000000')
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tiempo de ejecución: {elapsed_time} segundos")

if __name__ == '__main__':
    unittest.main()