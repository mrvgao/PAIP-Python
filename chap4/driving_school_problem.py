from collections import namedtuple

operator = namedtuple('operator', ['action', 'preconditions', 'add_list', 'del_list'])

school_operators = [
    operator('drive-son-to-school',
             {'son-at-home', 'car-works'},
             {'son-at-school'},
             {'son-at-home'}),
    operator('shop-installs-battery',
             {'car-needs-battery', 'shop-knows-problem', 'shop-has-money'},
             {'car-works'},
             set()),
    operator('tell-shop-problem',
             {'in-communication-with-shop'},
             {'shop-knows-problem'},
             set()),
    operator('telephone-shop',
             {'know-phone-number'},
             {'in-communication-with-shop'},
             set()),
    operator('look-up-number',
             {'have-phone-book'},
             {'know-phone-number'},
             set()),
    operator('give-shop-money',
             {'have-money'},
             {'shop-has-money'},
             {'have-money'}),
]


def apply_op(states, op):
    return states | op.add_list - op.del_list


def achieve(state, goal):
    return state.issuperset(goal)


def is_appropriate(current_state, op):
    return op.preconditions.issubset(current_state)


def get_successor(current_state, operators):
    success = {}
    for op in operators:
        if is_appropriate(current_state, op):
            success[op.action] = apply_op(current_state, op)
    return success


def gps(inital_states, goal_states, operators):
    if inital_states in goal_states:
        return [inital_states]

    pathes = [ [('init', inital_states)] ]

    visited = set()

    while pathes:
        path = pathes.pop(0)
        froniter_action, froniter_state = path[-1]

        if set(froniter_state) in visited: continue

        for action, state in get_successor(froniter_state, operators).items():
            p = path + [(action, state)]
            pathes.append(p)

            if achieve(state, goal_states): return p

        visited.add(tuple(froniter_state))

    return None


def get_solution(start_states, goal_states):
    solutions = (gps(start_states, goal_states, school_operators))
    for s in solutions:
        print(s)


# get_solution({'son-at-home', 'car-needs-battery', 'have-money', 'have-phone-book'},
#              {'son-at-school'})

get_solution({'son-at-home', 'car-needs-battery', 'have-money'},
             {'son-at-school'})


