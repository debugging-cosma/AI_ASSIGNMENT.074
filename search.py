# search.py

from collections import deque
import time


def bfs(initial_state, is_goal, get_next_states):
    start_time = time.time()

    queue = deque()
    queue.append((initial_state, [initial_state]))

    visited = set()
    nodes_explored = 0

    while queue:
        state, path = queue.popleft()
        nodes_explored += 1

        if is_goal(state):
            end_time = time.time()
            return path, nodes_explored, end_time - start_time

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None, nodes_explored, time.time() - start_time


def dfs(initial_state, is_goal, get_next_states):
    start_time = time.time()

    stack = []
    stack.append((initial_state, [initial_state]))

    visited = set()
    nodes_explored = 0

    while stack:
        state, path = stack.pop()
        nodes_explored += 1

        if is_goal(state):
            end_time = time.time()
            return path, nodes_explored, end_time - start_time

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))

    return None, nodes_explored, time.time() - start_time