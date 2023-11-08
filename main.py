#from controller.ShoppingListController import ShoppingListController
#from controller.BST_Controller import ShoppingListController
from controller.BST_Controller import ShoppingListController
from controller.UserController import UserController
from view.View import View

sc = View()

while True:
    sc.welcome()
    sc.displaymainMenu()
    option = int(input("\nIngrese una opción: "))

    if option == 1:
        u = UserController()
        user = u.login()
        if user:
            s = ShoppingListController(user)
            s.controller()
        else:
            print("Error")

    elif option == 2:
        u = UserController()
        user = u.crear_cuenta()

    elif option == 3:
      break

    else:
        print("Opción inválida")