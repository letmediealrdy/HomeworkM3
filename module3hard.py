data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

a = 0
def calculate_structure_sum(n):
    global a
    if isinstance(n, int):
        a += n
    elif isinstance(n, str):
        a += len(n)
    elif isinstance(n, list):
        for v in n:
            calculate_structure_sum(v)
    elif isinstance(n, tuple):
        for v in n:
            calculate_structure_sum(v)
    elif isinstance(n, dict):
        for v in n.items():
            calculate_structure_sum(v)
    else:
        for i in n:
            calculate_structure_sum(i)

    return a
result = calculate_structure_sum(data_structure)
print(result)