nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

flatten = lambda x: [item for nested_list in x for item in nested_list]

for i in flatten(nested_list):
    print(i)
