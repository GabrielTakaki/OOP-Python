class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


my_user = User('Gabriel', 'gabriel@gmail.com', '12345')
print(my_user.name)
print(my_user.email)
print(my_user.password)
