from itertools import permutations

def possible_permutations(ls: list):

    for perm in permutations(ls):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
