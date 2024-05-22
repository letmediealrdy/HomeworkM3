def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1, 4, 5)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, True, 'string']
values_dict = {'a': '2', 'b': 'False', 'c': 'notString'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'text']
print_params(*values_list_2, 42)