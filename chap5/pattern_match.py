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


fail = [True, None]


def pattern_match_l(pattern, input, bindings=None):
    bindings = bindings or defaultdict(lambda : None)
    if bindings == fail: return None
    elif is_variable(pattern):
        return match_variable(pattern, input, bindings)
    elif is_atom(pattern):
        if pattern == input: return bindings
        else: return fail
    elif is_tokens(pattern) and is_tokens(input):
        peak_p, peak_input = pattern[0], input[0] if len(pattern) > 1 else ' '.join(input[0:])
        return pattern_match_l(pattern[1:], input[1:],
                               bindings=pattern_match_l(peak_p, peak_input, bindings=bindings)
                )
    else:
        return bindings


def is_tokens(p_tokens):
    return isinstance(p_tokens, list) and len(p_tokens) > 0


def match_variable(var, input, bindings):
    if bindings[var] is None:
        bindings[var] = input
    elif bindings[var] != input:
        bindings = fail
    return bindings


def sub_list(variable_subsitude, words):
    variable, subsitude = variable_subsitude
    return [w if w != variable else subsitude for w in words]


def get_bindings_pair(bindings_dict):
    return bindings_dict.items()


assert pattern_match(test_pattern.split(), test_input.split())
assert not pattern_match(test_pattern.split(), test_n_input.split())
assert pattern_match_l('I need a ?X a really ?X'.split(), 'I need a vacation a really trip'.split()) is None
assert pattern_match_l('I need a ?X a really ?X'.split(), 'I need a vacation a really ?X'.split()) is None
assert dict(pattern_match_l('I need a ?X a really ?X'.split(), 'I need a vacation a really vacation'.split())) == {'?X': 'vacation'}
assert pattern_match_l('?X a really ?X'.split(), 'vacation a really ?X'.split()) is None
assert ' '.join(sub_list(
    *get_bindings_pair(
        pattern_match_l('I need a ?X a really ?X'.split(),
                        'I need a vacation a really vacation'.split())),
    'what would it mean to you if you got a ?X ?'.split())) == \
    'what would it mean to you if you got a vacation ?'

assert dict(pattern_match_l('?X is ?X'.split(), '2 is 2'.split())) == {'?X': '2'}
assert pattern_match_l('?X is ?X'.split(), '2 + 2 is 4'.split()) is None
assert pattern_match_l(['?X', 'is', '?X'], ['2 + 2', 'is', '4']) is None
assert dict(pattern_match_l(['?X', 'is', '?X'], ['2 + 2', 'is', '2 + 2'])) == {'?X': '2 + 2'}

r = pattern_match_l(['?P', 'need', '?X'], ['I', 'need', 'a', 'long', 'trip'])
assert dict(r) == {'?P': 'I', '?X': 'a long trip'}, dict(r)
print('test done!')

