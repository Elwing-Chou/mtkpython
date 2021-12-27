def test():
    return 3
# 型態: dic, 操作: []
# print(3)
# 型態: print 操作: (3)

b = test
print(b())

def test2():
    return test
print(test2()())

test2.height = 175
test2.func = test
print(test2.func())

class Person:
    pass

print(type(Person))
b = Person
p1 = b()