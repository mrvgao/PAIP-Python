# -----------------
# User Instructions
#
# In this problem you will be refactoring the bsuccessors function.
# Your new function, bsuccessors3, will take a state as an input
# and return a dict of {state:action} pairs.
#
# A state is a (here, there, light) tuple. Here and there are
# frozensets of people (each person is represented by an integer
# which corresponds to their travel time), and light is 0 if
# it is on the `here` side and 1 if it is on the `there` side.
#
# An action is a tuple of (travelers, arrow), where the arrow is
# '->' or '<-'. See the test() function below for some examples
# of what your function's input and output should look like.

import operator as op


def bsuccessors3(state):
    """Return a dict of {state:action} pairs.  State is (here, there, light)
    where here and there are frozen sets of people, light is 0 if the light is
    on the here side and 1 if it is on the there side.
    Action is a tuple (travelers, arrow) where arrow is '->' or '<-'"""
    _, _, light = state
    here_op, there_op, action = (op.sub, op.or_, '->') if light == 0 else (op.or_, op.sub, '<-')

    return {(here_op(state[0], frozenset([a, b])), there_op(state[1], frozenset([a, b])), 1-light): (set([a, b]), action)
            for a in state[light]
            for b in state[light]}


def test():
    b = bsuccessors3((frozenset([1]), frozenset([]), 0))
    assert b == {
        (frozenset(), frozenset({1}), 1): ({1}, '->')}, b

    assert bsuccessors3((frozenset([1, 2]), frozenset([]), 0)) == {
        (frozenset({1}), frozenset({2}), 1): ({2}, '->'),
        (frozenset(), frozenset({1, 2}), 1): ({1, 2}, '->'),
        (frozenset({2}), frozenset({1}), 1): ({1}, '->')}

    assert bsuccessors3((frozenset([2, 4]), frozenset([3, 5]), 1)) == {
        (frozenset({2, 4, 5}), frozenset({3}), 0): ({5}, '<-'),
        (frozenset({2, 3, 4, 5}), frozenset({}), 0): ({3, 5}, '<-'),
        (frozenset({2, 3, 4}), frozenset({5}), 0): ({3}, '<-')}
    return 'tests pass'


print(test())