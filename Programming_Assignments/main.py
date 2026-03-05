# main.py

from water_jug import get_initial_state, is_goal, get_next_states
from search import bfs, dfs


def print_result(name, result):
    path, nodes, time_taken = result

    print(f"\n{name} RESULT:")
    print("Path to goal:")
    for state in path:
        print(state)

    print("Nodes explored:", nodes)
    print("Time taken:", time_taken)


def main():
    initial_state = get_initial_state()

    bfs_result = bfs(initial_state, is_goal, get_next_states)
    print_result("BFS", bfs_result)

    dfs_result = dfs(initial_state, is_goal, get_next_states)
    print_result("DFS", dfs_result)


if __name__ == "__main__":
    main()
