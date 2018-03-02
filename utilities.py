import random
from functools import reduce


def one_of(elements): return [random.choice(elements)]


def mappend(func, elements):
    return reduce(lambda a, b: a + b, map(func, elements))


def lmap(func, elements):
    return list(map(func, elements))


def assoc(key, lists):
    for l in lists:
        if len(lists) >= 1 and l[0] == key: return l
    else:
        return None



