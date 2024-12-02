import random
import heapq
from collections import defaultdict

# Step 1: Generate a Complete Graph with Random Weights
def generate_complete_graph(num_cities, weight_range=(1, 100)):
    """
    Generates a complete graph with random edge weights.
    Args:
        num_cities (int): Number of nodes (cities) in the graph.
        weight_range (tuple): Range (min, max) of random edge weights.
    Returns:
        list: A list of edges with their weights.
    """
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            weight = random.randint(*weight_range)
            edges.append((f"City_{i + 1}", f"City_{j + 1}", weight))
    return edges

# Step 2: Calculate the MST using Prim's Algorithm
def calculate_mst(edges, num_cities):
    """
    Calculates the MST using Prim's algorithm.
    Args:
        edges (list): List of graph edges as (node1, node2, weight).
        num_cities (int): Total number of cities/nodes.
    Returns:
        tuple: MST as an adjacency list and the total MST weight.
    """
    # Convert edge list to adjacency list
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Prim's algorithm
    mst = defaultdict(list)
    visited = set()
    min_heap = [(0, "City_1", None)]  # (weight, current_node, parent_node)
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

# Step 3: Create a Full Tour from the MST
def create_tsp_tour(mst, start_city, original_edges):
    """
    Convert the MST into a full tour using DFS and add the correct edge back to the start.
    Args:
        mst (dict): The MST as an adjacency list.
        start_city (str): The starting city.
        original_edges (list): List of all original graph edges.
    Returns:
        tuple: A list representing the TSP tour and the total weight.
    """
    visited = set()
    tour = []
    total_weight = 0

    def dfs(city):
        visited.add(city)
        tour.append(city)
        for neighbor, weight in mst[city]:
            if neighbor not in visited:
                nonlocal total_weight
                total_weight += weight
                dfs(neighbor)

    # Perform DFS traversal from the starting city
    dfs(start_city)

    # Calculate the weight of the edge returning to the starting city
    last_city = tour[-1]
    return_to_start_weight = None
    for u, v, weight in original_edges:
        if (u == last_city and v == start_city) or (v == last_city and u == start_city):
            return_to_start_weight = weight
            break

    if return_to_start_weight is None:
        raise ValueError("No edge found to return to the starting city.")

    # Add the return edge weight to the total weight
    total_weight += return_to_start_weight
    tour.append(start_city)

    return tour, total_weight

# Step 4: Run and Test the Code
def main():
    num_cities = 5  # Adjust this as needed
    weight_range = (10, 50)  # Adjust weight range as needed

    # Generate the graph
    graph_edges = generate_complete_graph(num_cities, weight_range)
    print("Graph Edges (City1, City2, Weight):")
    for edge in graph_edges:
        print(edge)

    # Calculate the MST
    mst, mst_weight = calculate_mst(graph_edges, num_cities)
    print("\nMinimum Spanning Tree Edges:")
    for city, connections in mst.items():
        for neighbor, weight in connections:
            if city < neighbor:  # Print each edge only once
                print(f"({city}, {neighbor}, {weight})")
    print(f"Total Weight of MST: {mst_weight}")

    # Convert MST to TSP Tour
    tsp_tour, tsp_weight = create_tsp_tour(mst, "City_1", graph_edges)
    print("\nTSP Tour:")
    print(" -> ".join(tsp_tour))
    print(f"Total Weight of TSP Tour: {tsp_weight}")

if __name__ == "__main__":
    main()
