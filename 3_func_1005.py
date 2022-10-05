print(type(3))
# 字典 dic 操作 [key]
# 函式型態 print 操作 ("hello")
print(type(print))

b = int
print(b(5.2))

def test(n):
    if n == 0:
        return int
    else:
        return round

print(test(2)(5.21234, 3))