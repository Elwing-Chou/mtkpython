# https://docs.python.org/3/reference/datamodel.html#object.__init__
class Person:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return "{}/{}".format(self.height, self.weight)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.height == other.height and self.weight == other.weight

p1 = Person(175, 75)
print(p1.bmi())
# str(p1) -> p1.__str__()
print(p1)
# repr(p1) -> p1.__repr__()
print([p1])
p2 = Person(175, 75)
# p1.__eq__(p2)
print(p1 == p2)


class SuperPerson(Person):
    def __init__(self, h, w, c):
        Person.__init__(self, h, w)
        self.city = c

    def __str__(self):
        return "{}/{}".format(Person.__str__(self), self.city)

p3 = SuperPerson(180, 80, "Taipei")
print(p3.bmi(), Person.bmi(p3))
print(p3)