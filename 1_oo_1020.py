# https://docs.python.org/3/reference/datamodel.html#object.__init__
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return "{}:{:.2f}".format(self.name, self.bmi())

    def __repr__(self):
        return "{}...".format(self)

    def __eq__(self, other):
        return self.height == other.height

class SuperPerson(Person):
    def __init__(self, name, height, weight, city):
        Person.__init__(self, name, height, weight)
        self.city = city

    def __str__(self):
        return "{}[{}]".format(Person.__str__(self),
                               self.city)


p1 = SuperPerson("Elwing", 175, 75, "Taipei")
print(p1.bmi(), Person.bmi(p1))
# print -> str(p1) -> p1.__str__()
print(p1)
p2 = Person("Bob", 175, 80)
# p1.__repr__()
print([p1, p2])
# p1 == p2 -> p1.__eq__(p2)
print(p1 == p2)