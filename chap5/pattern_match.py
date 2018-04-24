from functools import reduce
import operator as op
from utilities import assoc
from collections import defaultdict


test_pattern = 'I need a ?X'
test_input = 'I need a vacation'
test_n_input = 'I dont need a vacation'


def is_atom(element): return isinstance(element, str) and ' ' not in element


def is_variable(element): return is_atom(element) and element.startswith('?')


def pattern_match(pattern, input):
    # pattern could be a list, which is split from 'I need a X_X'
    # or pattern could be a element which is the element of a list.
    if len(pattern) == 0 and len(input) == 0: return []
    elif is_variable(pattern): return True
    elif is_atom(pattern) and is_atom(input): return pattern == input
    else:
        return all(pattern_match(p, i) for p, i in zip(pattern, input))


def get_binding_val(var, bindings):
    return bindings[var]


def extend_bindings(var, val, bindings):
    bindings[var] = val
    return bindings


def pattern_match_l_buggy(pattern, input):
    # pattern match returns a list rather than True or False
    # the problems of this are:
    # 1. the is_atom(pattern) and is_atom(input) may return True, which is not a list;
    # 2. pattern_match_l return [], which should means Failure, but not append as a list.
    # 3. We want the binding of variables to agree - if ?X is used twice in the pattern, we don't
    # 4. We don't have indicator to show that math failure;
    # 5. If the pattern.first and input.first don't match, should not go on.
    # want it to match two different values in the input.
    if len(pattern) == 0 and len(input) == 0: return []
    elif is_variable(pattern): return [pattern, input]
    elif is_atom(pattern) and is_atom(input): return pattern == input
    else:
        return pattern_match_l_buggy(pattern[0], input[0]) + pattern_match_l_buggy(pattern[1:], input[1:])


no_binding = defaultdict(lambda : None)
fail = [True, None]


def pattern_match_l(pattern, input, bindings=no_binding):
    if bindings == fail: return None
    elif is_variable(pattern):
        return match_variable(pattern, input, bindings)
    elif pattern == input:
        return bindings
    elif isinstance(pattern, list) and isinstance(input, list):
        return pattern_match_l(pattern[1:], input[1:], pattern_match_l(pattern[0], input[0]))
    else:
        return fail


def match_variable(var, input, bindings):
    binding_val = get_binding_val(var, bindings)

    if binding_val is None:
        return extend_bindings(var, input, bindings)
    elif input == binding_val:
        return bindings
    else:
        return fail


def sub_list(variable_subsitude, words):
    variable, subsitude = variable_subsitude
    return [w if w != variable else subsitude for w in words]


print(sub_list(('?X', 'vacation'),
               'what would it mean to you if you got a ?X ?'.split()))

assert pattern_match(test_pattern.split(), test_input.split())
assert not pattern_match(test_pattern.split(), test_n_input.split())
print('test done!')

print(pattern_match_l('I need a ?X a really ?X'.split(), 'I need a vacation a really trip'.split()))
print(pattern_match_l('I need a ?X a really ?X'.split(), 'I need a vacation a really ?X'.split()))
