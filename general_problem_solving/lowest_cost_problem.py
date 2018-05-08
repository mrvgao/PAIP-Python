# -----------------
# User Instructions
#
# Define a function, lowest_cost_search, that is similar to
# shortest_path_search, but also takes into account the cost
# of an action, as defined by the function action_cost(action)
#
# Since we are using this function as a generalized version
# of the bridge problem, all the code necessary to solve that
# problem is included below for your reference.
#
# This code will not run yet. Click submit to see if your code
# is correct.


def lowest_cost_search(start, successors, is_goal, action_cost):
    """Return the lowest cost path, starting from start state,
    and considering successors(state) => {state:action,...},
    that ends in a state for which is_goal(state) is true,
    where the cost of a path is the sum of action costs,
    which are given by action_cost(action)."""
    # your code here
    Fail = []

    if is_goal: return [start]

    explored = set()
    froniter = [ [start] ]

    while froniter:
        path = froniter.pop(0)
        state = path[-1]
        if is_goal(state): return path

        pcost = path_cost(path)
        for (state, action) in successors(state).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(froniter, path2)
    return Fail


def bsuccessors2(state):
    """Return a dict of {state:action} pairs.  A state is a (here, there) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the light."""
    here, there = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light'])),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light'])),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')


def path_cost(path):
    "The total cost of a path (which is stored in a tuple with the final action)."
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost


def bcost(action):
    "Returns the cost (a number) of an action in the bridge problem."
    # An action is an (a, b, arrow) tuple; a and b are times; arrow is a string
    a, b, arrow = action
    return max(a, b)


def add_to_frontier(frontier, path):
    "Add path to frontier, replacing costlier path if there is one."
    # (This could be done more efficiently.)
    # Find if there is an old path to the final state of this path.
    old = None
    for i, p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return  # Old path was better; do nothing
    elif old is not None:
        del frontier[old]  # Old path was worse; delete it
    ## Now add the new path and re-sort
    frontier.append(path)
    frontier.sort(key=path_cost)


## Now there is still a problem to deal with.
def bridge_problem2(here):
    Fail = []
    here = frozenset(here) | frozenset(['light'])
    explored = set()  # set of states we have visited
    # State will be a (peoplelight_here, peoplelight_there) tuple
    # E.g. ({1, 2, 5, 10, 'light'}, {})
    frontier = [[(here, frozenset())]]  # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1 = state1 = final_state(path)
        if not here1 or (len(here1) == 1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors2(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail


def final_state(path): return path[-1]

