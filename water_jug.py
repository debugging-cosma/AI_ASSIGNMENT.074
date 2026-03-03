# water_jug.py

JUG1_CAPACITY = 4
JUG2_CAPACITY = 3
GOAL = 2   # want 2 litres in any jug


def get_initial_state():
    return (0, 0)


def is_goal(state):
    return state[0] == GOAL or state[1] == GOAL


def get_next_states(state):
    x, y = state
    next_states = []

    # Fill jug1
    next_states.append((JUG1_CAPACITY, y))

    # Fill jug2
    next_states.append((x, JUG2_CAPACITY))

    # Empty jug1
    next_states.append((0, y))

    # Empty jug2
    next_states.append((x, 0))

    # Pour jug1 -> jug2
    transfer = min(x, JUG2_CAPACITY - y)
    next_states.append((x - transfer, y + transfer))

    # Pour jug2 -> jug1
    transfer = min(y, JUG1_CAPACITY - x)
    next_states.append((x + transfer, y - transfer))

    return next_states