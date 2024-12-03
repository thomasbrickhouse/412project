# def tsp_approx(graph, timeout):
#   randomly select a node to start
#   Perform a greedy approach to traverse the complete graph
#   The output will be the shortest
#   Repeat the process multiple times to get different shortest paths and minimum costs
#   Stop running after a certain amount of time to get the best shortest path and minimum cost


import random
import time


def generate_complete_graph(num_cities, weight_range=(1, 100)):
    """
    Generates a complete graph with symmetric edge weights.
    Args:
        num_cities (int): Number of nodes (cities) in the graph.
        weight_range (tuple): Range (min, max) of random edge weights.
    Returns:
        dict: A dictionary representation of the graph as an adjacency matrix.
    """
    graph = {}
    for i in range(1, num_cities + 1):
        city_i = f"City_{i}"
        graph[city_i] = {}
        for j in range(1, num_cities + 1):
            if i != j:  # No self-loops
                city_j = f"City_{j}"
                if city_j not in graph[city_i]:  # Avoid duplicating the edge
                    weight = random.randint(*weight_range)
                    graph[city_i][city_j] = weight
                    graph[city_j] = graph.get(city_j, {})
                    graph[city_j][city_i] = weight
    return graph


def print_graph(graph):
    """
    Prints the graph in a readable format for debugging.
    Args:
        graph (dict): The graph as an adjacency matrix.
    """
    print("Graph Representation (Adjacency Matrix):")
    for city, neighbors in graph.items():
        neighbor_str = ", ".join(
            f"{neighbor}: {weight}" for neighbor, weight in neighbors.items()
        )
        print(f"{city} -> {neighbor_str}")
    print()


def tsp_approx(graph, timeout):
    # Initialize variables to keep track of the best solution
    best_path = None
    best_cost = float("inf")

    # Record the start time
    start_time = time.time()

    # Continue running until the timeout
    while time.time() - start_time < timeout:
        # Randomly select a starting node
        start_node = random.choice(list(graph.keys()))

        # Perform a greedy approach to find a solution
        current_path = [start_node]
        current_cost = 0
        unvisited = set(graph.keys())
        unvisited.remove(start_node)

        while unvisited:
            # Find the nearest neighbor to the current node
            last_node = current_path[-1]
            next_node = min(unvisited, key=lambda node: graph[last_node][node])
            current_cost += graph[last_node][next_node]
            current_path.append(next_node)
            unvisited.remove(next_node)

        # Complete the cycle by returning to the start node
        current_cost += graph[current_path[-1]][start_node]
        current_path.append(start_node)

        # Check if this path is better than the current best
        if current_cost < best_cost:
            best_cost = current_cost
            best_path = current_path

    return best_path, best_cost


# Generate a graph with 5 cities for debugging (you can increase this)
num_cities = 5 
graph = generate_complete_graph(num_cities)

# Print the generated graph
print_graph(graph)

# Run the TSP approximation algorithm
timeout = 5  # Run for 5 seconds for quick testing
shortest_path, minimum_cost = tsp_approx(graph, timeout)

# Print the results
print("\nBest Path:", shortest_path)
print("Minimum Cost:", minimum_cost)
