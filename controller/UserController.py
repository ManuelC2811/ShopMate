from model.ShoppingList import ShoppingList
from model.User import User
from view.View import View


class UserController:
  def __init__(self):
    self.view = View()

  def crear_cuenta(self):
    username = self.view.askUsername()
    password = self.view.askPassword()
    user = User(username, password)
    user.save_data()
    print("\nCuenta creada con exito")
    return user
    
  def login(self):
    self.view.login()
    username = self.view.askUsername()
    password = self.view.askPassword()
    user = User(username, password)
    if user.validar():
        print("")
        print('\033[1m' + 'Bienvenido' + '\033[0m')
        return user
    print('\033[1m' + 'Datos incorrectos' + '\033[0m')
    return False