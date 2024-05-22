def test(a = 1, b = True):
    print(a, b)
test()
def rec(n):
    if n <= 1:
        return n
    else:
        return n * rec(n-1)
print(rec(int(input('Введите число: '))))