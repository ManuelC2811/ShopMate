import csv


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.shopping_lists = []
      
    def save_data(self):
        user_data = [self.username, self.password]
        with open('resources/users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(user_data)
      
    def validar(self):
        with open("resources/users.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                us, psw = row
                if self.username == us and self.password == psw:
                    return True
        return False
