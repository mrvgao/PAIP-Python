from utilities import every

test_pattern = 'I need a ?X'
test_input = 'I need a vacation'
test_n_input = 'I dont need a vacation'


def is_atom(element): return isinstance(element, str) and ' ' not in element


def is_variable(element): return is_atom(element) and element.startswith('?')


def pattern_match(pattern, input):
    # pattern could be a list, which is split from 'I need a X_X'
    # or pattern could be a element which is the element of a list.
    if len(pattern) == 0 and len(input) == 0: return True
    elif is_variable(pattern): return True
    elif is_atom(pattern) and is_atom(input): return pattern == input
    else:
        return all(pattern_match(p, i) for p, i in zip(pattern, input))


assert pattern_match(test_pattern.split(), test_input.split())
assert not pattern_match(test_pattern.split(), test_n_input.split())
print('test done!')

