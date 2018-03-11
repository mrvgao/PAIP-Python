# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.
import itertools


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state

    light = 'light'
    have_light_side = here if light in here else there
    target_side = there if light in here else here
    direction = '->' if light in here else '<-'

    persons = list(have_light_side.difference({light}))

    successor = {}

    all_possible_combinations = itertools.combinations(persons, 2) if len(persons) >= 2 else [(persons[0], persons[0])]

    for p1, p2 in all_possible_combinations:
        light_time = max(p1, p2)

        move_elements = {p1, p2, light}

        have_light_side = frozenset(set(have_light_side) - move_elements)
        target_side = frozenset(set(target_side) | move_elements)

        action = (p1, p2, direction)

        here = have_light_side if direction == '->' else target_side
        there = target_side if direction == '->' else have_light_side

        successor[(here, there, t + light_time)] = action

    return successor
    # your code here


def test():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
        (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
        (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    return 'tests pass'


print(test())