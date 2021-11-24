nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def generator(a):
    flatten = lambda x: [item for nested_list in x for item in nested_list]
    yield flatten


for item in generator(nested_list):
    print(item)
