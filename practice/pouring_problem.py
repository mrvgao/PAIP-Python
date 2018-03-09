"""
There are two cups. Which have their capacities. And there is a pooling.
We set a goal. And The cups could transfer water to each other, and empty itself to pour or fill itself from pour.
We need get the solution how to get this goal.
"""


def get_successor(X, Y, x, y):
    assert (x <= X and y <= Y), (x, y)

    return {
        'X -> Y': (max(0, y + x - Y), min(Y, x + y)),
        'Y -> X': (min(X, x + y), max(0, y + x - X)),
        'X -> P': (0, y),
        'Y -> P': (x, 0),
        'P -> X': (X, y),
        'P -> Y': (x, Y),
    }


def find_goal(X, Y, goal, start=(0, 0)):
    if goal in start:
        return [start]

    pathes = [ [('init', start)] ]
    visited = set()

    while pathes:
        path = pathes.pop(0)
        frontier_action,  froniter_state = path[-1]
        x, y = froniter_state

        if froniter_state in visited: continue

        for action, state in get_successor(X, Y, x, y).items():
            p = path + [(action, state)]
            pathes.append(p)

            if goal in state: return p

        visited.add(froniter_state)

    return None


print(get_successor(9, 4, 9, 4))
solution = find_goal(123, 23, 6)

for s, c in solution:
    print(s, c)
