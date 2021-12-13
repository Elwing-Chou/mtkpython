class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return "{}/{}".format(self.height, self.weight)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.weight == other.weight

p1 = Person("Elwing", 175, 75)
print(p1.bmi())
print(Person.bmi(p1))
# str(p1) -> p1.__str__()
print(p1)
# repr(p1) -> p1.__repr__()
print([p1])
p2 = Person("Bob", 180, 80)
# p1.__eq__(p2)
print(p1 == p2)

class SuperPerson(Person):
    def __init__(self, name, height, weight, city):
        Person.__init__(self, name, height, weight)
        self.city = city

    def __str__(self):
        return "{}/{}".format(Person.__str__(self), self.city)

s1 = SuperPerson("Elwing", 180, 80, "Taipei")
print(s1)
print([s1])