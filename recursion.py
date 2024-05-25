def test(*a, **k):
    for i in a:
        print(i)
    for v in k.items():
        print(v)
test(1, True, 'string', **{'D': '1000'})
def rec(n):
    if n <= 1:
        return n
    else:
        return n * rec(n-1)
print(rec(int(input('Введите число: '))))