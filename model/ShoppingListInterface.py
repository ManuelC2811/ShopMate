from abc import ABC, abstractmethod


class ShoppingListInterface(ABC):
    @abstractmethod
    def añadir_producto(self, nombre, precio, unidad, cantidad):
        pass

    @abstractmethod
    def eliminar_producto(self, nombre_producto):
        pass

    @abstractmethod
    def modificar_producto(self, nombre_producto):
        pass

    @abstractmethod
    def marcar_comprado(self, nombre_producto):
      pass

    @abstractmethod
    def buscar_producto(self, nombre_producto):
      pass

    @abstractmethod
    def filtrar_categoria(self, categoria):
      pass
  
    @abstractmethod
    def guardar_productos_json(self):
        pass

    @abstractmethod
    def __str__(self):
        pass