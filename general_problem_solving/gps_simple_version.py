"""
General Problem Solver.
"""

from collections import namedtuple
from itertools import product


def make_op(action, preconditions, add_list, del_list):
    operator = namedtuple('op', ['action', 'preconditions', 'add_list', 'del_list'])
    return operator(action, set(preconditions), set(add_list), set(del_list))


def gps(current_state, goal_state, operators):
    def achieve():
        return any([g in current_state for g in goal_state])

    def is_appropriate(op, goal_states):
        return any([g in op.add_list for g in goal_states])

    def apply_op(op, states):
        if states in op.preconditions:
            new_states = states - op.del_list
            new_states = new_states + op.add_list
            return new_states
        else:
            return False

    if not achieve():
        for op in operators:
            if is_appropriate(op, goal_state):
                pass
        for op, goal in product(operators, goal_state):
            if is_appropriate(op, goal):
                return [gps(current_state, op.preconditions, operators)] + [op.action]
    else:
        return True


school_operators = [
    make_op('drive-son-to-school',
            ['son-at-home', 'car-works'],
            ['son-at-school'],
            ['son-at-home']),
    make_op('shop-installs-battery',
            ['car-needs-battery', 'shop-know-problem', 'shop-has-money'],
            ['car-works'],
            []),
    make_op('tell-shop-problem',
            ['in-communication-with-shop'],
            ['shop-knows-problem'],
            []),
    make_op('telephone-shop',
            ['know-phone-number'],
            ['in-communication-with-shop'],
            []),
    make_op('look-up-number',
            ['have-phone-book'],
            ['know-phone-number'],
            []),
    make_op('give-shop-money',
            ['have-money'],
            ['shop-has-money'],
            ['have-money']),
]

print(gps(
    {'son-at-home', 'car-needs-battery', 'have-money', 'have-phone-book'},
    {'son-at-school'},
    operators=school_operators
))
