# https://docs.python.org/zh-tw/3/reference/datamodel.html#object.__init__
class Person:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return str(self.bmi())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.height - self.weight) == (other.height - other.weight)

p1 = Person(80, 175)
print(p1.height)
print(p1.bmi())
# str(p1), p1.__str__()
print(p1)
# repr(p1)
print([p1])
p2 = Person(60, 155)
# p1.__eq__(p2)
print(p1 == p2)