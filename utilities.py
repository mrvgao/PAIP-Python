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


def combine_all(xlist, ylist):
    return [[x, y] for x in xlist for y in ylist]


def first_if(array, cond):
    for a in array:
        if cond(a): return a
    else:
        return None


def cond_all(cond, iterables):
    return all(cond(e) for e in iterables)


assert cond_all(lambda x: x > 0, [1, 2, 3])
