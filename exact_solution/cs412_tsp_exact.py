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
    nodes = list(graph.keys())
    if len(nodes) < 2:
        return nodes, 0.0  # Handle trivial cases with 0 or 1 node.

    best_path = None
    min_cost = float('inf')

    # Generate all permutations of nodes, treating the first node as the start
    start_node = nodes[0]
    other_nodes = nodes[1:]  # All nodes except the start
    for perm in permutations(other_nodes):
        path = [start_node] + list(perm) + [start_node]  # Complete path

        # Calculate the total cost for this permutation
        current_cost = 0
        valid = True
        for i in range(len(path) - 1):
            if path[i + 1] in graph[path[i]]:
                current_cost += graph[path[i]][path[i + 1]]
            else:
                valid = False
                break

        # Update the best path and cost
        if valid and current_cost < min_cost:
            min_cost = current_cost
            best_path = path

    return best_path, min_cost

def main():
    input_data = sys.stdin.read()

    graph = parse_input(input_data)

    best_path, min_cost = tsp_exact(graph)

    print(f"{min_cost:.4f}")
    print(" ".join(best_path))

if __name__ == "__main__":
    main()
