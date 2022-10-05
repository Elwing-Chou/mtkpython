# https://docs.python.org/3/reference/datamodel.html#object.__init__
class Person:
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    def bmi(self):
        ans = self.weight / (self.height / 100) ** 2
        return ans

    def __str__(self):
        return "{}/{}".format(self.height, self.weight)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.height == other.height and
                self.weight == other.weight)

p1 = Person(180, 80)
print(p1.bmi())
# str(p1) -> p1.__str__()
print(p1)
p2 = Person(180, 80)
# repr(p1) -> p1.__repr__()
print([p1, p2])
# p1 == p2 -> p1.__eq__(p2)
print(p1 == p2)