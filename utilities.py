import random
from functools import reduce
import jieba


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


def every(cond, iterables):
    return all(cond(e) for e in iterables)


def assoc(var, alist):
    for a in alist:
        try:
            if a[0] == var: return a
        except TypeError as e:
            pass
        except IndexError as e:
            pass
    return None


concat = ''.join


def is_tokens(p_tokens):
    return isinstance(p_tokens, list) and len(p_tokens) > 0


def is_atom(element): return isinstance(element, str)


def is_variable(element): return len(element) > 0 and element[0] == '?' and is_atom(element)


def is_segment_pattern(pattern):
    return is_tokens(pattern) and pattern[0].startswith('?*')


def merge_variable(split_tokens):
    results = []
    i = 0
    single_len, pattern_len = 2, 3
    while i <= len(split_tokens)-single_len:
        forward1 = concat(split_tokens[i:i+single_len])
        forward2 = concat(split_tokens[i:i+pattern_len])

        if is_segment_pattern([forward2]):
            results.append(forward2)
            i += pattern_len
        elif is_variable(forward1):
            results.append(forward1)
            i += single_len
        else:
            results.append(split_tokens[i])
            i += 1

    if i == len(split_tokens) - 1:
        results.append(split_tokens[-1])

    return results


def cut(string):
    return merge_variable(list(jieba.cut(string)))


def check_var_val(var, var_value=None, global_=True):
    if isinstance(var, str):
        print('{} ::=> {}'.format(var, var_value))
    else:
        scope = globals if global_ else locals
        k_v = first_if(list(scope().items()), lambda k_v: k_v[1] is var)
        format_result = '{} ::=> {}'.format(k_v[0], var) if k_v else None
        print(format_result)
        return format_result


if __name__ == '__main__':
    assert assoc(1, [(1, 1), (2, 2)]) == (1, 1)
    assert assoc(3, [(1, 1), (2, 2)]) is None
    assert every(lambda x: x > 0, [1, 2, 3])
    var_ = 'some var'
    assert check_var_val(var_) == 'var_ ::=> some var', check_var_val(var_)
    var_3 = var_[:3]
    assert check_var_val(var_3) == 'var_3 ::=> som'

    def some_fun(var):
        v = 1
        assert check_var_val(v) is None
        assert check_var_val(var) is None
        assert check_var_val(v, global_=False) is not None
        assert check_var_val(var, global_=False) is not None

    some_fun(0)

    print('test done!')
