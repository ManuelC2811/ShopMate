class View():
  
  def welcome(self):
    print("")
    print('\033[1;4m'+ "BIENVENIDO A SHOP MATE" + '\033[0m')

  def login(self):
    print("")
    print('\033[1;4m'+ "INICIAR SESIÓN" + '\033[0m')

  def displaymainMenu(self):
    print("")
    print("1. Iniciar sesión")
    print("2. Crear una cuenta")
    print("3. Cerrar")

  def userMenu(self):
    print("1. Crear lista de compra")
    print("2. Mis listas")
    print("3. Papelera")
    print("4. Cerrar sesion")

  def listMenu(self):
    print("Opciones: \n")
    print("1) Ver lista                         2) Añadir producto")
    print("3) Eliminar producto                 4) Modificar producto")
    print("5) Marcar producto como comprado     6) Filtrar")
    print("7) Buscar producto                   8) Volver\n")

  def filterMenu(self):
    print("¿Como desea filtrar?: ")
    print("")
    print("1) Categoria         2) Establecimiento de compra")
    print("3) Volver\n")
    
  def askUsername(self):
    username = input('Ingrese el usuario: ')
    return username
    
  def askPassword(self):
    password = input("Ingrese la contraseña: ")
    return password