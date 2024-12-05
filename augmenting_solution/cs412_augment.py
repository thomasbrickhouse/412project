import sys
from collections import defaultdict
import heapq
import random

# "Given a list of cities and the distances between each pair of cities, 
# what is the shortest possible route that visits each city exactly once and returns to the origin city?"

# TSP can be modeled as an undirected weighted graph, such that cities are the graph's vertices, paths are the graph's edges, 
# and a path's distance is the edge's weight. It is a minimization problem starting and finishing at a specified vertex after 
# having visited each other vertex exactly once. Often, the model is a complete graph (i.e., each pair of vertices is connected by an edge). 
# If no path exists between two cities, then adding a sufficiently long edge will complete the graph without affecting the optimal tour.

# run minimum spanning tree on same inputs and compare for analysis
# MST = Lower bound helps to estimate final answer between approximate

# Heres what I need to present:
    # why MST is a good lower bound for TSP
    # convince Molloy that MST is polynomial time computable
    # showcase the lower bound, optimal, approximate exist --> test cases
    # run all of these on something the optimal cannot complete --> plot on graph

    # complete graph and generate random weights 
    # 10 different graphs
    # google mat.plot.lib

def generate_complete_graph_test_case(num_vertices, weight_range=(1.0, 100.0)):
    vertices = [chr(97 + i) for i in range(num_vertices)]  # Generate vertices 'a', 'b', 'c', etc.
    edges = []

    # Generate all edges for a complete graph
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            u, v = vertices[i], vertices[j]
            weight = round(random.uniform(*weight_range), 1)
            edges.append((u, v, weight))

    # Format the output
    test_case = f"{num_vertices} {len(edges)}\n"
    test_case += "\n".join(f"{u} {v} {w}" for u, v, w in edges)

    # Put this in main
    # # Parameters
    # num_vertices = 3
    # weight_range = (1.0, 50.0)

    # # Generate the test case
    # test_case = generate_complete_graph_test_case(num_vertices, weight_range)
    # print(test_case)
    return test_case


# Calculate the MST using Prim's Algorithm
def calculate_mst(graph, num_cities, start_city=None):
    if start_city is None:
        start_city = next(iter(graph.keys()))  # Default to the first city in the graph
    
    mst = defaultdict(list)
    visited = set()
    min_heap = [(0, start_city, None)]  # (weight, current_node, parent_node)
    total_weight = 0

    while len(visited) < num_cities:
        weight, current, parent = heapq.heappop(min_heap)
        if current in visited:
            continue
        visited.add(current)
        if parent:
            mst[parent].append((current, weight))
            mst[current].append((parent, weight))
            total_weight += weight
        # Traverse through the neighbors
        for neighbor, w in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, current))

    return mst, total_weight

# Helper function to extract edges from the MST dictionary
def mst_edges(mst):
    edges = []
    for city, neighbors in mst.items():
        for neighbor, weight in neighbors:
            if city < neighbor:  # Avoid duplicate edges
                edges.append((city, neighbor, weight))
    return edges

# Calculate the lower bound by adding the MST weight to the lightest edge outside of it
def calculate_lower_bound(graph, mst, mst_weight):
    mst_edge_set = set((min(u, v), max(u, v)) for u, v, w in mst_edges(mst))
    lightest_edge_weight = float('inf')
    for city, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            edge = (min(city, neighbor), max(city, neighbor))
            if edge not in mst_edge_set and weight < lightest_edge_weight:
                lightest_edge_weight = weight
    return mst_weight + lightest_edge_weight

# Main function
def main():
    # # Read the number of vertices (n) and edges (m)
    # n, m = map(int, input().strip().split())
    
    # # Initialize graph as an adjacency list
    # graph = defaultdict(dict)
    
    # # Read each edge
    # for _ in range(m):
    #     u, v, w = input().strip().split()
    #     w = float(w)
    #     graph[u][v] = w
    #     graph[v][u] = w  # Undirected graph
    
    # graph, num_cities = graph, n

    # # Compute the MST
    # mst, mst_weight = calculate_mst(graph, num_cities)

    # # Compute the lower bound for TSP
    # lower_bound = calculate_lower_bound(graph, mst, mst_weight)

    # # Output the results
    # print(f"Lower bound cost: {lower_bound:.4f}")

    # Parameters
    num_vertices = 3
    weight_range = (1.0, 50.0)

    # Generate the test case
    test_case = generate_complete_graph_test_case(num_vertices, weight_range)
    print(test_case)


if __name__ == "__main__":
    main()
