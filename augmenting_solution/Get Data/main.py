import sys
from collections import defaultdict
import heapq
import random

import cs412_augment
import cs412_tsp_approx
import cs412_tsp_exact

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


def main():
    # Read input from stdin
    # input_data = sys.stdin.read()
    vertices = 15
    input_data = cs412_augment.generate_complete_graph_test_case(vertices, (1.0, 50.0))

    # Parse the input graph
    graph = parse_input(input_data)
    
    graph, num_cities = graph, vertices # change this number for vertices

    # EXACT
    best_path, min_cost = cs412_tsp_exact.tsp_exact(graph)

    # Print the output in the required format
    print(f"Exact cost: {min_cost:.4f}")
    print(" ".join(best_path))

    # APPROXIMATE
    timeout = 1
    best_path, best_cost = cs412_tsp_approx.tsp_approx(graph, timeout)

    print(f"Approximate cost: {best_cost:.4f}")
    print(" ".join(best_path))

    # AUGMENT LOWER BOUND
    # Compute the MST
    mst, mst_weight = cs412_augment.calculate_mst(graph, num_cities)

    # Compute the lower bound for TSP
    lower_bound = cs412_augment.calculate_lower_bound(graph, mst, mst_weight)

    # Output the results
    print(f"Lower bound cost: {lower_bound:.4f}")

if __name__ == "__main__":
    main()
