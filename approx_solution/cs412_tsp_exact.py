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


# ChatGPT generated code for purpose of creating graphs:

def tsp_exact(graph):
    """Solves the TSP exactly using brute-force."""
    vertices = list(graph.keys())
    start_node = vertices[0]  # Fix the start node to reduce redundant cycles
    min_cost = float("inf")
    best_path = []

    # Generate all permutations of the nodes (excluding the starting node)
    for perm in permutations(vertices[1:]):
        path = [start_node] + list(perm) + [start_node]
        cost = 0

        # Calculate the total cost of this path
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        # Update the minimum cost and best path
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost


def main():
    """Main function for Gradescope autograder."""
    # Read input from stdin
    input_data = sys.stdin.read()

    # Parse the input graph
    graph = parse_input(input_data)

    # Solve the TSP exactly
    best_path, min_cost = tsp_exact(graph)

    # Print the output in the required format
    print(f"{min_cost:.4f}")
    print(" ".join(best_path))


# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()
