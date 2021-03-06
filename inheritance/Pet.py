class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'Name: {self.name} Age: {self.age}')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f'{self.name} is saying meow')

    def show(self):
        print(f'Name: {self.name} Age: {self.age} Color: {self.color}')


class Dog(Pet):
    def speak(self):
        print(f'{self.name} is saying woof')


p = Pet('Puppy', 3)
p.show_info()

c = Cat('Kitty', 1, 'White')
c.speak()
c.show()

d = Dog('Doggy', 2)
d.show_info()
d.speak()
