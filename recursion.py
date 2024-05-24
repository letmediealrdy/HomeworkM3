def test(a = 1, b = True):
    print(a, b)
test()
def rec(*n):
    for i in n:
        if i <= 1:
            return i
        else:
            return i * rec(i-1)
print(rec(int(input('Введите число: '))))