class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        ans = self.weight / (self.height / 100) ** 2
        return ans

    def __str__(self):
        s = "[Name]{} [BMI]{}".format(self.name, self.bmi())
        return s

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.height == other.height

class SuperPerson(Person):

    def __init__(self, name, height, weight, place):
        Person.__init__(self, name, height, weight)
        self.place = place

    def __str__(self):
        ans = ("{} [Place]{}".format(Person.__str__(self),
                                     self.place))
        return ans

p1 = Person("Elwing", 175, 75)
# str(p1) -> p1.__str__()
print(p1)
p2 = Person("Bob", 175, 80)
# repr(p1) -> p1.__repr__()
print([p1, p2])
# p1 == p2 -> p1.__eq__(p2)
print(p1 == p2)
print(p1.bmi(), Person.bmi(p1))
s1 = SuperPerson("Carol", 160, 50, "Taipei")
print(s1)