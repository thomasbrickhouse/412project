# def tsp_approx(graph, timeout):
#   randomly select a node to start
#   Perform a greedy approach to traverse the complete graph
#   The output will be the shortest
#   Repeat the process multiple times to get different shortest paths and minimum costs
#   Stop running after a certain amount of time to get the best shortest path and minimum cost

import random
import time
import sys

def parse_input(input_string):
    lines = input_string.strip().split("\n")
    graph = {}

    for line in lines[1:]:
        node1, node2, weight = line.split()
        weight = float(weight)
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


def one_tsp(graph):
    start_node = random.choice(list(graph.keys()))
    current_path = [start_node]
    current_cost = 0
    unvisited = set(graph.keys())
    unvisited.remove(start_node)

    while unvisited:
        last_node = current_path[-1]
        next_node = min(unvisited, key=lambda node: graph[last_node][node])
        current_cost += graph[last_node][next_node]
        current_path.append(next_node)
        unvisited.remove(next_node)

    current_cost += graph[current_path[-1]][start_node]
    current_path.append(start_node)

    return current_path, current_cost


def tsp_approx(graph, timeout=None, single_iteration=False):
    if single_iteration:
        return one_tsp(graph)

    best_path = None
    best_cost = float("inf")
    start_time = time.time()

    while time.time() - start_time < timeout:
        current_path, current_cost = one_tsp(graph)
        if current_cost < best_cost:
            best_cost = current_cost
            best_path = current_path

    return best_path, best_cost


if __name__ == "__main__":
    input_data = sys.stdin.read()

    graph = parse_input(input_data)

    timeout = 1
    best_path, best_cost = tsp_approx(graph, timeout)

    print(f"{best_cost:.4f}")
    print(" ".join(best_path))
