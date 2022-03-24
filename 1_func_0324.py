# 1. 韓式(不加括號)是型態
# 字典: dic 操作:[key]
# 函式(SOP): round 操作: (3.2)
b = round
print(b(4.23, 1))

def test(n):
    if n == 0:
        return int
    else:
        return round
print(test(0)(42.12341))

# 2. 型態可以擁有method/value
test.height = 175
print(test.height)
test.func = round
print(test.func(4.2341, 2))