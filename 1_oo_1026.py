# https://docs.python.org/3/reference/datamodel.html#object.__init__
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return "{}: {}".format(self.name, self.bmi())

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return (self.bmi() + other.bmi()) / 2

class SuperPerson(Person):
    def __init__(self, name, height, weight, city):
        Person.__init__(self, name, height, weight)
        self.city = city


p1 = Person("Elwing", 175, 75)
print(p1.bmi())
print(Person.bmi(p1))
# print(p1) -> str(p1) -> p1.__str__()
print(p1)

p2 = SuperPerson("Bob", 180, 80, "Taipei")
print(p2.bmi())
# repr(p1) -> p1.__repr__()
print([p1, p2])

# p1.__add__(p2)
print(p1 + p2)