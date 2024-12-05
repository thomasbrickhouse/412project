from itertools import permutations
import sys


def parse_input(input_string):
    lines = input_string.strip().split("\n")
    num_nodes, num_edges = map(int, lines[0].split())
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

def tsp_exact(graph):
    return 0, 0

def main():
    input_data = sys.stdin.read()

    graph = parse_input(input_data)

    best_path, min_cost = tsp_exact(graph)

    print(f"{min_cost:.4f}")
    print(" ".join(best_path))

if __name__ == "__main__":
    main()
