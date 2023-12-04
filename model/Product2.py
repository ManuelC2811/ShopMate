class Product:
  def __init__(self, precio, unidad, cantidad, categoria):
    self.precio = precio
    self.unidad = unidad
    self.cantidad = cantidad
    self.categoria = categoria
    self.comprado = False

  def __str__(self):
    return f"{self.cantidad} {self.nombre} a ${self.precio} cada uno"
