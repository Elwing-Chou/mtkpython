# 字典: dic 操作:[欄位]
# 函式: test 操作:(3.14)
def test(n):
    return round(n, 3)

print(type(test))

b = test
print(b(3.14))

def test2():
    return test
print(test2()(3.1412342))

class Person:
    def __init__(self, h, w):
        self.h = h
        self.w = w
print(type(Person))
b = Person
p1 = b(175, 75)
print(p1.h)