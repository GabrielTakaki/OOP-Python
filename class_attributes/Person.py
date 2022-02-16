class Person:
    number_of_people = 0
    GRAVITY = -9.81

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_person()

    # acting on its class, not on an instance
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1



p1 = Person('João', 20)
p2 = Person('Maria', 25)
print(Person.number_of_people_())