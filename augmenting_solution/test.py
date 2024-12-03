import random
import heapq
from collections import defaultdict

# Generate a Complete Graph with Random Weights
def generate_complete_graph(num_cities, weight_range=(1, 100)):
    if num_cities < 2:
        raise ValueError("The graph must have at least 2 cities.")
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            weight = random.randint(*weight_range)
            edges.append((f"City_{i + 1}", f"City_{j + 1}", weight))
    return edges

# Calculate the MST using Prim's Algorithm
def calculate_mst(edges, num_cities, start_city="City_1"):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

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
        for neighbor, w in adj[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, current))

    return mst, total_weight

# Calculate the lower bound for TSP
def calculate_lower_bound(graph_edges, mst_edges, mst_weight):
    # Convert MST edges into a set for easy lookup
    mst_edge_set = set((min(u, v), max(u, v)) for u, v, w in mst_edges)

    # Find the lightest edge not in the MST
    lightest_edge_weight = float('inf')
    for u, v, w in graph_edges:
        edge = (min(u, v), max(u, v))
        if edge not in mst_edge_set and w < lightest_edge_weight:
            lightest_edge_weight = w

    # If no additional edge is found, just return the MST weight
    if lightest_edge_weight == float('inf'):
        return mst_weight

    return mst_weight + lightest_edge_weight

# Main function
def main():
    num_cities = 5
    weight_range = (10, 50)

    # Generate the graph
    graph_edges = generate_complete_graph(num_cities, weight_range)
    print("Graph Edges (City1, City2, Weight):")
    for edge in graph_edges:
        print(edge)

    # Compute the MST
    mst, mst_weight = calculate_mst(graph_edges, num_cities)
    print("\nMinimum Spanning Tree Edges:")
    mst_edges = []
    for city, connections in mst.items():
        for neighbor, weight in connections:
            if city < neighbor:  # To ensure each edge is printed once
                mst_edges.append((city, neighbor, weight))
    mst_edges.sort()
    for edge in mst_edges:
        print(f"({edge[0]}, {edge[1]}, {edge[2]})")
    print(f"Total Weight of MST: {mst_weight}")

    # Compute the lower bound for TSP
    lower_bound = calculate_lower_bound(graph_edges, mst_edges, mst_weight)
    print(f"Lower Bound for TSP (MST + Lightest Extra Edge): {lower_bound}")

if __name__ == "__main__":
    main()
