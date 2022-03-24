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


class Student(Person):

    def __init__(self, weight, height, name):
        Person.__init__(self, weight, height)
        self.name = name

    def study(self):
        self.weight = self.weight - 5

    def __str__(self):
        # self.__str__()
        return "{}:{}".format(self.name, Person.__str__(self))

s1 = Student(80, 175, "Elwing")
print(s1.bmi())
s1.study()
Student.study(s1)
print(s1.bmi())
print(s1)